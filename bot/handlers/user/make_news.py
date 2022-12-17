from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery,KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, ContentType, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.utils.callback_data import CallbackData
from keyboards.default.markups import *
from states import newsState
from aiogram.types.chat import ChatActions
from loader import dp, db, bot
from filters import IsUser

@dp.message_handler(IsUser(), text=craete_news_message, state="*")
async def process_add_product(message: Message):
    await newsState.title.set()

    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(cancel_message)

    await message.answer('Название?', reply_markup=markup)


@dp.message_handler(IsUser(), text=cancel_message, state=newsState.title)
async def process_cancel(message: Message, state: FSMContext):

    await message.answer('Ок, отменено!', reply_markup=user_defalt_markup())
    await state.finish()


@dp.message_handler(IsUser(), text=back_message, state=newsState.title)
async def process_title_back(message: Message, state: FSMContext):
    await process_add_product(message)


@dp.message_handler(IsUser(), state=newsState.title)
async def process_title(message: Message, state: FSMContext):

    async with state.proxy() as data:
        data['title'] = message.text

    await newsState.next()
    await message.answer('Описание?', reply_markup=back_markup())


@dp.message_handler(IsUser(), text=back_message, state=newsState.body)
async def process_body_back(message: Message, state: FSMContext):

    await newsState.title.set()

    async with state.proxy() as data:

        await message.answer(f"Изменить название с <b>{data['title']}</b>?", reply_markup=back_markup())


@dp.message_handler(IsUser(), state=newsState.body)
async def process_body(message: Message, state: FSMContext):

    async with state.proxy() as data:
        data['body'] = message.text

    # if(len(message.text)<=350):
    #     await message.answer(f"У вас новость длиной {len(message.text)}, для новостей у которых количество символов < 350 не будет создаваться отдельная страница.")
    # else:
    #     await message.answer(f"У вас новость длиной {len(message.text)}, для вашей новости будет созданна отделльня страница.")

    await newsState.next()
    await message.answer('Фото?', reply_markup=back_markup())

@dp.message_handler(IsUser(), text=back_message, state=newsState.image)
async def process_image_photo_back(message: Message, state: FSMContext):

    await newsState.body.set()

    async with state.proxy() as data:
        await message.answer(f"Изменить название с <b>{data['body']}</b>?", reply_markup=back_markup())


@dp.message_handler(IsUser(), content_types=ContentType.PHOTO, state=newsState.image)
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

    await message.answer('Локация?', reply_markup=get_keyboard())

@dp.message_handler(IsUser(), state=newsState.image)
async def change_body_and_next(message: Message, state: FSMContext):
    await message.answer("ОТПРАВТЕ ФОТОГРАФИЮ!!!")


@dp.message_handler(IsUser(), text=back_message, state=newsState.location)
async def process_location_back(message: Message, state: FSMContext):

    await newsState.image.set()

    await message.answer(f"Другое фото?", reply_markup=back_markup())


@dp.message_handler(IsUser(), content_types=['location'], state=newsState.location)
async def process_location(message: Message, state: FSMContext):
    lat = message.location.latitude
    lon = message.location.longitude

    async with state.proxy() as data:
        data['location'] = str(f'{lat},{lon}')
    title = data['title']
    body = data['body']
    image = data['image']

    await newsState.next()


    markup = check_markup()
    text = f'{title} \n{body}'
    await message.answer_photo(photo=image,
                                reply_markup=markup)
    await message.answer(text)


@dp.message_handler(IsUser(), lambda message: message.text not in [back_message, all_right_message], state=newsState.confirm)
async def process_confirm_invalid(message: Message, state: FSMContext):
    await message.answer('Такого варианта не было.')


@dp.message_handler(IsUser(), text=back_message, state=newsState.confirm)
async def process_confirm_back(message: Message, state: FSMContext):

    await newsState.location.set()

    async with state.proxy() as data:
        await message.answer(f"Изменить Локацию??", reply_markup=get_keyboard())


@dp.message_handler(IsUser(), text=all_right_message, state=newsState.confirm)
async def process_confirm(message: Message, state: FSMContext):

    async with state.proxy() as data:
        user_id = message.from_user.id
        title = data['title']
        body = data['body']
        image = data['image']
        location = data['location']
        imageUrl = data["imageurl"]

        db.query('INSERT INTO news VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                 (None, user_id, location, title, body, image, None, imageUrl))

    await state.finish()
    await message.answer('Готово!', reply_markup=user_defalt_markup())