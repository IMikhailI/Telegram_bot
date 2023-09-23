from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
import sqlite3 as sq
# from Telegram_bot.database.base import script_path

import os
from Telegram_bot.database.path import get_script_dir


# def get_script_dir():
#     abs_path = path.abspath(__file__)  # полный путь к файлу скрипта
#     return path.dirname(abs_path)


def doctor_keyboard(buttons: str):

    conn = sq.connect(os.path.join(get_script_dir(), 'test_base.db'))
    cur = conn.cursor()

    cur.execute(f"""SELECT sur_name||" "||first_name||" "||patr_name
                    FROM WORKER w
                    INNER JOIN SPECIALITY s
                    ON w.speciality_id = s.id
                    WHERE s.name = '{buttons}' """)

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
    doctor_keyboards: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True)

    return doctor_keyboards


# doctor_keyboard("Психолог")
