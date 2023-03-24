# вопрос
# Привет. Напиши пожалуйста код python для телеграм бота, который запрашивает у пользователя номер телефона и четыре последние цифры карты. Сохраняет это в переменные и формирует запрос к api https://meal.gift-cards.ru/api/1/virtual-cards/. Выполняет запрос к api, извлекает данные баланса карты ['data']['balance']['availableAmount'] и возвращает пользователю в телеграм.
#

import requests
import telebot

bot = telebot.TeleBot("<API_TOKEN>")

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет, введите номер телефона и четыре последние цифры карты (разделяйте пробелом)")

# Обработчик сообщения от пользователя
@bot.message_handler(func=lambda message: True)
def get_card_balance(message):
    # Разделяем номер телефона и четыре последние цифры карты
    phone, card_number = message.text.split()

    # Формируем запрос к API
    url = "https://meal.gift-cards.ru/api/1/virtual-cards/"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": "Bearer <ACCESS_TOKEN>"
    }
    data = {
        "card": {
            "last_pan": card_number
        }
    }
    response = requests.post(url, headers=headers, json=data).json()

    # Извлекаем данные баланса карты
    balance = response['data']['balance']['availableAmount']

    # Отправляем пользователю сообщение с балансом карты
    bot.send_message(message.chat.id, f"Баланс карты: {balance}")

# Запускаем бота
bot.polling()


# Пожалуйста, замените `<API_TOKEN>` и `<ACCESS_TOKEN>` на свои токены API и доступа соответственно.