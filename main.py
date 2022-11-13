from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
import emoji

from config import TOKEN

bot = Bot(TOKEN)
dp = Dispatcher(bot)

# API_URL_1 = 'https://7015.deeppavlov.ai/model'  # negative/ positive / neutral
# API_URL_2 = 'https://7012.deeppavlov.ai/model'  # wiki


async def on_startup(_):
    print('bot online')


@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    b1 = KeyboardButton('Cat')
    b2 = KeyboardButton('Dog')

    kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

    kb_client.insert(b1).insert(b2)
    await message.answer("Кого показать?", reply_markup=kb_client)


@dp.message_handler(commands=['Cat'])
async def command_cat(message: types.Message):
    print('cat')
    await message.answer(emoji.emojize("Это кот! :cat:"))


@dp.message_handler(commands=['/Dog'])
async def command_neg_pos(message: types.Message):
    await message.answer(emoji.emojize("Это собака! :dog:"))


@dp.message_handler() # декоратор     в пустой хендлер попадает то, что нигде не было раньше, его держим внизу
async def echo_send(message : types.Message):
    if message.text == 'Cat':
        await message.answer(emoji.emojize("Это кот! :cat:"))
    if message.text == 'Привет':
        await message.answer('И тебе привет!')
    if message.text == 'Dog':
        await message.answer(emoji.emojize("Это собака! :dog:"))    
    await message.answer(message.text)
    # await message.reply(message.text)
    # await bot.send_message(message.from_user.id, message.text)# в личку


executor.start_polling(dp, skip_updates=True, on_startup=on_startup) # чтобы в бот не приходили сообщения, отправленные пока он не работал
