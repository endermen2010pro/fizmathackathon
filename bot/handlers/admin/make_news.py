from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, ContentType, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.utils.callback_data import CallbackData
from keyboards.default.markups import *
from states import newsState
from aiogram.types.chat import ChatActions
from loader import dp, db, bot
from filters import IsAdmin
from PIL import Image,ImageFilter
import io

@dp.message_handler(IsAdmin(), text=craete_news_message, state="*")
async def process_add_news(message: Message):
    await newsState.title.set()

    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(cancel_message)

    await message.answer('Название?', reply_markup=markup)


@dp.message_handler(IsAdmin(), text=cancel_message, state=newsState.title)
async def process_cancel(message: Message, state: FSMContext):

    await message.answer('Ок, отменено!', reply_markup=admin_defalt_markup())
    await state.finish()


@dp.message_handler(IsAdmin(), text=back_message, state=newsState.title)
async def process_title_back(message: Message, state: FSMContext):
    await process_add_news(message)


@dp.message_handler(IsAdmin(), state=newsState.title)
async def process_title(message: Message, state: FSMContext):

    async with state.proxy() as data:
        data['title'] = message.text

    await newsState.next()
    await message.answer('Описание?', reply_markup=back_markup())


@dp.message_handler(IsAdmin(), text=back_message, state=newsState.body)
async def process_body_back(message: Message, state: FSMContext):

    await newsState.title.set()

    async with state.proxy() as data:

        await message.answer(f"Изменить название с <b>{data['title']}</b>?", reply_markup=back_markup())


@dp.message_handler(IsAdmin(), state=newsState.body)
async def process_body(message: Message, state: FSMContext):

    async with state.proxy() as data:
        data['body'] = message.text

    await newsState.next()
    await message.answer('Фото?', reply_markup=back_markup())

@dp.message_handler(IsAdmin(), text=back_message, state=newsState.image)
async def process_image_photo_back(message: Message, state: FSMContext):

    await newsState.body.set()

    async with state.proxy() as data:
        await message.answer(f"Изменить описание с <b>{data['body']}</b>?", reply_markup=back_markup())


@dp.message_handler(IsAdmin(), content_types=ContentType.PHOTO, state=newsState.image)
async def process_image_photo(message: Message, state: FSMContext):
    print("yes")
    fileID = message.photo[-1].file_id
    file_info = await bot.get_file(fileID)
    file_path = await file_info.get_url()
    downloaded_file = (await bot.download_file(file_info.file_path)).read()

    async with state.proxy() as data:
        data['image'] = downloaded_file
        data['imageurl'] = file_path

    await newsState.next()

    await message.answer('Автор?', reply_markup=back_markup())

@dp.message_handler(IsAdmin(), state=newsState.image)
async def change_body_and_next(message: Message, state: FSMContext):
    await message.answer("ОТПРАВТЕ ФОТОГРАФИЮ!!!")


@dp.message_handler(IsAdmin(), text=back_message, state=newsState.author)
async def process_author_back(message: Message, state: FSMContext):

    await newsState.image.set()

    await message.answer(f"Другое фото?", reply_markup=back_markup())


@dp.message_handler(IsAdmin(), state=newsState.author)
async def process_author(message: Message, state: FSMContext):

    async with state.proxy() as data:
        data['author'] = message.text
    author = data['author']
    title = data['title']
    body = data['body']
    image = data['image']

    print(body)

    await newsState.next()


    markup = check_markup()
    text = f'{title} \n{body} \n\n@{author}'
    await message.answer_photo(photo=image,
                                reply_markup=markup)
    await message.answer(text)


@dp.message_handler(IsAdmin(), lambda message: message.text not in [back_message, all_right_message], state=newsState.confirm)
async def process_confirm_invalid(message: Message, state: FSMContext):
    await message.answer('Такого варианта не было.')


@dp.message_handler(IsAdmin(), text=back_message, state=newsState.confirm)
async def process_confirm_back(message: Message, state: FSMContext):

    await newsState.author.set()

    async with state.proxy() as data:

            await message.answer(f"Изменить Автора с <b>{data['author']}</b>?", reply_markup=back_markup())


@dp.message_handler(IsAdmin(), text=all_right_message, state=newsState.confirm)
async def process_confirm(message: Message, state: FSMContext):

    async with state.proxy() as data:
        user_id = message.from_user.id
        title = data['title']
        body = data['body']
        image = data['image']
        author = data['author']
        imageUrl = data["imageurl"]

        # tag = db.fetchone(
        #     'SELECT title FROM categories WHERE idx=?', (data['category_index'],))[0]
        # idx = md5(' '.join([title, body, tag]
        #                    ).encode('utf-8')).hexdigest()

        db.query('INSERT INTO news VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                 (None, user_id, title, body, image, author, None, imageUrl))

    await state.finish()
    await message.answer('Готово!', reply_markup=admin_defalt_markup())