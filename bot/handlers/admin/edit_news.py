from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, ContentType, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.utils.callback_data import CallbackData
from keyboards.default.markups import *
from states import newsEditState
from aiogram.types.chat import ChatActions
from loader import dp, db, bot
from datetime import datetime
from filters import IsAdmin

@dp.message_handler(IsAdmin(), text=edit_news_message, state="*")
async def select_edit_news(message: Message):
    await newsEditState.selectId.set()

    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(cancel_message)

    await message.answer('какую новость вы хотите изменить?', reply_markup=markup)

@dp.message_handler(IsAdmin(), text=cancel_message, state=newsEditState.selectId)
async def edit_process_cancel(message: Message, state: FSMContext):

    await message.answer('Ок, отменено!', reply_markup=admin_defalt_markup())
    await state.finish()

@dp.message_handler(IsAdmin(), state=newsEditState.selectId)
async def setID_edit_news(message: Message, state: FSMContext):
    try:
        print(message.text)
        id = int(message.text)
    except:
        await message.answer("ведите число - id новости которую вы хотите исправить")
        return
    news = db.fetchall(f'SELECT * FROM news WHERE idx = {id}')[0]
    async with state.proxy() as data:
        data["idx"] = news[0]
        data['iduser'] = news[1]
        data['title'] = news[2]
        data['body'] = news[3]
        data['photo'] = news[4]
        data['author'] = news[5]
        data['ischecked'] = news[6]
        text = data['title']+'\n'+data['body']+"\n\n@"+data['author']
        # await message.answer_photo(photo=data['photo'],
        #                             caption=text)
        await message.answer_photo(photo=data['photo'])
        await message.answer(text)
        await message.answer(f"Изменить тайтл? \n{data['title']}",reply_markup=admin_edit_news_markup())
    await newsEditState.title.set()

@dp.message_handler(IsAdmin(), text=edit_news_next_message ,state=newsEditState.title)
async def set_defalt_title_and_next(message: Message, state: FSMContext):
    async with state.proxy() as data:
        await message.answer(f"Изменить тело? \n{data['body']}",reply_markup=admin_edit_news_markup())
    await newsEditState.body.set()

@dp.message_handler(IsAdmin(), state=newsEditState.title)
async def change_title_and_next(message: Message, state: FSMContext):
    async with state.proxy() as data:
        dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print("EDIT in" + dt_string, data['title'],sep='\n')
        data['title'] = message.text
        await message.answer("title измененно")
        await message.answer(f"Изменить тело? \n{data['body']}",reply_markup=admin_edit_news_markup())
    await newsEditState.body.set()

@dp.message_handler(IsAdmin(), text=edit_news_next_message ,state=newsEditState.body)
async def set_defalt_body_and_next(message: Message, state: FSMContext):
    async with state.proxy() as data:
        await message.answer_photo(photo=data['photo'],
                                caption="Изменить фото?",
                                reply_markup=admin_edit_news_markup())
    await newsEditState.image.set()

@dp.message_handler(IsAdmin(), state=newsEditState.body)
async def change_body_and_next(message: Message, state: FSMContext):
    async with state.proxy() as data:
        dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print("EDIT in" + dt_string, data['body'],sep='\n')
        data['body'] = message.text
        await message.answer("тело измененно")
        await message.answer_photo(photo=news[0][4],
                                reply_markup=admin_confirm_markup())
        await message.answer(text)
    await newsEditState.image.set()


@dp.message_handler(IsAdmin(), text=edit_news_next_message ,state=newsEditState.image)
async def set_defalt_body_and_next(message: Message, state: FSMContext):
    print("yes")
    async with state.proxy() as data:
        db.query(f"UPDATE news SET title = ?,body = ?,photo = ? WHERE idx = {data['idx']}",(data['title'],data['body'],data['photo']))
    await message.answer("Новость измененна!", reply_markup=admin_defalt_markup())
    await state.finish()

@dp.message_handler(IsAdmin(), content_types=ContentType.PHOTO, state=newsEditState.image)
async def change_body_and_next(message: Message, state: FSMContext):
    fileID = message.photo[-1].file_id
    file_info = await bot.get_file(fileID)
    downloaded_file = (await bot.download_file(file_info.file_path)).read()

    async with state.proxy() as data:
        dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print("EDIT photo in" + dt_string)
        data['photo'] = downloaded_file
        db.query(f"UPDATE news SET title = ?,body = ?,photo = ? WHERE idx = {data['idx']}",(data['title'],data['body'],data['photo']))
        await message.answer("Новость измененна!", reply_markup=admin_defalt_markup())
    await newsEditState.image.set()
    await state.finish()

@dp.message_handler(IsAdmin(), state=newsEditState.image)
async def change_body_and_next(message: Message, state: FSMContext):
    await message.answer("ОТПРАВТЕ ФОТОГРАФИЮ!!!")



    