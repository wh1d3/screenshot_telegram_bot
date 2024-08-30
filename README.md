# Telegram Screenshot Bot

Telegram Screenshot Bot is a simple bot that takes a URL from a user, navigates to the page, and sends back a screenshot. The bot is built using `Telethon` and `pyppeteer`, allowing for interaction with Telegram and automated browser tasks.

![Screenshot Example](https://i.imgur.com/iZwmpii.png)

## Features

- Accepts URLs from users in Telegram.
- Navigates to the given URL and takes a screenshot of the webpage.
- Sends the screenshot back to the user in Telegram.
- Handles multiple URLs in a single message.
- Automatically names screenshots based on the URL and the timestamp.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/wh1d3/screenshot_telegram_bot.git
   cd screenshot_telegram_bot
   ```
2. Create a virtual environment and install dependencies:
     ```bash
    python -m venv venv
    pip install -r requirements.txt
    ```
3. Set up your Telegram bot: 
**Obtain your API_ID, API_HASH, and BOT_TOKEN from Telegram's BotFather.**
4. Run the bot:
   ```bash
   python main.py
   ```

# Usage
- **Start the bot with the /start command.**
- **Send a message with a URL. The bot will visit the URL and send back a screenshot of the page.**
- **The bot supports multiple URLs in a single message.**

# Commands
1) /start - Start the bot and get a welcome message.
2) Send any message with a URL to receive a screenshot of the page.

# Technologies Used
* Python 3.7+: Main programming language.
* Telethon: For interacting with the Telegram API.
* pyppeteer: For automating the browser to take screenshots.
* requests: To handle HTTP requests.

# Contact
**For any questions or suggestions, feel free to contact me via Telegram**
