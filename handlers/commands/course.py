from aiogram import types
from aiogram.dispatcher import FSMContext

from decouple import config

from loader import dp


@dp.message_handler(text="Kurslar haqida ma'lumot", state="*")
async def get_courses(message: types.Message, state=FSMContext):
    courses = ""
