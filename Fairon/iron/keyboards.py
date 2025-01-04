from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main=ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="корзина"),
     KeyboardButton(text="Каталог")],
    [KeyboardButton(text="Контакты")]
])