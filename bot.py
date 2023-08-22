import asyncio

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage  # не надежно, посмотреть Redis

from config_data import config
from handlers import user_handlers


async def main():
    bot = Bot(token=config.TOKEN)
    storage: MemoryStorage = MemoryStorage()
    dp: Dispatcher = Dispatcher(storage=storage)

    # Регистрируем роутер в диспетчере
    dp.include_router(user_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    await storage.close()


if __name__ == '__main__':
    asyncio.run(main())
