import telebot
from config import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
👋 Hello! Welcome to the school bot.
Use the buttons or type a message to interact with me.
I can help you see your schedule, get info about the school, or just chat!\
""")

# Handle all other messages
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    # Simple sanitization: remove potentially dangerous characters
    safe_text = ''.join(c for c in message.text if c.isalnum() or c.isspace())
    bot.reply_to(message, safe_text if safe_text else "⚠️ Your message contained unsupported characters.")

try:
    bot.infinity_polling()
except Exception as e:
    print(f"An error occurred while polling: {e}")
