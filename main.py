import os
import re
import logging
from datetime import datetime as dt
import requests
from telethon import TelegramClient, events
from pyppeteer import launch

from settings import API_ID, API_HASH, BOT_TOKEN, WIDTH, HEIGHT, DIRECTORY_PATH

logging.basicConfig(level=logging.INFO)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

if not os.path.exists(DIRECTORY_PATH):
    os.makedirs(DIRECTORY_PATH)

async def start_browser():
    browser = await launch(headless=True, args=['--no-sandbox'])
    webpage = await browser.newPage()
    await webpage.setViewport({'width': WIDTH, 'height': HEIGHT})
    return browser, webpage

def get_urls(message: str) -> list[str]:
    regex = r"(https?://[^\s]+)"
    return re.findall(regex, message)

def get_file_name(url: str) -> str:
    u_start = re.sub(r'https?://', '', url)
    u_clean = u_start.replace('/', '_').replace(':', '_')
    return f'{dt.now().strftime("%Y-%m-%d_%H-%M-%S")}_{u_clean}.png'

@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.respond("Привіт! Надішліть мені посилання, і я зроблю скріншот сторінки.")
    raise events.StopPropagation

@bot.on(events.NewMessage(outgoing=False))
async def handle_message(event):
    urls = get_urls(event.text)
    if urls:
        browser, webpage = await start_browser()
        for url in urls:
            try:
                logging.info(f'Отримано URL: {url}')
                response = requests.get(url)
                if response.status_code == 200:
                    await event.respond(f'Виконую скріншот для: {url}')
                    await webpage.goto(url)
                    screenshot_path = os.path.join(DIRECTORY_PATH, get_file_name(url))
                    await webpage.screenshot(path=screenshot_path, fullPage=True)
                    await event.respond(f'Готово! Ось ваш скріншот:', file=screenshot_path)
                else:
                    await event.respond(f'Не вдалося перейти за посиланням. Статус: {response.status_code}')
            except Exception as e:
                logging.error(f'Помилка при обробці {url}: {e}')
                await event.respond(f'Виникла помилка при обробці URL: {url}')
        await browser.close()
    else:
        await event.respond("Будь ласка, надішліть коректне посилання.")

if __name__ == '__main__':
    bot.run_until_disconnected()
