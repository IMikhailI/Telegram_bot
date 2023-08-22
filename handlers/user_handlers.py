from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext

from Telegram_bot.lexicon.lexicon import LEXICON
from Telegram_bot.keyboards.main_keyboard import main_keyboard  # главная клавиатура
from Telegram_bot.keyboards.speciality_keybord import speciality_keyboard  # клавиатура выбора специальности (функция)
from Telegram_bot.keyboards.doctor_keyboard import doctor_keyboard  # клавиатура выбора врача (функция)
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
async def cmd_speciality(message: Message, state: FSMContext):
    await message.answer(text=LEXICON['/speciality'], reply_markup=speciality_keyboard())
    # Устанавливаем пользователю состояние "step1"
    await state.set_state(St.step1)  # !!!пропускает команду Назад!!!


# Состояние выбора врача
@router.message(St.step1)
async def cmd_doctor(message: Message, state: FSMContext):
    item1 = message.text
    # await state.update_data(
    #     {
    #         'item1': item1
    #     }
    # )
    await message.answer(text=LEXICON['/doctor'], reply_markup=doctor_keyboard(item1))
    await state.set_state(St.step2)


# # Состояние выбора времени
# @router.message(St.step2)
# async def cmd_time(message: Message, state: FSMContext):
#     item2 = message.text
#     await message.answer("Выберите время", reply_markup=time_keyboard(item2))


@router.message(Command(commands=["cancel"]))
@router.message(F.text == "Назад")
async def cmd_cancel(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        text="Действие отменено",
        reply_markup=main_keyboard
    )


# Срабатывает на сообщения пользователя
@router.message()
async def send_answer(message: Message):
    if message.text == "Посмотреть мою запись":
        await message.answer("Смотрите")
    elif message.text == "Отменить запись":
        await message.answer("Отменяйте")
    else:
        await message.answer(text=LEXICON['other_answer'])
