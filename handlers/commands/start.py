from aiogram import enums
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.filters import CommandStart, Command
from aiogram.utils.deep_linking import create_start_link, decode_payload

from decouple import config

from loader import dp, router, bot
from keyboards.default import buttons


class Form(StatesGroup):
    chat_id = State()


async def create_link(id: int) -> dict:
    return await create_start_link(bot=bot, payload=id, encode=True)


@router.message(Command("create_ad_link"))
async def create_ad_link(message: Message, state: FSMContext) -> None:
    if message.chat.id == 1767432724:
        text = "Chat ID sini kiriting"
        await message.answer(text=text)
        await state.set_state(Form.chat_id)


@router.message(Form.chat_id)
async def get_chat_id(message: Message, state: FSMContext) -> None:
    chat_id = message.text

    ad_link = await create_link(id=chat_id)

    await message.reply(text=f"Havola: {ad_link}")


@router.message(CommandStart())
async def start(message: Message, command: Command = None) -> None:
    if command:
        args = command.args
        if args:
            reference = decode_payload(args)
            chat = await bot.get_chat(chat_id=reference)
            chat_name = chat.full_name
            text = f"Chat ID: {reference}\nChat Name: {chat_name}\nUshbu chatdan {message.from_user.username} start bosdi!"
            await bot.send_message(chat_id=1767432724, text=text)
    text = "Assalomu alaykum! Botga xush kelibsiz!\nKurslarga yozilish uchun pastdagi <b>Murojaat</b> tugmasini bosing."
    await message.answer(text=text, parse_mode=enums.ParseMode.HTML, reply_markup=buttons)
