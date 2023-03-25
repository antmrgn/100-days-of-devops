# Привет. Напиши пожалуйста код python для телеграм бота, который запрашивает у пользователя номер телефона и четыре последние цифры карты. Сохраняет это в переменные и формирует запрос на адрес https://meal.gift-cards.ru/api/1/virtual-cards/"номер телефона"/"последние четыре цифры карты". Из ответа, который в формате JSON, извлекает данные баланса карты ['data']['balance']['availableAmount'] и возвращает пользователю в телеграм.

import requests
import telebot

bot = telebot.TeleBot("<BOT-TOKEN>")

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
    url = f"https://meal.gift-cards.ru/api/1/virtual-cards/{phone}/{card_number}"
#    headers = {
#        "Content-Type": "application/json",
#        "Accept": "application/json",
#        "Authorization": "Bearer <ACCESS_TOKEN>"
#    }
#    response = requests.get(url, headers=headers).json()
    response = requests.get(url).json()
 
    # Извлекаем данные баланса карты
    balance = response['data']['balance']['availableAmount']

    # Отправляем пользователю сообщение с балансом карты
    bot.send_message(message.chat.id, f"Баланс карты: {balance}")

# Запускаем бота
bot.polling()