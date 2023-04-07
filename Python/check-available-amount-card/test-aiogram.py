import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from config_reader import config
import requests

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=config.bot_token.get_secret_value())
# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Введи номер телефона в формате +7XXXXXXXXXX и через пробел четыре последние цифры карты")

@dp.message(Command("help"))
async def process_help_command(message: types.Message):
    await message.answer("Бот поможет тебе узнать баланс карты SUP. Напиши /start чтобы начать")

@dp.message()
async def echo_message(message: types.Message):
#    await message.answer("message")
#    await message.answer(message.text)
                         
    phone, card_number = message.text.split()

    url = f"https://meal.gift-cards.ru/api/1/virtual-cards/{phone}/{card_number}"

    response = requests.get(url).json()
 
    # Извлекаем данные баланса карты
    balance = response['data']['balance']['availableAmount']

    # Отправляем пользователю сообщение с балансом карты
    await message.answer("Баланс карты:") 
    await message.answer(balance)   



# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())