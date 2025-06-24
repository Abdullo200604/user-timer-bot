from aiogram import types, Router
from aiogram.filters import Command


router=Router()


@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Assalomu Aleykum! Istalgan vaqtni @Pdptimebot HH:MM:SS formatida yuboring, teskari sanash boshlanadi.")