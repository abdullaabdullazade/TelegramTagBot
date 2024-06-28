# TelegramTagBot 🤖

TelegramTagBot is a Python-based Telegram bot that allows users to tag all members in a group chat. The bot requires admin permissions to function properly. This bot is built using the Pyrogram library and SQLite for user management.

TelegramTagBot, qrup çatında bütün üzvləri işarələməyə imkan verən Python əsaslı Telegram botudur. Botun düzgün işləməsi üçün administrator icazələri tələb olunur. Bu bot Pyrogram kitabxanası və istifadəçi idarəetməsi üçün SQLite istifadə edərək qurulub.

## Features / Xüsusiyyətlər 🌟

- Tag all members in a group chat / Qrup çatında bütün üzvləri işarələmək
- Start and stop tagging with commands / Komandalarla işarələməyə başlamaq və dayandırmaq
- Check if the bot is working / Botun işlədiyini yoxlamaq
- User-friendly messages and prompts / İstifadəçi dostu mesajlar və göstərişlər

## Requirements / Tələblər 📦

- Python 3.6+
- Pyrogram
- SQLite3

## Installation / Quraşdırma ⚙️

1. **Clone the repository** / **Repozitoriyanı klonlayın**:

    ```sh
    git clone https://github.com/abdullaabdullazade/TelegramTagBot.git
    cd TelegramTagBot
    ```

2. **Install the required Python packages** / **Tələb olunan Python paketlərini quraşdırın**:

    ```sh
    pip install pyrogram
    ```

3. **Set up your Telegram bot** / **Telegram botunuzu qurun**:

    - Create a new bot on Telegram by talking to [BotFather](https://t.me/BotFather).
    - Get your `api_id`, `api_hash`, and `bot_token` from BotFather.
    - [BotFather](https://t.me/BotFather) ilə danışaraq Telegramda yeni bot yaradın.
    - `api_id`, `api_hash` və `bot_token` məlumatlarınızı BotFather-dan əldə edin.

4. **Configure the bot with your credentials** / **Botu məlumatlarınızla konfiqurasiya edin**:

    Replace the placeholders in the script with your credentials.

    Skriptdəki yer tutucuları məlumatlarınızla əvəz edin.

    ```python
    api_id = 'YOUR_API_ID'  # write api_id
    api_hash = 'YOUR_API_HASH'  # write api_hash
    bot_token = 'YOUR_BOT_TOKEN'  # write bot_token
    your_telegram_username = 'YOUR_TELEGRAM_USERNAME'  # without @ / @ işarəsi olmadan
    your_telegram_bot_username = 'YOUR_TELEGRAM_BOT_USERNAME'  # without @ / @ işarəsi olmadan
    ```

5. **Run the bot** / **Botu işə salın**:

    ```sh
    python bot.py
    ```

## Usage / İstifadə 🛠️

After starting the bot, you can use the following commands:

Botu işə saldıqdan sonra aşağıdakı komandaları istifadə edə bilərsiniz:

### Commands / Komandalar 📝

- `/start` - Check if the bot is working / Botun işlədiyini yoxlayın
- `/all` - Tag everyone in the group. For example: /all your_message / Qrupdakı hər kəsi işarələyin. Məsələn: /all your_message
- `/close` - Stop tagging / İşarələməni dayandırın
- `/help` - Display help message / Yardım mesajını göstərin

### Adding the Bot to a Group / Botu Qrupa Əlavə Etmək ➕

To add the bot to a group, click the button provided in the start message or add the bot manually. Make sure to grant the bot admin permissions.

Botu qrupa əlavə etmək üçün, start mesajında göstərilən düyməni klikləyin və ya botu əl ilə əlavə edin. Botun administrator icazələrini aldığından əmin olun.

### Example / Nümunə 📋

1. Add the bot to your group / Botu qrupunuza əlavə edin.
2. Use the `/start` command to check if the bot is active / Botun aktiv olduğunu yoxlamaq üçün `/start` əmrindən istifadə edin.
3. Use the `/all` command to tag all members in the group / Qrupdakı bütün üzvləri işarələmək üçün `/all` əmrindən istifadə edin.
4. Use the `/close` command to stop tagging / İşarələməni dayandırmaq üçün `/close` əmrindən istifadə edin.

## Contributing / Töhfə Vermə 🤝

Feel free to fork this project and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

Bu layihəni fork edib pull request göndərməkdən çəkinməyin. Böyük dəyişikliklər üçün əvvəlcə dəyişmək istədiyinizi müzakirə etmək üçün bir issue açın.


## Contact / Əlaqə 📬

If you have any questions, feel free to open an issue or reach out to me at [abdulla.abdullazade.2008@gmail.com](mailto:abdulla.abdullazade.2008@gmail.com).

Hər hansı bir sualınız varsa, xahiş edirəm, bir məsələ açın və ya mənə [abdulla.abdullazade.2008@gmail.com](mailto:abdulla.abdullazade.2008@gmail.com) ünvanından müraciət edin.

---