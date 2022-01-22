from aiogram import Bot
from aiogram.dispatcher import Dispatcher
#import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage
storage = MemoryStorage()
#bot = Bot(token=os.getenv(('TOKEN')))
bot = Bot(token="5034576426:AAHUKodA0IinoOo9K6YXlP6W1VwbfV3rBuQ")
dp = Dispatcher(bot, storage=storage)
