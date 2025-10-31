import telebot
from telebot import types
from logic import DBManager
from config import BOT_TOKEN

db = DBManager()
bot = telebot.TeleBot(BOT_TOKEN)

user_choices = {}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('📅 Просмотр Расписания', '🏫 О Школе', '❓ Помощь')
    bot.send_message(message.chat.id,
                     "👋 Привет! Добро пожаловать в нашего бота онлайн-школы.\n"
                     "Здесь вы можете просмотреть своё расписание, узнать информацию о школе или получить помощь.\n"
                     "Выберите опцию ниже 👇",
                     reply_markup=markup)

@bot.message_handler(func=lambda m: True)
def handle_buttons(message):
    if message.text == "📅 Просмотр Расписания":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        markup.row('9', '10', '11')
        bot.send_message(message.chat.id, "Пожалуйста, выберите свой класс:", reply_markup=markup)
        user_choices[message.chat.id] = {}

    elif message.text in ['9', '10', '11']:
        if message.chat.id in user_choices:
            user_choices[message.chat.id]['grade'] = int(message.text)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            markup.row('Понедельник', 'Вторник', 'Среда')
            markup.row('Четверг', 'Пятница')
            bot.send_message(message.chat.id, "Пожалуйста, выберите день:", reply_markup=markup)
        else:
            bot.send_message(message.chat.id, "⚠️ Сначала нажмите 📅 Просмотр Расписания.")

    elif message.text in ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница']:
        if message.chat.id in user_choices and 'grade' in user_choices[message.chat.id]:
            grade = user_choices[message.chat.id]['grade']
            day = message.text
            lesson_text = db.get_random_lesson(day, grade)
            bot.send_message(message.chat.id, lesson_text)
            user_choices.pop(message.chat.id)
        else:
            bot.send_message(message.chat.id, "⚠️ Сначала выберите класс.")

    elif message.text == "🏫 О Школе":
        bot.send_message(message.chat.id,
                         "🎓 О нашей школе:\n\n"
                         "Мы — онлайн-школа, предоставляющая качественное образование студентам со всего мира.\n"
                         "Обучение увлекательное, интерактивное и доступно из любой точки 🌍")

    elif message.text == "❓ Помощь":
        bot.send_message(message.chat.id,
                         "💬 Раздел помощи:\n\n"
                         "- Нажмите 📅 Просмотр Расписания, чтобы увидеть свои уроки.\n"
                         "- Нажмите 🏫 О Школе, чтобы узнать больше о школе.\n"
                         "- Введите /start в любой момент, чтобы вернуться в главное меню.\n"
                         "Если что-то не работает, попробуйте перезапустить чат или обратитесь к учителю.")

    else:
        bot.send_message(message.chat.id, "⚠️ Ой! Пожалуйста, используйте кнопки или введите /start, чтобы увидеть меню снова.")

bot.infinity_polling()
