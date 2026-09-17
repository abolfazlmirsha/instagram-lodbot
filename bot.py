import os

TOKEN = os.environ.get("BOT_TOKEN")

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
