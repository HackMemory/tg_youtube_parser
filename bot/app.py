from handlers.users import register_handlers_common, register_handlers_search
from loader import dp
from utils.set_bot_commands import set_default_commands

from aiogram import executor


async def on_startup(dispatcher):
    #Model.metadata.create_all(db_engine)
    await set_default_commands(dispatcher)


if __name__ == '__main__':
    register_handlers_common(dp)
    register_handlers_search(dp)
    executor.start_polling(dp, on_startup=on_startup)