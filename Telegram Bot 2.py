import telebot
import threading
from telebot import storage

bot = telebot.TeleBot("7830810346:AAERZ_auMqeoR8tRjHZL-tfmsAYEi-c6bU0")
state_storage = storage.StateMemoryStorage()

user_states = {}



@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот с системой напоминаний. Используй команду /remind чтобы установить напоминание.")


@bot.message_handler(commands=['remind'])
def F (message):
    chat_id = message.chat.id
    user_states[chat_id] = 'waiting_for_time'
    bot.send_message(chat_id, "Через сколько минут напомнить?")



@bot.message_handler(func=lambda message: True)
def T (message):
    chat_id = message.chat.id

    if chat_id in user_states and user_states[chat_id] == 'waiting_for_time':
        try:
            min = float(message.text)
            if min <= 0:
                bot.send_message(chat_id, "Пожалуйста, введите положительное число.")
                return

            sec = min * 60
            text = f"Напоминание сработало! Вы просили напомнить через {min} минут."

            # Создаем таймер
            timer = threading.Timer(sec, S, args=[chat_id, text])
            timer.start()

            bot.send_message(chat_id, f"Хорошо, напомню через {min} минут.")
            del user_states[chat_id]

        except ValueError:
            bot.send_message(chat_id, "Пожалуйста, введите число (например: 5 или 2.5).")


def S (chat_id, text):
    bot.send_message(chat_id, text)


if __name__ == '__main__':
    print("Бот запущен...")
    bot.infinity_polling()
