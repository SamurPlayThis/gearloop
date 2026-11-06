import os
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup, WebAppInfo
from aiogram.utils.keyboard import ReplyKeyboardBuilder

TOKEN = os.getenv("BOT_TOKEN", "PASTE_BOT_TOKEN_HERE")
WEBAPP_URL = os.getenv("WEBAPP_URL", "https://YOUR-DOMAIN.example")

dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    kb = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="🏭 Открыть GEARLOOP", web_app=WebAppInfo(url=WEBAPP_URL))]],
        resize_keyboard=True
    )
    await message.answer(
        "Добро пожаловать на GEARLOOP! Построй свою производственную империю 🏭",
        reply_markup=kb
    )

async def main():
    if TOKEN == "PASTE_BOT_TOKEN_HERE":
        raise RuntimeError("Укажи токен бота в переменной окружения BOT_TOKEN.")
    bot = Bot(TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
