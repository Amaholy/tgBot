# main.py

import telebot
from telebot import types
from telebot import apihelper
import config
import handlers

# --- СОСТОЯНИЯ ПОЛЬЗОВАТЕЛЕЙ ---

user_authenticated = {}
user_city = {}


# --- ИНИЦИАЛИЗАЦИЯ ---
# Прокси только если задан PROXY_URL в .env (на сервере).
# Для локального теста строку PROXY_URL не указывайте или закомментируйте.
if config.PROXY_URL:
    apihelper.proxy = {'https': config.PROXY_URL}
bot = telebot.TeleBot(config.BOT_TOKEN)


# --- РЕГИСТРАЦИЯ ОБРАБОТЧИКОВ СООБЩЕНИЙ ---

@bot.message_handler(commands=['start'])
def handle_start(message: types.Message):
    handlers.send_welcome(bot, message, user_authenticated, user_city)

@bot.message_handler(commands=['help'])
def handle_help(message: types.Message):
    handlers.send_help(bot, message)

@bot.message_handler(commands=['myid'])
def handle_myid(message: types.Message):
    handlers.send_myid(bot, message)

@bot.message_handler(commands=['stop'])
def handle_stop(message: types.Message):
    handlers.send_goodbye(bot, message, user_authenticated, user_city)

# Обработчик ввода кода доступа (сработает, только если пользователь не аутентифицирован)
@bot.message_handler(func=lambda message: not user_authenticated.get(message.from_user.id, False) and message.text)
def handle_code(message: types.Message):
    handlers.handle_access_code(bot, message, user_authenticated, user_city)

# Обработчик сообщений, которые не являются командами, но при этом пользователь уже аутентифицирован. 
@bot.message_handler(func=lambda message: user_authenticated.get(message.from_user.id, False))
def handle_authenticated_text(message: types.Message):
    # Пока ничего не делаем с текстовыми сообщениями от аутентифицированных пользователей
    pass


# --- РЕГИСТРАЦИЯ ОБРАБОТЧИКОВ INLINE-КНОПОК ---

@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call: types.CallbackQuery):
    handlers.callback_handler(bot, call, user_authenticated, user_city)


# --- ЗАПУСК БОТА ---
if __name__ == '__main__':
    print("Бот V.E.R.A. запущен...")
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(f"Произошла ошибка при запуске бота: {e}")
