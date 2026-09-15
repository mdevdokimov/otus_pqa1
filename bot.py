"""
приложение ждет от бота сообщений
ожидает Имя города
возвращает погоду в запрошенном городе
"""
import os

import requests
import telebot

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
VERSION = os.environ.get("APP_VERSION", "development")

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    """ответ на start или help. отправляем Велком сообщение."""
    welcome_text = (
        f"Привет! Отправь мне название города на английском, и я пришлю текущую погоду.\n\n"
        f"🤖 Версия бота: {VERSION}"
    )
    bot.reply_to(message, welcome_text)


@bot.message_handler(func=lambda message: True)
def get_weather(message):
    """забираем погоду и отдаем боту"""
    city = message.text
    url = f"https://wttr.in/{city}?format=j1&lang=ru"
    try:
        response = requests.get(url, timeout=5).json()
        current = response["current_condition"][0]
        temp = current["temp_C"]
        desc = (
            current["lang_ru"][0]["value"]
            if "lang_ru" in current
            else current["weatherDesc"][0]["value"]
        )
        humidity = current["humidity"]

        text = (
            f"🌤 Погода в {city.capitalize()}:\n"
            f"🌡 Температура: {temp}°C\n"
            f"📝 Статус: {desc}\n"
            f"💧 Влажность: {humidity}%\n"
        )
        bot.reply_to(message, text)
    except ValueError as e:
        print(f"Ошибка бота: {e}")
        bot.reply_to(
            message,
            "❌ Не удалось найти этот город.\
                  Попробуйте ввести название латиницей (например, Moscow).",
        )


if __name__ == "__main__":
    print("Telegram-бот успешно запущен...")
    bot.infinity_polling()
