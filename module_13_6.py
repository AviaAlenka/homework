from aiogram import Bot, Dispatcher, executor,types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

api = ""
bot = Bot(token = api)
dp = Dispatcher(bot, storage = MemoryStorage())
kb = ReplyKeyboardMarkup(resize_keyboard=True, input_field_placeholder =
                         "Чтобы узнать свою норму калорий, нажми 'Рассчитать'")
button = KeyboardButton(text = "Рассчитать")
button2 = KeyboardButton(text = "Информация")
kb.add(button)
kb.insert(button2)

ikb = InlineKeyboardMarkup()

ibutton = InlineKeyboardButton(text = 'Рассчитать норму калорий',
                               callback_data = 'calories')
ibutton2 = InlineKeyboardButton(text = 'Формулы расчёта' ,
                               callback_data = 'formulas')
ikb.add(ibutton)
ikb.insert(ibutton2)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands=["start"])
async def start_message(message):
    await message.answer("Привет! Я - бот, помогающий твоему здоровью!",
                         reply_markup = kb)

@dp.message_handler(text="Рассчитать")
async def main_menu(message):

    await message.answer('Выберите опцию:', reply_markup = ikb)

@dp.callback_query_handler(text = 'formulas')
async def get_formulas(call):
    await call.message.answer("10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161")


@dp.callback_query_handler(text = "calories")
async def set_age(call):
    await call.message.answer("Введи свой возраст:", reply_markup = types.ReplyKeyboardRemove())
    await UserState.age.set()

@dp.message_handler(state = UserState.age)
async def set_growth(message, state):
    await state.update_data(age = message.text)
    data = await state.get_data()
    await message.answer("Введи свой рост (в сантиметрах):")
    await UserState.growth.set()

@dp.message_handler(state = UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    data = await state.get_data()
    await message.answer("Введи свой вес (в кг):")
    await UserState.weight.set()

@dp.message_handler(state = UserState.weight)
async def set_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    await UserState.weight.set()
    calories = (10 * int(data["weight"]) + 6.25 * int(data["growth"])
                - 5 * int(data["age"]) - 161)
    await message.answer(f"Твоя норма калорий - {calories} ккал")
    await state.finish()

@dp.message_handler()
async def all_message(message):
    await message.answer("Введите команду /start, чтобы начать общение")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)