from aiogram import Bot, Dispatcher, executor,types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
import datetime

api = "8100419843:AAHoQivMyXedI3BxgqlQH2lKKnY_aiXx2SM"
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


file_name = "res.txt"
start_time = datetime.datetime.now()
rost = "Введи свой рост (в сантиметрах):"

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands=["start"], state='*')
async def start_message(message: types.Message):
    await message.answer("Привет! Я - бот, помогающий твоему здоровью!",
                         reply_markup = kb)
    # await bot.send_message(message.from_user.id, message.from_user.first_name)
    # print(message.from_user.first_name)
    global file_name1
    file_name1 = f"res.txt_{message.from_user.username}"
    with open(file_name, "a", encoding='utf-8') as file:
        file.writelines(f"Имя: {str(message.from_user.username)}, Время: {start_time}\n")

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
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age = message.text)
    data = await state.get_data()
    await message.answer(rost)
    await UserState.growth.set()
    async with state.proxy() as data:
        data['text'] = message.text
        user_message = data['text']
    global file_name1
    with open(file_name1, "a", encoding='utf-8') as file:
        file.writelines(f"{str(message.from_user.username)} Возраст: {str(user_message)}\n")

@dp.message_handler(state = UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=message.text)
    data = await state.get_data()
    await message.answer("Введи свой вес (в кг):")
    await UserState.weight.set()
    async with state.proxy() as data:
        data['text'] = message.text
        user_message = data['text']
    global file_name1
    with open(file_name1, "a", encoding='utf-8') as file:
        file.writelines(f"{str(message.from_user.username)} Рост: {str(user_message)}\n")

@dp.message_handler(state = UserState.weight)
async def set_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    await UserState.weight.set()
    calories = (10 * int(data["weight"]) + 6.25 * int(data["growth"])
                - 5 * int(data["age"]) - 161)
    await message.answer(f"Твоя норма калорий - {calories} ккал")
    async with state.proxy() as data:
        data['text'] = message.text
        user_message = data['text']
    global file_name1
    with open(file_name1, "a", encoding='utf-8') as file:
        file.writelines(f"{str(message.from_user.username)} Вес: {str(user_message)}\n")
    await state.finish()

@dp.message_handler()
async def all_message(message):
    await message.answer("Введите команду /start, чтобы начать общение")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
