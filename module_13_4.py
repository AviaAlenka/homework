from aiogram import Bot, Dispatcher, executor,types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
import asyncio

api = ""
bot = Bot(token = api)
dp = Dispatcher(bot, storage = MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands=["start"])
async def start_message(message):
    await message.answer("Привет! Я - бот, помогающий твоему здоровью!\n"
                         "Если хочешь посчитать норму калорий, введи 'Calories'")

@dp.message_handler(text="Calories")
async def set_age(message):
    await message.answer("Введи свой возраст:")
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
