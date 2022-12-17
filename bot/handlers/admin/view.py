from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from loader import dp, db
import json
from states import admin_viewState
from keyboards.default.markups import *
from filters import IsAdmin
from keyboards.default.markups import *
import firebase_admin
from firebase_admin import db as firease_db


cred_obj = firebase_admin.credentials.Certificate('./data/serviceAccountKey.json')
default_app = firebase_admin.initialize_app(cred_obj, {
	'databaseURL':'https://fizmatgovnoton-default-rtdb.firebaseio.com/'
})
ref = firease_db.reference("/reports")

def get_next_news():
    orders = db.fetchall('SELECT * FROM news WHERE ischecked IS NULL ORDER BY ROWID')
    print(orders)
    if(len(orders)==0):
        return "Пока что новостей нет"
    return orders

# @dp.message_handler(IsAdmin(), text=view_all_news_message, state="*")
# async def get_all_news(message: Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['post_id'] = 0
#     orders = db.fetchall('SELECT * FROM news')
#     for news in orders:
#         text = f"id - {news[0]} \nuid - {news[1]}\n title - {news[2]}\n body - {news[3]}\n author - {news[5]}"
#         await message.answer_photo(photo=news[4],
#                                 reply_markup=admin_defalt_markup())
#         await message.answer(text)

@dp.message_handler(IsAdmin(), text=skip_news_message, state=admin_viewState.nextNews)
async def skip_news(message: Message, state: FSMContext):
    await state.finish()
    await message.answer('oke',reply_markup=admin_defalt_markup())

@dp.message_handler(IsAdmin(), text=view_news_admin_message, state="*")
async def process_news(message: Message, state: FSMContext):
    news = get_next_news()
    if(news == 'Пока что новостей нет'):
        await admin_viewState.start.set()
        await message.answer('Пока что новостей нет',reply_markup=admin_defalt_markup())
    else:
        await admin_viewState.nextNews.set() 
        location = list(map(float,news[0][2].split(',')))
        print(location)
        lon, lat = location[0], location[1]

        text = f"id - {news[0][0]} \nuid - {news[0][1]}\n title - {news[0][3]}\n body - {news[0][4]}"
        await message.answer_photo(photo=news[0][5],
                                reply_markup=admin_confirm_markup())
        await message.answer_location(lon, lat)
        await message.answer(text)
        async with state.proxy() as data:
            data['now_cheked_id'] = news[0][0]

@dp.message_handler(IsAdmin(), text=confirm_message, state=admin_viewState.nextNews)
async def accept_news(message: Message, state: FSMContext):
    global ref
    async with state.proxy() as data:
        id = data['now_cheked_id']
    orders = db.fetchall(f'SELECT * FROM news WHERE idx = {id}')

    if(orders[0][6]!=None):
        await message.answer("Кто то другой уже сдеал это!")
        news = get_next_news()
        if(news == 'Пока что новостей нет'):
            await message.answer('Пока что новостей нет',reply_markup=admin_defalt_markup())
            await admin_viewState.start.set()
        else:
            location = list(map(float,news[0][2].split(',')))
            print(location)
            lon, lat = location[0], location[1]

            text = f"id - {news[0][0]} \nuid - {news[0][1]}\n title - {news[0][3]}\n body - {news[0][4]}"
            await message.answer_photo(photo=news[0][5],
                                    reply_markup=admin_confirm_markup())
            await message.answer_location(lon, lat)
            await message.answer(text)
            async with state.proxy() as data:
                data['now_cheked_id'] = news[0][0]
        return
    accepted = db.fetchall('SELECT * FROM news ORDER BY ROWID')
    # data = supabase.table("trend").insert({"title":orders[0][2],"body":orders[0][3],"author":orders[0][5],"fileurl":orders[0][7],'clickable':isclikbl}).execute()
    datatofb = {}
    for i in accepted:
        datatofb[i[3]] = {"loaction":i[2],'body':i[4],'image':i[7],'isAccepted':"false"}
    json_data_to_fb = json.dumps(datatofb)
    ref.set(json_data_to_fb)
    db.query(f"UPDATE news SET ischecked = 1 WHERE idx = {id}")
    news = get_next_news()
    if(news == 'Пока что новостей нет'):
        await message.answer('Пока что новостей нет',reply_markup=admin_defalt_markup())
        await admin_viewState.start.set()
    else:
        location = list(map(float,news[0][2].split(',')))
        print(location)
        lon, lat = location[0], location[1]

        text = f"id - {news[0][0]} \nuid - {news[0][1]}\n title - {news[0][3]}\n body - {news[0][4]}"
        await message.answer_photo(photo=news[0][5],
                                reply_markup=admin_confirm_markup())
        await message.answer_location(lon, lat)
        await message.answer(text)
        async with state.proxy() as data:
            data['now_cheked_id'] = news[0][0]

@dp.message_handler(IsAdmin(), text=cancel_message, state=admin_viewState.nextNews)
async def deaccept_news(message: Message, state: FSMContext):
    async with state.proxy() as data:
        id = data['now_cheked_id']
    orders = db.fetchall(f'SELECT * FROM news WHERE idx = {id}')

    if(orders[0][6]!=None):
        await message.answer("Кто то другой уже сдеал это!")
        news = get_next_news()
        if(news == 'Пока что новостей нет'):
            await message.answer('Пока что новостей нет',reply_markup=admin_defalt_markup())
            await admin_viewState.start.set()
        else:
            location = list(map(float,news[0][2].split(',')))
            print(location)
            lon, lat = location[0], location[1]

            text = f"id - {news[0][0]} \nuid - {news[0][1]}\n title - {news[0][3]}\n body - {news[0][4]}"
            await message.answer_photo(photo=news[0][5],
                                    reply_markup=admin_confirm_markup())
            await message.answer_location(lon, lat)
            await message.answer(text)
            async with state.proxy() as data:
                data['now_cheked_id'] = news[0][0]
        return
    
    db.query(f"UPDATE news SET ischecked = 0 WHERE idx = {id}")
    news = get_next_news()
    if(news == 'Пока что новостей нет'):
        await message.answer('Пока что новостей нет',reply_markup=admin_defalt_markup())
        await admin_viewState.start.set()
    else:
        location = list(map(float,news[0][2].split(',')))
        print(location)
        lon, lat = location[0], location[1]

        text = f"id - {news[0][0]} \nuid - {news[0][1]}\n title - {news[0][3]}\n body - {news[0][4]}"
        await message.answer_photo(photo=news[0][5],
                                reply_markup=admin_confirm_markup())
        await message.answer_location(lon, lat)
        await message.answer(text)
        async with state.proxy() as data:
            data['now_cheked_id'] = news[0][0]

    
