from aiogram import types
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from loader import dp
from Tiktok import tk
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.builtin import CallbackQuery
@dp.message_handler(Text(startswith='https://youtube-media-downloader.p.rapidapi.com'))
async def test(message:types.Message):
    natija = tk(message.text)
    qoshiq =natija['music']

    btn = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="حمل الموسيقى",url="{}".format(qoshiq))]
        ]
    )
    await message.answer_audio(natija['video'],reply_markup=btn)
