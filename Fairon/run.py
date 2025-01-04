import asyncio
from aiogram import Bot, Dispatcher
from iron.hand import router
from config import TOKEN


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher() 
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except:
        print('Exit')

