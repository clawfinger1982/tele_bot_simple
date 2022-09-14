from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb1 = ReplyKeyboardMarkup(resize_keyboard=True)
kb2 = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('/start')
b2 = KeyboardButton('/help')
b3 = KeyboardButton('/description')
b4 = KeyboardButton('/photo')
b5 = KeyboardButton('/location')
b6 = KeyboardButton('/give')
b7 = KeyboardButton('/rand_photo')

kb.add(b2)
kb1.add(b1).insert(b2).add(b3).insert(b4).add(b5).insert(b6)
kb2.add(b7)

ikb = InlineKeyboardMarkup(row_width=2)
ib1 = InlineKeyboardButton(text='Рандомная_фотка',
                           callback_data='rand_photo')
ib2 = InlineKeyboardButton(text='лайк',
                           callback_data='like')
ib3 = InlineKeyboardButton(text='дизлайк',
                           callback_data='dislike')
ib4 = InlineKeyboardButton(text='главное меню',
                           callback_data='main')
ikb.add(ib2, ib3).insert(ib1).insert(ib4)
