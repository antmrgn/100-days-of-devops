# взято из https://xakep.ru/2021/11/28/python-telegram-bots/
from urllib.request import urlopen
import telebot, json 
# Создаем экземпляр бота
bot = telebot.TeleBot('bot_key')
# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я на связи. Напиши мне что-нибудь )')
@bot.message_handler(commands=["balance"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Баланс на карте: ')
    url = "https://meal.gift-cards.ru/api/1/virtual-cards/+79270123456/0123"
    response = urlopen(url)
    data_json = json.loads(response.read())
    amount = data_json['data']['balance']['availableAmount']
    bot.send_message(m.chat.id, amount)
# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, 'Вы написали: ' + message.text)
# Запускаем бота
bot.polling(none_stop=True, interval=0)
