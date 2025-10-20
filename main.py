import telebot
from config import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)

# Handle '/start' and '/help'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('📅 View Schedule', '🏫 About School', '❓ Help')
    bot.reply_to(message, """
👋 Привет! Добро пожаловать в наш бот онлайн-школы.
Здесь вы можете просматривать своё расписание, узнавать информацию о школе или получать помощь.
                 
Выберите опцию ниже 👇
""", reply_markup=markup)


# Handle all other messages
@bot.message_handler(func=lambda message: True)
def handle_buttons(message):
    if message.text == "📅 View Schedule":
        bot.send_message(message.chat.id,"""📅 Ваше расписание:

🧮 Понедельник: Математика - 10:00
🧬 Вторник: Биология - 11:00
💻 Среда: Информатика - 12:00
📖 Четверг: Литература - 10:30
🌍 Пятница: География - 11:00""")
        

    elif message.text == "🏫 About School":
        bot.send_message(message.chat.id, """🎓 О нашей школе:

Мы — онлайн-школа, предоставляющая качественное образование студентам со всего мира.  
Наша цель — сделать обучение увлекательным, интерактивным и доступным из любой точки 🌍  

Вы всегда можете проверить своё расписание или получить помощь через этого бота!""")
        

    elif message.text == "❓ Help":
        bot.send_message(message.chat.id, """💬 Раздел помощи:

Как пользоваться ботом:
- Нажмите 📅 View Schedule, чтобы увидеть своё расписание.
- Нажмите 🏫 About School, чтобы узнать информацию о школе.
- Введите /start в любой момент, чтобы вернуться в главное меню.

Если что-то не работает, попробуйте перезапустить чат или обратитесь к своему учителю.""")
        

    else:
        bot.send_message(message.chat.id, "⚠️ Ой! Пожалуйста, используйте кнопки или введите /start, чтобы увидеть меню снова.")

bot.infinity_polling()