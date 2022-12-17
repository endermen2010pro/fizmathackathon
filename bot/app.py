
import os
import handlers
from aiogram import executor, types
from states import admin_viewState, newsState
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove
from data import config
from loader import dp, db, bot
import filters
import logging
from keyboards.default.markups import *

filters.setup(dp)

WEBAPP_HOST = "0.0.0.0"
WEBAPP_PORT = int(os.environ.get("PORT", 5000))
user_message = 'Пользователь'
admin_message = 'Админ'


@dp.message_handler(commands='start', state="*")
async def cmd_start(message: types.Message):

    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    markup.row(user_message, admin_message)

    await message.answer('''Привет! 👋

🤖 Я бот-раб. Я загружаю ваши новости на tempmpdsite.tmt4.kz
    
😱 Чтобы написать новость, нужно нажать на \n"🖋 Создать новость".

📝 Ваша новость будет расмотренна админитраторами, после этого она появиться на сайте.

📍 Для новостей у которых описание больше чем 350 символов предусмотрена отдельная страничка.

🩸 Если у вас залагал бот напишите /start для обновления

🤝 Заказать похожего бота? Свяжитесь с разработчиком <a href="https://t.me/Dtorossyan">David Torossyan</a>, он не кусается)))
    ''', reply_markup=markup)
    cid = message.chat.id
    if cid in config.ADMINS:
        config.ADMINS.append(cid)
        await message.answer('Включен админский режим.', reply_markup=admin_defalt_markup())
    else:
        await message.answer('Включен пользовательский режим.', reply_markup=user_defalt_markup())

async def on_startup(dp):
    logging.basicConfig(level=logging.INFO)
    db.create_tables()


async def on_shutdown():
    logging.warning("Shutting down..")
    await dp.storage.close()
    await dp.storage.wait_closed()
    logging.warning("Bot down")


if __name__ == '__main__':

    executor.start_polling(dp, on_startup=on_startup, skip_updates=False)
