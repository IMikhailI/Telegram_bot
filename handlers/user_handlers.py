from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext

from Telegram_bot.lexicon.lexicon import LEXICON
from Telegram_bot.keyboards.main_keyboard import main_keyboard  # главная клавиатура
from Telegram_bot.keyboards.speciality_keybord import speciality_keyboards  # клавиатура выбора специальности (функция)
from Telegram_bot.keyboards.doctor_keyboard import doctor_keyboard  # клавиатура выбора врача (функция)
from Telegram_bot.keyboards.time_keybord import time_keyboards
from Telegram_bot.FSM import St

# Инициализируем роутер уровня модуля
router: Router = Router()


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
        # await state.update_data(
        #     {
        #         'item1': item1
        #     }
        # )
        await message.answer(text=LEXICON['/doctor'], reply_markup=doctor_keyboard(item1))
        await state.set_state(St.step2)


# Состояние выбора времени
@router.message(St.step2)
async def cmd_time(message: Message, state: FSMContext):
    if message.text == "Отмена":
        await state.set_state()
        await message.answer("Принято", reply_markup=main_keyboard)
    else:
        item2 = message.text
        print("item2 - ", item2)
        await message.answer(f"Выберите любое время приёма\n{item2}", reply_markup=time_keyboards())
        await state.set_state(St.step3)


# Состояние авторизации
@router.message(St.step3)
async def cmd(message: Message, state: FSMContext):
    if message.text == "Отмена":
        await state.set_state()
        await message.answer("Принято", reply_markup=main_keyboard)
    else:
        item3 = message.text
        print("item3 - ", item3)
        await message.answer(f"Теперь давайте авторизуемся\n{item3}", reply_markup=None)
        await state.set_state(St.step4)


# Конечное состояние
@router.message(St.step4)
async def cmd(message: Message, state: FSMContext):
    if message.text == "Отмена":
        await state.set_state()
        await message.answer("Принято", reply_markup=main_keyboard)
    else:
        item4 = message.text
        print("item4 - ", item4)
        await message.answer(f"Подтвердите запись к врачу\n{item4}", reply_markup=None)
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
