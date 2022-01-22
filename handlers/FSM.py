from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher.filters.state import State, StatesGroup
from handlers.connect import plots, CreateDiag, UseProgramNew
from aiogram import types, Dispatcher
from create_bot import dp, bot
import datetime
from handlers.config import *
from keyboards.keyb import *
class User:
    def __init__(self):
        self.Birthday = None
        self.data = ["21", "3", "2", "1", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "1", "0", "0", "0", "0", "0", "0", "172", "50", "0"]


#def CheackingUser(message):
#    if message.chat.id not in users:
#        users.append(message.chat.id)
#        user[message.chat.id] = User()


def validatedate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%d.%m.%Y')
        return False
    except ValueError:
        return True


class FSMSt1(StatesGroup):
    date = State()
    age = State()
    gender = State()
    st1_v4 = State()
    st1_v5 = State()
    st1_v6 = State()
    st1_v7 = State()
    st1_v8 = State()
    st1_v9 = State()
    st1_v10 = State()
    st1_v11 = State()
    st1_v12 = State()
    st1_v13 = State()
    st1_v14 = State()
    st1_v15 = State()
    st1_v16 = State()
    st1_v17 = State()
    st1_v18 = State()
    st1_v19 = State()
    st1_v20 = State()
    st1_v21 = State()
    st1_v22 = State()
    st1_v23 = State()
    st1_v24 = State()
    st1_v25 = State()
    st1_v26 = State()
    st1_v27 = State()
    st1_v28 = State()
    st1_v29 = State()
    st1_v30 = State()
    st1_v31 = State()








async def St1_Start(message: types.Message):
    await FSMSt1.date.set()
    await message.answer('Введите дату рождения в формате xx.xx.xxxx', reply_markup=ReplyKeyboardRemove())


async def St1_Date(message: types.Message, state: FSMContext):
    if validatedate(message.text):
        await message.answer("Пожалуйста, введите корректную дату")
        return
    async with state.proxy() as data:
        data['data'+str(message.from_user.id)] = ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]
        data['b'+str(message.from_user.id)] = "{0}".format(message.text)
    await FSMSt1.next()
    await message.answer('Введите возраст')


async def St1_2(message: types.Message, state: FSMContext):
    if not message.text.isnumeric():
        await message.answer("Пожалуйста, введите корректный возраст")
        return
    elif int(message.text) < 10 or int(message.text) > 130:
        await message.answer("Пожалуйста, введите корректный возраст")
        return

    async with state.proxy() as data:
        data['data'+str(message.from_user.id)][0] = "{0}".format(message.text)
        #await message.answer(str(data['data'+str(message.from_user.id)]))
        #await message.answer(str(data['b'+str(message.from_user.id)]))
    await FSMSt1.next()
    await message.answer(s1_v[2], reply_markup=s1_a3k)


async def St1_3(message: types.Message, state: FSMContext):
    if message.text not in s1_a3:
        await message.answer("Пожалуйста, введите один из предложенных ответов", reply_markup=s1_a3k)
        return

    async with state.proxy() as data:
        if (message.text == s1_a3[0]):
            data['data'+str(message.from_user.id)][1] = "3"
        elif (message.text == s1_a3[1]):
            data['data'+str(message.from_user.id)][1] = "4"
        else:
            await message.answer('что-то не так')
        #await message.answer(str(data['data'+str(message.from_user.id)]))
        #await message.answer(str(data['b'+str(message.from_user.id)]))
    await FSMSt1.next()
    await message.answer(s1_v[3])


async def St1_4(message: types.Message, state: FSMContext):
    if not message.text.isnumeric():
        await message.answer("Пожалуйста, введите корректный рост")
        return
    elif int(message.text) < 100 or int(message.text) > 400:
        await message.answer("Пожалуйста, введите корректный рост")
        return

    async with state.proxy() as data:
        data['data'+str(message.from_user.id)][28] = "{0}".format(message.text)
        #await message.answer(str(data['data'+str(message.from_user.id)]))
        #await message.answer(str(data['b'+str(message.from_user.id)]))
    await FSMSt1.next()
    await message.answer(s1_v[4])
    #await state.finish()


async def St1_5(message: types.Message, state: FSMContext):
    if not message.text.isnumeric():
        await message.answer("Пожалуйста, введите корректный вес")
        return
    elif int(message.text) < 20 or int(message.text) > 500:
        await message.answer("Пожалуйста, введите корректный вес")
        return

    async with state.proxy() as data:
        data['data'+str(message.from_user.id)][29] = "{0}".format(message.text)
        #await message.answer(str(data['data'+str(message.from_user.id)]))
        #await message.answer(str(data['b'+str(message.from_user.id)]))
    await FSMSt1.next()
    await message.answer(s1_v[5], reply_markup=s1_a6k)


async def St1_6(message: types.Message, state: FSMContext):
    if message.text not in s1_a6:
        await message.answer("Пожалуйста, введите один из предложенных ответов", reply_markup=s1_a6k)
        return

    async with state.proxy() as data:
        if (message.text == s1_a6[0]):
            data['data'+str(message.from_user.id)][2] = "1"
        elif (message.text == s1_a6[1]):
            data['data'+str(message.from_user.id)][2] = "2"
        elif (message.text == s1_a6[2]):
            data['data'+str(message.from_user.id)][2] = "3"
        elif (message.text == s1_a6[3]):
            data['data'+str(message.from_user.id)][2] = "4"
        else:
            await message.answer('что-то не так')
        #await message.answer(str(data['data'+str(message.from_user.id)]))
        #await message.answer(str(data['b'+str(message.from_user.id)]))
    #await state.finish()
    await FSMSt1.next()
    await message.answer(s1_v[6], reply_markup=s1_a7k)


async def St1_7(message: types.Message, state: FSMContext):
    if message.text not in s1_a7:
        await message.answer("Пожалуйста, введите один из предложенных ответов", reply_markup=s1_a7k)
        return

    async with state.proxy() as data:
        if (message.text == s1_a7[0]):
            data['data'+str(message.from_user.id)][3] = "1"
        elif (message.text == s1_a7[1]):
            data['data'+str(message.from_user.id)][3] = "0"
        else:
            await message.answer('что-то не так')
    await FSMSt1.next()
    await message.answer(s1_v[7], reply_markup=s1_a8k)


async def St1_8(message: types.Message, state: FSMContext):
    if message.text not in s1_a8:
        await message.answer("Пожалуйста, введите один из предложенных ответов", reply_markup=s1_a8k)
        return

    async with state.proxy() as data:
        if (message.text == s1_a8[0]):
            data['data'+str(message.from_user.id)][19] = "1"
        elif (message.text == s1_a8[1]):
            data['data'+str(message.from_user.id)][19] = "0"
        elif (message.text == s1_a8[2]):
            data['data'+str(message.from_user.id)][19] = "1"
        elif (message.text == s1_a8[3]):
            data['data'+str(message.from_user.id)][19] = "0"
        else:
            await message.answer('что-то не так')
        #await message.answer(str(data['data'+str(message.from_user.id)]))
        #await message.answer(str(data['b'+str(message.from_user.id)]))
    #await state.finish()
    await FSMSt1.next()
    await message.answer(s1_v[8], reply_markup=s1_a9k)


async def St1_9(message: types.Message, state: FSMContext):
    if message.text not in s1_a9:
        await message.answer("Пожалуйста, введите один из предложенных ответов", reply_markup=s1_a9k)
        return

    async with state.proxy() as data:
        if (message.text == s1_a9[0]):
            data['data'+str(message.from_user.id)][20] = "0"
        elif (message.text == s1_a9[1]):
            data['data'+str(message.from_user.id)][20] = "1"
        else:
            await message.answer('что-то не так')
        #await message.answer(str(data['data'+str(message.from_user.id)]))
        #await message.answer(str(data['b'+str(message.from_user.id)]))
    await FSMSt1.next()
    await message.answer(s1_v[9], reply_markup=s1_a10k)


async def St1_10(message: types.Message, state: FSMContext):
    if message.text not in s1_a10:
        await message.answer("Пожалуйста, введите один из предложенных ответов", reply_markup=s1_a10k)
        return

    async with state.proxy() as data:
        if (message.text == s1_a10[0]):
            data['data'+str(message.from_user.id)][21] = "1"
        elif (message.text == s1_a10[1]):
            data['data'+str(message.from_user.id)][21] = "0"
        else:
            await message.answer('что-то не так')
        #await message.answer(str(data['data'+str(message.from_user.id)]))
        #await message.answer(str(data['b'+str(message.from_user.id)]))
    #await state.finish()
    await FSMSt1.next()
    await message.answer(s1_v[10], reply_markup=s1_a10k)


async def St1_11(message: types.Message, state: FSMContext):
    if message.text not in s1_a10:
        await message.answer("Пожалуйста, введите один из предложенных ответов", reply_markup=s1_a10k)
        return

    async with state.proxy() as data:
        if (message.text == s1_a10[0]):
            data['data'+str(message.from_user.id)][22] = "1"
        elif (message.text == s1_a10[1]):
            data['data'+str(message.from_user.id)][22] = "0"
        else:
            await message.answer('что-то не так')
        #await message.answer(str(data['data'+str(message.from_user.id)]))
        #await message.answer(str(data['b'+str(message.from_user.id)]))
    #await state.finish()
    await FSMSt1.next()
    await message.answer(s1_v[11], reply_markup=s1_a10k)


async def St1_12(message: types.Message, state: FSMContext):
    if message.text not in s1_a10:
        await message.answer("Пожалуйста, введите один из предложенных ответов", reply_markup=s1_a10k)
        return

    async with state.proxy() as data:
        if (message.text == s1_a10[0]):
            data['data'+str(message.from_user.id)][23] = "1"
        elif (message.text == s1_a10[1]):
            data['data'+str(message.from_user.id)][23] = "0"
        else:
            await message.answer('что-то не так')
        #await message.answer(str(data['data'+str(message.from_user.id)]))
        #await message.answer(str(data['b'+str(message.from_user.id)]))
    #await state.finish()
    await FSMSt1.next()
    await message.answer(s1_v[12], reply_markup=s1_a10k)


async def St1_13(message: types.Message, state: FSMContext):
    if message.text not in s1_a10:
        await message.answer("Пожалуйста, введите один из предложенных ответов", reply_markup=s1_a10k)
        return

    async with state.proxy() as data:
        if (message.text == s1_a10[0]):
            data['data'+str(message.from_user.id)][24] = "1"
        elif (message.text == s1_a10[1]):
            data['data'+str(message.from_user.id)][24] = "0"
        else:
            await message.answer('что-то не так')
        #await message.answer(str(data['data'+str(message.from_user.id)]))
        #await message.answer(str(data['b'+str(message.from_user.id)]))
    #await state.finish()
    await FSMSt1.next()
    await message.answer(s1_v[13], reply_markup=s1_a10k)


async def St1_14(message: types.Message, state: FSMContext):
    if message.text not in s1_a10:
        await message.answer("Пожалуйста, введите один из предложенных ответов", reply_markup=s1_a10k)
        return

    async with state.proxy() as data:
        if (message.text == s1_a10[0]):
            data['data'+str(message.from_user.id)][25] = "1"
        elif (message.text == s1_a10[1]):
            data['data'+str(message.from_user.id)][25] = "0"
        else:
            await message.answer('что-то не так')
        #await message.answer(str(data['data'+str(message.from_user.id)]))
        #await message.answer(str(data['b'+str(message.from_user.id)]))
    #await state.finish()
    await FSMSt1.next()
    await message.answer(s1_v[14], reply_markup=s1_a10k)


async def St1_15(message: types.Message, state: FSMContext):
    if message.text not in s1_a10:
        await message.answer("Пожалуйста, введите один из предложенных ответов", reply_markup=s1_a10k)
        return

    async with state.proxy() as data:
        if (message.text == s1_a10[0]):
            data['data'+str(message.from_user.id)][26] = "1"
        elif (message.text == s1_a10[1]):
            data['data'+str(message.from_user.id)][26] = "0"
        else:
            await message.answer('что-то не так')
        #await message.answer(str(data['data'+str(message.from_user.id)]))
        #await message.answer(str(data['b'+str(message.from_user.id)]))
    #await state.finish()
    await FSMSt1.next()
    await message.answer(s1_v[15], reply_markup=s1_a10k)


async def St1_16(message: types.Message, state: FSMContext):
    if message.text not in s1_a10:
        await message.answer("Пожалуйста, введите один из предложенных ответов", reply_markup=s1_a10k)
        return

    async with state.proxy() as data:
        if (message.text == s1_a10[0]):
            data['data'+str(message.from_user.id)][27] = "1"
        elif (message.text == s1_a10[1]):
            data['data'+str(message.from_user.id)][27] = "0"
        else:
            await message.answer('что-то не так')
        #await message.answer(str(data['data'+str(message.from_user.id)]))
        #await message.answer(str(data['b'+str(message.from_user.id)]))
    #await state.finish()
    await FSMSt1.next()
    await message.answer(s1_v[16], reply_markup=s1_a10k)


async def St1_17(message: types.Message, state: FSMContext): #здесь
    if message.text not in s1_a10:
        await message.answer("Пожалуйста, введите один из предложенных ответов", reply_markup=s1_a10k)
        return

    async with state.proxy() as data:
        if (message.text == s1_a10[0]):
            data['data'+str(message.from_user.id)][7] = "1"
            await FSMSt1.next()
            await message.answer(s1_v[17], reply_markup=s1_a18k)
        elif (message.text == s1_a10[1]):
            data['data'+str(message.from_user.id)][7] = "0"
            await FSMSt1.st1_v25.set()
            await message.answer(s1_v[24], reply_markup=s1_a25k)
        else:
            await message.answer('что-то не так')
        #await message.answer(str(data['data'+str(message.from_user.id)]))
        #await message.answer(str(data['b'+str(message.from_user.id)]))
    #await state.finish()


async def St1_18(message: types.Message, state: FSMContext):
    if message.text not in s1_a18:
        await message.answer("Пожалуйста, введите один из предложенных ответов", reply_markup=s1_a18k)
        return

    async with state.proxy() as data:
        if (message.text == s1_a18[0]):
            data['data'+str(message.from_user.id)][8] = "1"
        elif (message.text == s1_a18[1]):
            data['data'+str(message.from_user.id)][8] = "0"
        else:
            await message.answer('что-то не так')
        #await message.answer(str(data['data'+str(message.from_user.id)]))
        #await message.answer(str(data['b'+str(message.from_user.id)]))
    #await state.finish()
    await FSMSt1.next()
    await message.answer(s1_v[18], reply_markup=s1_a19k)


async def St1_19(message: types.Message, state: FSMContext):
    if message.text not in s1_a19:
        await message.answer("Пожалуйста, введите один из предложенных ответов", reply_markup=s1_a19k)
        return

    async with state.proxy() as data:
        if (message.text == s1_a19[0]):
            data['data'+str(message.from_user.id)][9] = "0"
        elif (message.text == s1_a19[1]):
            data['data'+str(message.from_user.id)][9] = "1"
        else:
            await message.answer('что-то не так')
        #await message.answer(str(data['data'+str(message.from_user.id)]))
        #await message.answer(str(data['b'+str(message.from_user.id)]))
    #await state.finish()
    await FSMSt1.next()
    await message.answer(s1_v[19], reply_markup=s1_a20k)


async def St1_20(message: types.Message, state: FSMContext):
    if message.text not in s1_a20:
        await message.answer("Пожалуйста, введите один из предложенных ответов", reply_markup=s1_a20k)
        return

    async with state.proxy() as data:
        if (message.text == s1_a20[0]):
            data['data'+str(message.from_user.id)][10] = "0"
        elif (message.text == s1_a20[1]):
            data['data'+str(message.from_user.id)][10] = "1"
        else:
            await message.answer('что-то не так')
        #await message.answer(str(data['data'+str(message.from_user.id)]))
        #await message.answer(str(data['b'+str(message.from_user.id)]))
    #await state.finish()
    await FSMSt1.next()
    await message.answer(s1_v[20], reply_markup=s1_a21k)


async def St1_21(message: types.Message, state: FSMContext):
    if message.text not in s1_a21:
        await message.answer("Пожалуйста, введите один из предложенных ответов", reply_markup=s1_a21k)
        return

    async with state.proxy() as data:
        if (message.text == s1_a21[0]):
            data['data'+str(message.from_user.id)][11] = "0"
        elif (message.text == s1_a21[1]):
            data['data'+str(message.from_user.id)][11] = "1"
        elif (message.text == s1_a21[2]):
            data['data'+str(message.from_user.id)][11] = "2"
        else:
            await message.answer('что-то не так')
        #await message.answer(str(data['data'+str(message.from_user.id)]))
        #await message.answer(str(data['b'+str(message.from_user.id)]))
    #await state.finish()
    await FSMSt1.next()
    await message.answer(s1_v[21], reply_markup=s1_a22k)


async def St1_22(message: types.Message, state: FSMContext):
    if message.text not in s1_a22:
        await message.answer("Пожалуйста, введите один из предложенных ответов", reply_markup=s1_a22k)
        return

    async with state.proxy() as data:
        if (message.text == s1_a22[0]):
            data['data'+str(message.from_user.id)][12] = "0"
        elif (message.text == s1_a22[1]):
            data['data'+str(message.from_user.id)][12] = "1"
        else:
            await message.answer('что-то не так')
        #await message.answer(str(data['data'+str(message.from_user.id)]))
        #await message.answer(str(data['b'+str(message.from_user.id)]))
    #await state.finish()
    await FSMSt1.next()
    await message.answer(s1_v[22], reply_markup=s1_a23k)


async def St1_23(message: types.Message, state: FSMContext):
    if message.text not in s1_a23:
        await message.answer("Пожалуйста, введите один из предложенных ответов", reply_markup=s1_a23k)
        return

    async with state.proxy() as data:
        if (message.text == s1_a23[0]):
            data['data'+str(message.from_user.id)][13] = "0"
        elif (message.text == s1_a23[1]):
            data['data'+str(message.from_user.id)][13] = "0"
        elif (message.text == s1_a23[2]):
            data['data'+str(message.from_user.id)][13] = "1"
        elif (message.text == s1_a23[3]):
            data['data'+str(message.from_user.id)][13] = "2"
        elif (message.text == s1_a23[4]):
            data['data'+str(message.from_user.id)][13] = "0"
        else:
            await message.answer('что-то не так')
        #await message.answer(str(data['data'+str(message.from_user.id)]))
        #await message.answer(str(data['b'+str(message.from_user.id)]))
    #await state.finish()
    await FSMSt1.next()
    await message.answer(s1_v[23], reply_markup=s1_a24k)


async def St1_24(message: types.Message, state: FSMContext):
    if message.text not in s1_a24:
        await message.answer("Пожалуйста, введите один из предложенных ответов", reply_markup=s1_a24k)
        return

    async with state.proxy() as data:
        if (message.text == s1_a24[0]):
            data['data'+str(message.from_user.id)][13] = "0"
        elif (message.text == s1_a24[1]):
            data['data'+str(message.from_user.id)][13] = "2"
        elif (message.text == s1_a24[2]):
            data['data'+str(message.from_user.id)][13] = "1"
        else:
            await message.answer('что-то не так')
        #await message.answer(str(data['data'+str(message.from_user.id)]))
        #await message.answer(str(data['b'+str(message.from_user.id)]))
    #await state.finish()
    await FSMSt1.next()
    await message.answer(s1_v[24], reply_markup=s1_a25k)

async def St1_25(message: types.Message, state: FSMContext):
    if message.text not in s1_a25:
        await message.answer("Пожалуйста, введите один из предложенных ответов", reply_markup=s1_a25k)
        return

    async with state.proxy() as data:
        if (message.text == s1_a25[0]):
            data['data'+str(message.from_user.id)][4] = "0"
        elif (message.text == s1_a25[1]):
            data['data'+str(message.from_user.id)][4] = "1"
        elif (message.text == s1_a25[2]):
            data['data'+str(message.from_user.id)][4] = "2"
        else:
            await message.answer('что-то не так')
        #await message.answer(str(data['data'+str(message.from_user.id)]))
        #await message.answer(str(data['b'+str(message.from_user.id)]))
    #await state.finish()
    await FSMSt1.next()
    await message.answer(s1_v[25], reply_markup=s1_a10k)

async def St1_26(message: types.Message, state: FSMContext):
    if message.text not in s1_a10:
        await message.answer("Пожалуйста, введите один из предложенных ответов", reply_markup=s1_a10k)
        return

    async with state.proxy() as data:
        if (message.text == s1_a10[0]):
            data['data'+str(message.from_user.id)][5] = "1"
        elif (message.text == s1_a10[1]):
            data['data'+str(message.from_user.id)][5] = "0"
        else:
            await message.answer('что-то не так')
        #await message.answer(str(data['data'+str(message.from_user.id)]))
        #await message.answer(str(data['b'+str(message.from_user.id)]))
    #await state.finish()
    await FSMSt1.next()
    await message.answer(s1_v[26], reply_markup=s1_a10k)


async def St1_27(message: types.Message, state: FSMContext):
    if message.text not in s1_a10:
        await message.answer("Пожалуйста, введите один из предложенных ответов", reply_markup=s1_a10k)
        return

    async with state.proxy() as data:
        if (message.text == s1_a10[0]):
            data['data'+str(message.from_user.id)][6] = "1"
        elif (message.text == s1_a10[1]):
            data['data'+str(message.from_user.id)][6] = "0"
        else:
            await message.answer('что-то не так')
        #await message.answer(str(data['data'+str(message.from_user.id)]))
        #await message.answer(str(data['b'+str(message.from_user.id)]))
    #await state.finish()
    await FSMSt1.next()
    await message.answer(s1_v[27], reply_markup=s1_a10k)


async def St1_28(message: types.Message, state: FSMContext):
    if message.text not in s1_a10:
        await message.answer("Пожалуйста, введите один из предложенных ответов", reply_markup=s1_a10k)
        return

    async with state.proxy() as data:
        if (message.text == s1_a10[0]):
            data['data'+str(message.from_user.id)][15] = "1"
        elif (message.text == s1_a10[1]):
            data['data'+str(message.from_user.id)][15] = "0"
        else:
            await message.answer('что-то не так')
        #await message.answer(str(data['data'+str(message.from_user.id)]))
        #await message.answer(str(data['b'+str(message.from_user.id)]))
    #await state.finish()
    await FSMSt1.next()
    await message.answer(s1_v[28], reply_markup=s1_a10k)


async def St1_29(message: types.Message, state: FSMContext):
    if message.text not in s1_a10:
        await message.answer("Пожалуйста, введите один из предложенных ответов", reply_markup=s1_a10k)
        return

    async with state.proxy() as data:
        if (message.text == s1_a10[0]):
            data['data'+str(message.from_user.id)][16] = "1"
        elif (message.text == s1_a10[1]):
            data['data'+str(message.from_user.id)][16] = "0"
        else:
            await message.answer('что-то не так')
        #await message.answer(str(data['data'+str(message.from_user.id)]))
        #await message.answer(str(data['b'+str(message.from_user.id)]))
    #await state.finish()
    await FSMSt1.next()
    await message.answer(s1_v[29], reply_markup=s1_a10k)


async def St1_30(message: types.Message, state: FSMContext):
    if message.text not in s1_a10:
        await message.answer("Пожалуйста, введите один из предложенных ответов", reply_markup=s1_a10k)
        return

    async with state.proxy() as data:
        if (message.text == s1_a10[0]):
            data['data'+str(message.from_user.id)][17] = "1"
        elif (message.text == s1_a10[1]):
            data['data'+str(message.from_user.id)][17] = "0"
        else:
            await message.answer('что-то не так')
        #await message.answer(str(data['data'+str(message.from_user.id)]))
        #await message.answer(str(data['b'+str(message.from_user.id)]))
    #await state.finish()
    await FSMSt1.next()
    await message.answer(s1_v[30], reply_markup=s1_a10k)

async def St1_31(message: types.Message, state: FSMContext):
    if message.text not in s1_a10:
        await message.answer("Пожалуйста, введите один из предложенных ответов", reply_markup=s1_a10k)
        return

    async with state.proxy() as data:
        if (message.text == s1_a10[0]):
            data['data'+str(message.from_user.id)][18] = "1"
        elif (message.text == s1_a10[1]):
            data['data'+str(message.from_user.id)][18] = "0"
        else:
            await message.answer('что-то не так')
        await message.answer(str(data['data'+str(message.from_user.id)]))
        await message.answer(str(data['b'+str(message.from_user.id)]))
        diag = CreateDiag(1, data['b'+str(message.from_user.id)], data['data'+str(message.from_user.id)])
        mylist = UseProgramNew(diag)
        await bot.send_message(message.from_user.id, str(mylist))

        mylist = mylist.replace('[', '')
        mylist = mylist.replace(']', '')
        print(mylist)

        ready = list(map(float, mylist.split(',')))
        if len(ready) == 7:
            temp = max(ready[0], ready[1], ready[2])
            ready.insert(3, temp)

        print(ready)
        await plots(message, ready)
    await state.finish()


def register_handlers_FSM(dp: Dispatcher):
    dp.register_message_handler(St1_Start, commands=['st1'], state=None)
    dp.register_message_handler(St1_Date, state=FSMSt1.date)
    dp.register_message_handler(St1_2, state=FSMSt1.age)
    dp.register_message_handler(St1_3, state=FSMSt1.gender)
    dp.register_message_handler(St1_4, state=FSMSt1.st1_v4)
    dp.register_message_handler(St1_5, state=FSMSt1.st1_v5)
    dp.register_message_handler(St1_6, state=FSMSt1.st1_v6)
    dp.register_message_handler(St1_7, state=FSMSt1.st1_v7)
    dp.register_message_handler(St1_8, state=FSMSt1.st1_v8)
    dp.register_message_handler(St1_9, state=FSMSt1.st1_v9)
    dp.register_message_handler(St1_10, state=FSMSt1.st1_v10)
    dp.register_message_handler(St1_11, state=FSMSt1.st1_v11)
    dp.register_message_handler(St1_12, state=FSMSt1.st1_v12)
    dp.register_message_handler(St1_13, state=FSMSt1.st1_v13)
    dp.register_message_handler(St1_14, state=FSMSt1.st1_v14)
    dp.register_message_handler(St1_15, state=FSMSt1.st1_v15)
    dp.register_message_handler(St1_16, state=FSMSt1.st1_v16)
    dp.register_message_handler(St1_17, state=FSMSt1.st1_v17)
    dp.register_message_handler(St1_18, state=FSMSt1.st1_v18)
    dp.register_message_handler(St1_19, state=FSMSt1.st1_v19)
    dp.register_message_handler(St1_20, state=FSMSt1.st1_v20)
    dp.register_message_handler(St1_21, state=FSMSt1.st1_v21)
    dp.register_message_handler(St1_22, state=FSMSt1.st1_v22)
    dp.register_message_handler(St1_23, state=FSMSt1.st1_v23)
    dp.register_message_handler(St1_24, state=FSMSt1.st1_v24)
    dp.register_message_handler(St1_25, state=FSMSt1.st1_v25)
    dp.register_message_handler(St1_26, state=FSMSt1.st1_v26)
    dp.register_message_handler(St1_27, state=FSMSt1.st1_v27)
    dp.register_message_handler(St1_28, state=FSMSt1.st1_v28)
    dp.register_message_handler(St1_29, state=FSMSt1.st1_v29)
    dp.register_message_handler(St1_30, state=FSMSt1.st1_v30)
    dp.register_message_handler(St1_31, state=FSMSt1.st1_v31)
