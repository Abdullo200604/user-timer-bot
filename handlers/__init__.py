from handlers import start, timer_handler
from aiogram import Dispatcher


def register_all_handlers(dp: Dispatcher):
    dp.include_router(start.router)
    dp.include_router(timer.router)