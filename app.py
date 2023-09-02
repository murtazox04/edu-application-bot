import asyncio
import logging
import sys
import handlers

from loader import dp, bot, router

from decouple import config


TOKEN = config('BOT_TOKEN')


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
