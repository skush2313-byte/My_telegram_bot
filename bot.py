import telebot

# Yaha apna BotFather se mila token daalo
TOKEN = "8213860517:AAFH7MnJVS8PcWsDaWpvw8KLNIA6tu00_90"

bot = telebot.TeleBot(TOKEN)

# Jab user /start likhega to ye reply aayega
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello! 👋 Mai ek Telegram bot hoon.")

# Jo bhi user likhega, bot wahi reply karega
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

print("Bot chal gaya...")

bot.polling()
