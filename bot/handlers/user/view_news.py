from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, ContentType, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.utils.callback_data import CallbackData
from keyboards.default.markups import *
from states import newsState
from aiogram.types.chat import ChatActions
from loader import dp, db, bot
from filters import IsUser

@dp.message_handler(IsUser(), text=view_news_message)
async def view_my_news(message: Message,state="*"):
    id = message.from_user.id
    ls = db.fetchall(f'SELECT * FROM news WHERE iduser = {id}')
    ls = ls[-10:]
    print(len(ls))
    if(len(ls)==0): 
        await message.answer("У вас еще нет новостей")
    else:
        for news in ls:
            wait = "В очереди"
            if(news[6]==1):
                wait = "На сайте"
            elif(news[6]==0):
                wait = "Отменено"

            text = f"<b>{news[2]}</b>\n{news[3]}\nАвтор:{news[5]}\nОжидание - {wait}"
            await message.answer_photo(photo=news[4]
                            ,reply_markup=user_defalt_markup())
            await message.answer(text)