from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
import sqlite3 as sq

import os
from Telegram_bot.database.path import get_script_dir


# def get_script_dir():
#     abs_path = path.abspath(__file__)  # полный путь к файлу скрипта
#     return path.dirname(abs_path)


def speciality_keyboards():

    conn = sq.connect(os.path.join(get_script_dir(), 'test_base.db'))
    cur = conn.cursor()

    cur.execute('SELECT name FROM SPECIALITY')

    users = cur.fetchall()

    info = []
    for el in users:
        info += el[0::]

    cur.close()
    conn.close()

    info.append("Отмена")

    # Заполняем список списками с кнопками
    keyboard: list[list[KeyboardButton]] = [
        [KeyboardButton(text=i)] for i in info]

    # Создаем объект клавиатуры, добавляя в него список списков с кнопками
    speciality_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True)

    return speciality_keyboard
