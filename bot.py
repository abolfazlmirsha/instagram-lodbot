import os
import telebot

TOKEN = os.environ.get("8674509588:AAEF7_dFS7rGCIuQcBYHs9J4RVqKpk1clU8")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(
        message,
        "سلام 👋\n"
        "به instagram_lodbot خوش آمدید.\n\n"
        "ربات آماده دریافت پیام شماست."
    )

@bot.message_handler(func=lambda message: True)
def reply(message):
    bot.reply_to(
        message,
        "پیام شما دریافت شد ✅"
    )

print("Bot Started...")

bot.infinity_polling()
