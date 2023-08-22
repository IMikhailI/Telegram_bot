from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
import sqlite3 as sq


def speciality_keyboard():
    pass
    #  Пример
    # conn = sq.connect('test_database.db')
    # cur = conn.cursor()
    #
    # cur.execute("""SELECT DISTINCT s.Speciality FROM Speciality s""")
    #
    # users = cur.fetchall()
    #
    # info = []
    # for el in users:
    #     info += el[0::]
    #
    # cur.close()
    # conn.close()
    #
    # info.append("Назад")
    #
    # # Заполняем список списками с кнопками
    # keyboard: list[list[KeyboardButton]] = [
    #     [KeyboardButton(text=i)] for i in info]
    #
    # # Создаем объект клавиатуры, добавляя в него список списков с кнопками
    # speciality_keyboards: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
    #     keyboard=keyboard,
    #     resize_keyboard=True)
    #
    # return speciality_keyboards


# # ВАРИАНТ 2 - СЪЕДАЕТ КНОПКИ.
# buttons: list[KeyboardButton] = []
# keyboard: list[list[KeyboardButton]] = []
#
# # Заполняем список списками с кнопками
# q = 0
# for i in info:
#     q += 1
#     buttons.append(KeyboardButton(text=i))
#     if q == 2:
#         keyboard.append(buttons)
#         buttons = []
#         q = 0
#
# # Создаем объект клавиатуры, добавляя в него список списков с кнопками
# speciality_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
#                                         keyboard=keyboard,
#                                         resize_keyboard=True)
