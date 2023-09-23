from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
import sqlite3 as sq

import os

from Telegram_bot.lexicon.lexicon import LEXICON
from Telegram_bot.keyboards.main_keyboard import main_keyboard  # главная клавиатура
from Telegram_bot.keyboards.speciality_keybord import speciality_keyboards  # клавиатура выбора специальности (функция)
from Telegram_bot.keyboards.doctor_keyboard import doctor_keyboard  # клавиатура выбора врача (функция)
from Telegram_bot.keyboards.time_keybord import time_keyboards
from Telegram_bot.FSM import St

from Telegram_bot.database.path import get_script_dir

# Инициализируем роутер уровня модуля
router: Router = Router()

sa = {}


# Срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON['/start'], reply_markup=main_keyboard)


# Срабатывает на команду /speciality или кнопку меню - выбор специальности врача
@router.message(Command(commands='speciality'))
@router.message(F.text == "Выбрать специальность врача")
@router.message(St.step0)
async def cmd_speciality(message: Message, state: FSMContext):
    await message.answer(text=LEXICON['/speciality'], reply_markup=speciality_keyboards())
    # Устанавливаем пользователю состояние "step2"
    await state.set_state(St.step1)  # !!!пропускает команду Назад!!!


# Состояние выбора врача
@router.message(St.step1)
async def cmd_doctor(message: Message, state: FSMContext):
    if message.text == "Отмена":
        await state.set_state()
        await message.answer("Принято", reply_markup=main_keyboard)

    else:
        item1 = message.text
        print("item1 - ", item1)
        await message.answer(text=LEXICON['/doctor'], reply_markup=doctor_keyboard(item1))
        await state.set_state(St.step2)


# Состояние выбора времени
@router.message(St.step2)
async def cmd_doc(message: Message, state: FSMContext):
    if message.text == "Отмена":
        await state.set_state()
        await message.answer("Принято", reply_markup=main_keyboard)
    else:
        doc = message.text
        sa['doc'] = doc
        print("item2 - ", doc)
        await message.answer('⌛ Выберите любое время приёма из предложенного списка.\n\n❗ Если кнопок со временем нет попробуйте записаться попозже.', reply_markup=time_keyboards(doc))
        await state.set_state(St.step3)

print(sa)


# Состояние авторизации
@router.message(St.step3)
async def cmd_time(message: Message, state: FSMContext):
    if message.text == "Отмена":
        await state.set_state()
        await message.answer("Принято", reply_markup=main_keyboard)
    else:
        time = message.text
        sa['time'] = time
        print("item3 - ", time)
        await message.answer("Теперь напишите своё ФИО и номер телефона.")
        await state.set_state(St.step4)


# Конечное состояние
@router.message(St.step4)
async def cmd_fio(message: Message, state: FSMContext):
    fio = message.text
    print("item4 - ", fio)

    conn = sq.connect(os.path.join(get_script_dir(), 'test_base.db'))
    cur = conn.cursor()

    cur.execute(f"""UPDATE EVENT 
                        SET client_data = '{fio}'
                        WHERE worker_id IN (SELECT id FROM WORKER WHERE sur_name||" "||first_name||" "||patr_name = '{sa['doc']}') AND start_date = '{sa['time']}'""")

    conn.commit()
    cur.close()
    conn.close()

    await message.answer("Запись  к врачу создана", reply_markup=main_keyboard)
    await state.set_state()


# Срабатывает на сообщения пользователя
@router.message()
async def send_answer(message: Message):
    if message.text == "Посмотреть мою запись":
        await message.answer("Смотрите")
    elif message.text == "Отменить запись":
        await message.answer("Отменяйте")
    else:
        await message.answer(text=LEXICON['other_answer'])
