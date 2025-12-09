import sys
import asyncio
from aiogram import Bot
from aiogram.exceptions import TelegramAPIError
from config import TELEGRAM_TEXT_FILEPATH, BOT_TOKEN, GROUP_ID

async def send_to_telegram():
    bot = Bot(token=BOT_TOKEN)
    print(TELEGRAM_TEXT_FILEPATH)
    try:
        with open(TELEGRAM_TEXT_FILEPATH, 'r', encoding='utf-8') as file:
            message = file.read()
    except FileNotFoundError:
        print(f"Файл {TELEGRAM_TEXT_FILEPATH} не найден!")
        return
    except Exception as e:
        print(f"Ошибка при чтении файла: {str(e)}")
        return

    try:
        await bot.send_message(chat_id=GROUP_ID, text=message, parse_mode="HTML")
        print("Сообщение успешно отправлено в Telegram")
    except TelegramAPIError as e:
        print(f"Ошибка Telegram API: {str(e)}")
    finally:
        await bot.session.close()

def main():
    asyncio.run(send_to_telegram())

if __name__ == "__main__":
    main()