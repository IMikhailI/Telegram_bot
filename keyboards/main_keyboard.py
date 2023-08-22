from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

# Создаем объекты главных кнопок
button_1: KeyboardButton = KeyboardButton(text='Выбрать специальность врача')
button_2: KeyboardButton = KeyboardButton(text='Посмотреть мою запись')  # возможно не понадобятся
button_3: KeyboardButton = KeyboardButton(text='Отменить запись')  # возможно не понадобятся

# Создаем объект клавиатуры, добавляя в него кнопки
main_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
    keyboard=[[button_1, button_2, button_3]],
    resize_keyboard=True)
