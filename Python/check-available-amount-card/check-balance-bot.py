# подключаем необходимые модули
import asyncio
import logging
import requests
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
# конфиг (токен бота) храним в отдельном файле
from config_reader import config


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

# Хэндлер на команду /help
@dp.message(Command("help"))
async def process_help_command(message: types.Message):
    await message.answer("Бот поможет тебе узнать баланс карты SUP. Напиши /start чтобы начать")

# Хэндлер на любое сообщение
@dp.message()
async def echo_message(message: types.Message):
    # проверяем сообщение на соответствие условиям
    if "+7" in message.text and len(message.text) == 17 and " " in message.text:
        # разделяем сообщение на номер телефона и номер карты
        phone, card_number = message.text.split()

        url = f"https://meal.gift-cards.ru/api/1/virtual-cards/{phone}/{card_number}"

        # делаем запрос к страничке с данными
        response = requests.get(url).json()
        # излекаем статус ответа со страницы
        status = response['status']
        if status == "OK":
            # Извлекаем данные баланса карты
            balance = response['data']['balance']['availableAmount']

            # Отправляем пользователю сообщение с балансом карты
            await message.answer("Баланс карты:") 
            await message.answer(balance)
        else:
            # отправляем пользователю сообщению о неудачном запросе баланса. И выводи поулченный статус
            await message.answer("Не удалось получить информацию. Проверьте правильность ввода номера и карты")
            await message.answer(status)
    else:
        # сообщение в случае неверного формата ввода
        await message.answer("Неверный ввод. Повторите") 


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())