from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

back_message = '👈 Назад'
confirm_message = '✅ Подтвердить'
all_right_message = '✅ Все верно'
cancel_message = '🚫 Отменить'
craete_news_message = '🖋 Оповестить Админов'
# view_news_message = '🗿 Мои новости'
# view_all_news_message = '🌚 Все новости'
view_news_admin_message = "📦 Проверить посты"
# edit_news_message= "👩🏿‍🎨 Изменить новсть"
skip_news_message = "🙅‍♂️ Скип"
# edit_news_next_message = "👉 Следующее"

def get_keyboard():
    keyboard = ReplyKeyboardMarkup()
    button = KeyboardButton("Поделиться Локацией", request_location=True)
    button2 = KeyboardButton(back_message)
    keyboard.add(button)
    keyboard.add(button2)
    return keyboard

def confirm_markup():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.add(confirm_message)
    markup.add(back_message)

    return markup

def back_markup():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.add(back_message)

    return markup

def check_markup():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.row(back_message, all_right_message)

    return markup

def submit_markup():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.row(cancel_message, all_right_message)

    return markup

def user_defalt_markup():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.row(craete_news_message)

    return markup

def admin_defalt_markup():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, selective=True, row_width=2)
    [markup.add(i) for i in [view_news_admin_message]]

    return markup

# def admin_edit_news_markup():
#     markup = ReplyKeyboardMarkup(resize_keyboard=True, selective=True, row_width=2)
#     markup.add(edit_news_next_message)

#     return markup

def admin_confirm_markup():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.add(confirm_message)
    markup.add(cancel_message)
    markup.add(skip_news_message)

    return markup
