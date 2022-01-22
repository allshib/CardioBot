from create_bot import bot, dp
from aiogram import types, Dispatcher
from handlers import config
from handlers.connect import plots, CreateDiag, UseProgramNew
from keyboards.keyb import start_kb


async def starts(message: types.Message):
    await bot.send_message(message.from_user.id, 'Привет, для начала обследования введите /st1', reply_markup=start_kb)

    #diag = CreateDiag(config.defaultStage, config.defaultDate, config.defaultArr)
    #mylist = UseProgramNew(diag)
    #await bot.send_message(message.from_user.id, str(mylist))

    #mylist = mylist.replace('[', '')
    #mylist = mylist.replace(']', '')
    #print(mylist)

    #ready = list(map(float, mylist.split(',')))
    #if len(ready) == 7:
    #    temp = ready[2]
    #    ready.insert(2, temp)

    #print(ready)
    #await plots(message, ready)


async def St1(message: types.Message):
    await bot.send_message(message.from_user.id, 'Привет', reply_markup=start_kb)


def register_handlers_start(dp: Dispatcher):
    dp.register_message_handler(starts, commands=['start', 'help'])
    dp.register_message_handler(St1, commands=['st'])
