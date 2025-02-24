from aiogram import Bot, Dispatcher, types
from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
import asyncio
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()

@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Тест веб", web_app=WebAppInfo(url="https://deadmindx.github.io/test_app/"))]
        ]
    )
    await message.answer("Нажми на кнопку для теста Web App:", reply_markup=keyboard)

@dp.message(lambda message: message.web_app_data)
async def web_app_response(message: types.Message):
    await message.answer(f"Ты отправил: {message.web_app_data.data}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())