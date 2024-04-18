import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram import F
from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

# Инициализация бота и диспетчера
TOKEN = '6233851565:AAFhXsYEtiGZ9l62mFFBwxIx4-fsFyZ_wZk'

dp = Dispatcher()
bot = Bot(TOKEN, parse_mode=ParseMode.HTML)

# Определение доступных цветов
colors = {
    "Красный": "#FF0000",
    "Оранжевый": "#FFA500",
    "Желтый": "#FFFF00",
    "Зеленый": "#00FF00",
    "Голубой": "#00FFFF",
    "Синий": "#0000FF",
    "Фиолетовый": "#800080"
}


# Обработчик команды /start
@dp.message(Command('start'))
async def start(message: types.Message):
    kb = ReplyKeyboardBuilder()
    for color in colors:
        kb.add(KeyboardButton(text=color))
    await message.answer("Выберите цвет:", reply_markup=kb.as_markup())


# Обработчик кнопок с цветами
@dp.message(F.text.in_(colors))
async def send_color_image(message: types.Message):
    color = message.text
    color_code = colors[color]
    print(color_code[1:])
    image_url = f"https://dummyimage.com/500x500/{color_code[1:]}/{color_code[1:]}"
    await bot.send_photo(chat_id=5061328116, photo=image_url, caption=f"Цвет {color}", parse_mode=ParseMode.HTML)


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
