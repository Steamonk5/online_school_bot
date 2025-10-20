import telebot
from config import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('📅 View Schedule', '🏫 About School', '❓ Help')
    bot.reply_to(message, """
👋 Hello! Welcome to our Online School Bot.
Here you can check your lesson schedule, learn more about the school, or get help.
Choose an option below 👇
""", reply_markup=markup)


# Handle all other messages
@bot.message_handler(func=lambda message: True)
def handle_buttons(message):
    if message.text == "📅 View Schedule":
        bot.send_message(message.chat.id,
"""🧮 Monday: Math - 10:00 AM
🧬 Tuesday: Biology - 11:00 AM
💻 Wednesday: Computer Science - 12:00 PM
📖 Thursday: Literature - 10:30 AM
🌍 Friday: Geography - 11:00 AM""")
        

    elif message.text == "🏫 About School":
        bot.send_message(message.chat.id, """🎓 About Our School:

We are an online school dedicated to providing high-quality education to students worldwide.  
Our goal is to make learning fun, interactive, and accessible from anywhere 🌍  

You can always check your schedule or get help using this bot!""")
        

    elif message.text == "❓ Help":
        bot.send_message(message.chat.id, """💬 Help Section:

                         
Here’s how to use this bot:
- Press 📅 View Schedule to see your weekly lessons.
- Press 🏫 About School to learn more about the school.
- Press /start anytime to return to the main menu.

If something doesn’t work, try restarting the chat or contact your teacher.""")


    else:
        bot.send_message(message.chat.id, "⚠️ Oops! Please use the buttons or type /start to see the menu again.")

bot.infinity_polling()