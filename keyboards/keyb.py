from aiogram.types import ReplyKeyboardMarkup, KeyboardButton#, ReplyKeyboardRemove
from handlers.config import *
b1 = KeyboardButton('Начать исследование')
b2 = KeyboardButton('Справка')

st1 = KeyboardButton('/st1')
st2 = KeyboardButton('Стадия 2')
st3 = KeyboardButton('Стадия 3')
kb = ReplyKeyboardMarkup(resize_keyboard=True)
start_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

start_kb.add(st1)
#kb.add(st1)

s1_a3k = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
for name in s1_a3:
    s1_a3k.add(name)

s1_a6k = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
for name in s1_a6:
    s1_a6k.add(name)

s1_a7k = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
for name in s1_a7:
    s1_a7k.add(name)


s1_a8k = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
for name in s1_a8:
    s1_a8k.add(name)

s1_a9k = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
for name in s1_a9:
    s1_a9k.add(name)

s1_a10k = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
for name in s1_a10:
    s1_a10k.add(name)

s1_a18k = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
for name in s1_a18:
    s1_a18k.add(name)

s1_a19k = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
for name in s1_a19:
    s1_a19k.add(name)

s1_a20k = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
for name in s1_a20:
    s1_a20k.add(name)

s1_a21k = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
for name in s1_a21:
    s1_a21k.add(name)

s1_a22k = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
for name in s1_a22:
    s1_a22k.add(name)

s1_a23k = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
for name in s1_a23:
    s1_a23k.add(name)

s1_a24k = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
for name in s1_a24:
    s1_a24k.add(name)

s1_a25k = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
for name in s1_a25:
    s1_a25k.add(name)
