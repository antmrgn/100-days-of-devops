# взято из https://xakep.ru/2021/11/28/python-telegram-bots/
from urllib.request import urlopen
import telebot, json 
from telebot import types
# Создаем экземпляр бота
bot = telebot.TeleBot('bot_key')
# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
#    bot.send_message(m.chat.id, 'Выбери кнопку )')
        # Запрашиваем номер телефона и 4 последние цифры карты
#        msg = random.choice(first) + ' ' + random.choice(second) + ' ' + random.choice(second_add) + ' ' + random.choice(third)
        # Отправляем результат в Телеграм
    bot.send_message(m.chat.id, "Введите номер телефона в формате +7900123456")
    phone = str(m)
    bot.send_message(m.chat.id, "Введите последние четыре цифры вашей карты")
    card = str(m)
    bot.send_message(m.chat.id, "Вы ввели номер телефона: " + phone + ". Последние четыре цифры карты: " + card)

    # Готовим кнопки
    keyboard = types.InlineKeyboardMarkup()
    key_balance = types.InlineKeyboardButton(text='Запросить баланс', callback_data='balance')
    keyboard.add(key_balance)
    key_last_operation = types.InlineKeyboardButton(text='Запросить последнюю операцию', callback_data='last_operaion')
    keyboard.add(key_last_operation)
    key_5_last_operations = types.InlineKeyboardButton(text='Запросить 5 последних операций', callback_data='last_5_operaions')
    keyboard.add(key_5_last_operations)
    bot.send_message(m.chat.id, text='Выбери действие', reply_markup=keyboard)
@bot.message_handler(commands=["balance"])
def balance(m, res=False):
    bot.send_message(m.chat.id, 'Баланс на карте: ')
    url = "https://meal.gift-cards.ru/api/1/virtual-cards/+79270123456/1234"
    response = urlopen(url)
    data_json = json.loads(response.read())
    amount = data_json['data']['balance']['availableAmount']
    bot.send_message(m.chat.id, amount)
# Обработчик нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "balance": 
        # Запрашиваем номер телефона и 4 последние цифры карты
#        msg = random.choice(first) + ' ' + random.choice(second) + ' ' + random.choice(second_add) + ' ' + random.choice(third)
        # Отправляем результат в Телеграм
        bot.send_message(call.message.chat.id, "Введите номер телефона в формате +7900123456")
# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, 'Вы написали: ' + message.text)
# Запускаем бота
bot.polling(none_stop=True, interval=0)
