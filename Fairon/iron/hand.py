import asyncio
from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.enums import ChatAction

import iron.keyboards as kb

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.bot.send_chat_action(chat_id=message.from_user.id,
                                       action=ChatAction.TYPING)
    await asyncio.sleep(2)
    await message.reply('Привет!', reply_markup=kb.main)
    await message.answer("Как дела?")


@router.message(Command("help"))
async def get_help(message: Message):
    await message.answer("это комманда /help")

@router.message(F.text == "Как дела?")
async def how_are_you(message: Message):
    await message.answer("Ок!")
#@dp.message(F.photo)
#async def get_photo(message: Message):
    #await message.answer(f"ID фото: {message.photo[-1].file_id}")

@router.message(Command("get_photo"))
async def get_photo(message: Message):
    await message.answer_photo(
        photo="AgACAgIAAxkBAAMrZzwiI_Ct5o2xL8myd284m6LfxW4AAvfvMRtdQeFJ6Ju9zd5HjqsBAAMCAAN4AAM2BA",
        caption="Картиночка")

@router.message()
async def echo(message: Message):
    await message.answer("Комманда не существует")
