from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import time
import sqlite3 as sql

api_id = 0000000  # write api_id
api_hash = ''     # write api_hash
bot_token = ''    # write bot_token

app = Client("Botname", api_id=api_id, api_hash=api_hash,
             bot_token=bot_token)

your_telegram_username = ''  # without @
your_telegram_bot_username = ''  # without @

buttons_start = [
    [InlineKeyboardButton("📌Add me to your group", url=f'https://t.me/{your_telegram_bot_username}?startgroup=hbase')]
]

start_text = (
    "🤖 The bot is working. You can now tag group members.\n\n\n"
    "❗️Note: I need to be an admin to be able to tag everyone.\n\n\n"
    f"⚠️ Write to @{your_telegram_username} for comments or suggestions."
)
help_text = (
    "/start   -   Check if the bot is working.\n"
    "/all   -   Tag everyone in the group. For example: /all your_message\n"
    "/close - Stop tagging.\n\n\n"
    "❗️Note: I need to be an admin to tag everyone.\n"
    f"⚠️ For comments or suggestions, write to @{your_telegram_username}."
)
start_tag_text = "Tag started✅"
stop_tag_text = "Tag ended✅"
must_be_admin_text = "I must be an admin to tag"
minimum_members_text = "You must have at least 5 members to tag"

db = sql.connect('database.db', check_same_thread=False)

admins_owner = [enums.ChatMemberStatus.ADMINISTRATOR, enums.ChatMemberStatus.OWNER]

tags = {}

def check_admin(msg):
    try:
        status = app.get_chat_member(msg.chat.id, msg.from_user.id).status
    except:
        return True   # for anonyms admins
    return status in admins_owner

def add_user(msg):
    user = db.execute(f'SELECT * FROM Users WHERE ID={msg.chat.id}')
    if user.fetchone() is None:
        db.execute(f'INSERT INTO Users VALUES({msg.chat.id})')
    db.commit()

def tag(msg):
    text = msg.text.split(' ', 1)[1] if ' ' in msg.text else ""
    app.send_message(msg.chat.id, start_tag_text)
    users = [i.user.mention for i in app.get_chat_members(msg.chat.id) if not i.user.is_deleted and not i.user.is_bot]
    tag_user = 5

    if len(users) >= 5:
        i = 0
        while i <= len(users) and tags[msg.chat.id]:
            if not tags[msg.chat.id]:
                break
            else:
                msg.reply(f"{', '.join(users[i:i+tag_user])} **{text}**")
                time.sleep(1.5)
            i += tag_user
        app.send_message(msg.chat.id, stop_tag_text)
    else:
        msg.reply(minimum_members_text)

@app.on_message(filters.command('start') & filters.private)
def start(bot, msg):
    add_user(msg)
    bot.send_message(msg.chat.id, start_text, reply_markup=InlineKeyboardMarkup(buttons_start))

@app.on_message(filters.command('start') & filters.group)
def start_group(bot, msg):
    add_user(msg)
    bot.send_message(msg.chat.id, start_text)

@app.on_message(filters.command('help') & filters.private)
def help(bot, msg):
    bot.send_message(msg.chat.id, help_text, reply_markup=InlineKeyboardMarkup(buttons_start))

@app.on_message(filters.command('help') & filters.group)
def help_group(bot, msg):
    bot.send_message(msg.chat.id, help_text)

@app.on_message(filters.command('all') & filters.group)
def all(bot, msg):
    global tags
    bot.delete_messages(msg.chat.id, msg.id)
    if check_admin(msg):
        tags[msg.chat.id] = True
        tag(msg)
    else:
        msg.reply(must_be_admin_text)
        

@app.on_message(filters.command('close') & filters.group)
def close(bot, msg):
    global tags
    if check_admin(msg) and tags.get(msg.chat.id):
        tags[msg.chat.id] = False
        bot.delete_messages(msg.chat.id, msg.id)

print("Online")
app.run()


#By @codejavascript