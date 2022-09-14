import random
import aiogram.utils.exceptions
from aiogram.dispatcher.filters import Text
from aiogram.utils.callback_data import CallbackData
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove
from config import TOKEN_API
from keyboard_bot_project import kb, kb1, kb2, ikb

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

count = 0
count1 = 0

async def on_startup(_):
    print('Бот запущен!')


# + Реализовать бота таким образом, что бы все обновления пропускались в оффлайн режиме
# + При включении сервера в консоли должна отображаться инфа по этому поводу.

# + Реализовать бот в двух файлах. В первом находится клава пользователя, во втором
# + весь остальной функционал.

# + У бота должны быть реализованы команды /start, /help, /description,
# + должно присутствовать главное меню с клавиатурой, где пользователь может
# + использовать каждую из этих команд.

# + должно быть реализовано меню, где пользователь может получить одну рандомную
# + фотографию из заранее заготовленного списка, оттуда должен быть переход на главное меню.

# + Под фотографией должно быть описание данной фотографии, при этом должна присутствовать
# + инлайн клавиатура.

# + При нажатии должен генерироваться callback запрос, ему должна быть сопоставлена
# + обработка со стороны сервера.

#  + Инлайн клава должна состоять из 3х кнопок:
# + 1 - Следующая рандомная фотография
# + 2 - Лайк
# + 3 - Дизлайк
# + Если пользователь нажмет лайк/дизлайк, должен появиться соответствующий label
# + Обработайте как-либо повторное нажатие на кнопку при одной и той же фотографии:

# + Реализовать возможность боту отправлять вам стикеры, эмодзи и рандомное местоположение.

# @dp.message_handler(Text(equals=["rand_photo", "photo"]))
# async def open_kb_photo(messasge: types.Message):
#     await message.answer(#text='random photo',
#                          #caption=photos[rand_photo],
#                          reply_markup=ReplyKeyboardRemove())

@dp.message_handler(commands=['help'])
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="""
                           <b>/help</b> - <em> список команд </em>
                           <b>/start</b> - <em> начало работы </em>
                           <b>/description</b> - <em> описание </em>
                           <b>/photo</b> - <em> отправка фото </em>
                           <b>/location</b> - <em> отправка случайной локации </em>
                           <b>/give</b> - <em> отправка случайной гифки/эмодзи </em>""",
                           parse_mode='HTML',
                           reply_markup=kb1)
    await message.delete()

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Welcome to our bot! \n Push the button.',
                           reply_markup=kb)
    await message.delete()

@dp.message_handler(commands=['give'])
async def send_stick(message: types.Message):
    stick = (
        'CAACAgIAAxkBAAEFh6li9NEdMzkm5FGniKnCjRyLODlW4AACRhYAApVPyUt1xp2x3W7f3CkE',
        'CAACAgIAAxkBAAEFxS5jF0479vJsTHOuiTYkonTqSNAxDgACVAADFSsAAkdshxv4c9QTKQQ',
        'CAACAgIAAxkBAAEFxTBjF05c0PRKoATOT6ear2RFemCngwACCgADM_toHSSwQ0gdbp2OKQQ',
        'CAACAgIAAxkBAAEFxTJjF056a29ZcgABOEI9FZxODqNEHzQAAgIYAAJy3MBLeek8uL7FmAwpBA',
        'CAACAgEAAxkBAAEFxTZjF0656jUy_iCCtPTul-CJjM4pvAACWgoAAr-MkAQSfxie_QwxDCkE',
        'CAACAgIAAxkBAAEFxThjF07ziE34qJrfKst8EN_UbGK_PAACKgEAAv5QNQAB8fZx0WBqsGYpBA'
    )
    stick1 = stick[random.randint(0, 5)]
    await bot.send_sticker(message.from_user.id,
                           sticker=stick1,
                           reply_markup=kb)
    await message.delete()


@dp.message_handler(commands=['location'])
async def send_lock(message: types.Message):
    await bot.send_location(chat_id=message.from_user.id,
                            latitude=random.randint(20, 60),
                            longitude=random.randint(20, 90),
                            reply_markup=kb)
    await message.delete()

@dp.message_handler(commands=['description'])
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Бот отправляет рандомные фотки, даёт возможность лайкать их, и не только',
                           parse_mode='HTML',
                           reply_markup=kb)
    await message.delete()

@dp.message_handler(commands=['photo'])
async def ph_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Push the button for get random photo',
                           parse_mode='HTML',
                           reply_markup=kb2)
    await message.delete()

@dp.message_handler(commands=['rand_photo'])
async def photo_command(message: types.Message):
    global p
    p = (
        'https://klike.net/uploads/posts/2019-07/1564314166_13.jpg',
        'https://klike.net/uploads/posts/2019-07/1564314102_14.jpg',
        'https://klike.net/uploads/posts/2019-07/1564314134_15.jpg',
        'https://klike.net/uploads/posts/2018-10/1539499418_5.jpg'
    )
    d = p[random.randint(0, 3)]
    await bot.send_photo(message.from_user.id,
                         photo=d,
                         caption='Do you like this photo?',
                         reply_markup=ikb)
    await message.delete()

@dp.callback_query_handler()
async def vote_callback(callback: types.CallbackQuery):
    global d
    global count
    global count1
    if callback.data == 'like':
        if count == 0:
            await callback.answer(text='You like it!)))')
            count += 1
        else:
            await callback.answer(text='Too many requests.')
    elif callback.data == 'dislike':
        if count1 == 0:
            await callback.answer(text='You dislike it...((')
            count1 += 1
        else:
            await callback.answer(text='Too many requests.')
    elif callback.data == 'main':
            await callback.message.answer(text='Welcome to main menu',
                                          reply_markup=kb1)
            await callback.answer()
    elif callback.data == 'rand_photo':
        rand_photo = p[random.randint(0, 3)]
        await callback.answer(text='New photo')
        await callback.message.edit_media(types.InputMedia(media=rand_photo,
                                                       type='photo',
                                                       caption='Do you like this photo?'),
                                                       reply_markup=ikb)
        count = 0
        count1 = 0
        await callback.answer()


@dp.message_handler()
async def emoji_reply(message: types.Message):
    await message.reply(message.text)


if __name__ == "__main__":
    executor.start_polling(dispatcher=dp,
                           on_startup=on_startup,
                           skip_updates=True)
