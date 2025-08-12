import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# Токен берём из переменной окружения (задать в Render)
TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("Ас-саляму алейкум\nЗдравствуйте")

async def main():
    await dp.start_polling(bot)

if name == "main":
    asyncio.run(main())
