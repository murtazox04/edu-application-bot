from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📝 Murojaat"),
            # KeyboardButton(text="Kurslar haqida ma'lumot"),
        ],
    ],
    resize_keyboard=True
)

check_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ha✅"),
            KeyboardButton(text="Yo'q❌"),
        ]
    ]
)
