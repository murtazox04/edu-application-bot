from aiogram import F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from decouple import config

from loader import dp, bot, router


class Form(StatesGroup):
    get_fullname = State()
    get_phonenumber = State()
    get_goals = State()


@router.message(F.text == "📝 Murojaat")
async def application(message: Message, state: FSMContext) -> None:
    text = "F.I.SH. kiriting!\nMisol uchun: Abdusattor Abdullayev yoki G'anisher Safaraliyev Abdusamad o'g'li"
    await message.reply(text=text)
    await state.set_state(Form.get_fullname)


@router.message(Form.get_fullname)
async def get_fullname(message: Message, state: FSMContext) -> None:
    full_name = message.text
    await state.update_data(full_name=full_name)
    text = "Bog'lanish uchun telefon raqamingizni qoldiring\nMisol uchun: +998900459442 yoki 900459442"
    await message.reply(text=text)
    await state.set_state(Form.get_phonenumber)


@router.message(Form.get_phonenumber)
async def get_fullname(message: Message, state: FSMContext) -> None:
    phone_number = message.text
    await state.update_data(phone_number=phone_number)
    text = "Siz aynan qaysi kursga yozilmoqchi ekanligingiz va bizdan nimalarni kutayotganingizni qisqacha yozing."
    await message.reply(text=text)
    await state.set_state(Form.get_goals)


@router.message(Form.get_goals)
async def get_goals(message: Message, state: FSMContext) -> None:
    goals = message.text
    data = await state.get_data()
    full_name = data.get("full_name")
    phone_number = data.get("phone_number")
    username = message.from_user.username
    text = ""

    if username:
        text += "Telegram: {username}\n".format(username=username)

    text += "<b>Yangi murojaat!</b>\nF.I.SH: {full_name}\nTelefon raqami: {phone_number}\nMaqsadi: {goals}".format(
        full_name=full_name, phone_number=phone_number, goals=goals)

    await bot.send_message(chat_id=config("CHAT_ID"), text=text)
    await message.answer(text="Ma'lumotlaringiz muvaffaqiyatli yuborildi! Tezda siz bilan bog'lanamiz.")
