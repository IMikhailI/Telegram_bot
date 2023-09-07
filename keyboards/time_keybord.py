from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def time_keyboards():
    info = ["время 1", "время 2", "время 3", "время 4", "время 5", "время 6", "Отмена"]

    # Заполняем список списками с кнопками
    keyboard: list[list[KeyboardButton]] = [
        [KeyboardButton(text=i)] for i in info]

    # Создаем объект клавиатуры, добавляя в него список списков с кнопками
    speciality_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True)

    return speciality_keyboard
