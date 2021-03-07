import telebot

bot = telebot.TeleBot("1616148015:AAGFOawl52NZ_imt3YqGGJAiYe94wYf7vR4")

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Приветушки. Меня зовут Вальдемар. Буду хэлповать тебе время от времени, чем смогу. Что я могу? Вот список команд:")

@bot.message_handler(commands=['reminders'])
def send_welcome(message):
	bot.reply_to(message, "Годно, напоминания запущены.")

@bot.message_handler(commands=['memes'])
def send_welcome(message):
	bot.reply_to(message, "Лови мем!")

@bot.message_handler(commands=['food'])
def send_welcome(message):
	bot.reply_to(message, "Сейчас покажу еду поблизости:")

@bot.message_handler(commands=['horoscope'])
def send_welcome(message):
	bot.reply_to(message, "Давай посмотрим что звёзды говорят сегодня")

@bot.message_handler(commands=['help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()
