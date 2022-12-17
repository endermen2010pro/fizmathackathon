from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from loader import dp, db
from states import admin_viewState
from keyboards.default.markups import *
from filters import IsAdmin
from keyboards.default.markups import *

from supabase import create_client, Client

url = "https://wsyguraczxyaviqiadza.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6IndzeWd1cmFjenh5YXZpcWlhZHphIiwicm9sZSI6ImFub24iLCJpYXQiOjE2NjgyNjU5NzAsImV4cCI6MTk4Mzg0MTk3MH0.lHksI0mHyA8LrBOF8sqJ7-WHvZAKyYvfeIaqisenUFc"
supabase: Client = create_client(url, key)

def get_next_news():
    orders = db.fetchall('SELECT * FROM news WHERE ischecked IS NULL ORDER BY ROWID')
    if(len(orders)==0):
        return "Пока что новостей нет"
    return orders

@dp.message_handler(IsAdmin(), text=view_all_news_message, state="*")
async def get_all_news(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['post_id'] = 0
    orders = db.fetchall('SELECT * FROM news')
    for news in orders:
        text = f"id - {news[0]} \nuid - {news[1]}\n title - {news[2]}\n body - {news[3]}\n author - {news[5]}"
        await message.answer_photo(photo=news[4],
                                reply_markup=admin_defalt_markup())
        await message.answer(text)

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
        text = f"id - {news[0][0]} \nuid - {news[0][1]}\n title - {news[0][2]}\n body - {news[0][3]}\n author - {news[0][5]}"
        await message.answer_photo(photo=news[0][4],
                                reply_markup=admin_confirm_markup())
        await message.answer(text)
        async with state.proxy() as data:
            data['now_cheked_id'] = news[0][0]
    # orders = db.fetchall('SELECT * FROM news WHERE ischecked = 0 ORDER BY ROWID ASC LIMIT 1')
    # # print(len(orders))
    # if len(orders) == 0: await message.answer('Пока что новостей нет')
    # else: 
    #     text = f"id - {orders[0][0]} \nuid - {orders[0][1]}\n title - {orders[0][2]}\n body - {orders[0][3]}\n author - {orders[0][5]}"
    #     await message.answer_photo(photo=orders[0][4],
    #                             caption=text,
    #                             reply_markup=admin_confirm_markup())
    #     async with state.proxy() as data:
    #         data['now_cheked_id'] = orders[0][0]
    #     await admin_viewState.nextNews.set() 

@dp.message_handler(IsAdmin(), text=confirm_message, state=admin_viewState.nextNews)
async def accept_news(message: Message, state: FSMContext):
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
            text = f"id - {news[0][0]} \nuid - {news[0][1]}\n title - {news[0][2]}\n body - {news[0][3]}\n author - {news[0][5]}"
            await message.answer_photo(photo=news[0][4],
                                reply_markup=admin_confirm_markup())
            await message.answer(text)
            async with state.proxy() as data:
                data['now_cheked_id'] = news[0][0]
        return
    # orders2 = db.fetchall(f'SELECT * FROM news WHERE idx = {id}')
    # await message.answer_photo(photo=orders2[0][4])
    isclikbl = False
    if len(orders[0][3])>350:
        isclikbl = True
    data = supabase.table("trend").insert({"title":orders[0][2],"body":orders[0][3],"author":orders[0][5],"fileurl":orders[0][7],'clickable':isclikbl}).execute()
    assert len(data.data) > 0
    db.query(f"UPDATE news SET ischecked = 1 WHERE idx = {id}")
    news = get_next_news()
    if(news == 'Пока что новостей нет'):
        await message.answer('Пока что новостей нет',reply_markup=admin_defalt_markup())
        await admin_viewState.start.set()
    else:
        text = f"id - {news[0][0]} \nuid - {news[0][1]}\n title - {news[0][2]}\n body - {news[0][3]}\n author - {news[0][5]}"
        await message.answer_photo(photo=news[0][4],
                                reply_markup=admin_confirm_markup())
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
            text = f"id - {news[0][0]} \nuid - {news[0][1]}\n title - {news[0][2]}\n body - {news[0][3]}\n author - {news[0][5]}"
            await message.answer_photo(photo=news[0][4],
                                reply_markup=admin_confirm_markup())
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
        text = f"id - {news[0][0]} \nuid - {news[0][1]}\n title - {news[0][2]}\n body - {news[0][3]}\n author - {news[0][5]}"
        await message.answer_photo(photo=news[0][4],
                                reply_markup=admin_confirm_markup())
        await message.answer(text)
        async with state.proxy() as data:
            data['now_cheked_id'] = news[0][0]

    
