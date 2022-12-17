from aiogram.dispatcher.filters.state import StatesGroup, State

class newsState(StatesGroup):
    title = State()
    body = State()
    image = State()
    location = State()
    confirm = State()

# class newsEditState(StatesGroup):
#     selectId = State()
#     title = State()
#     body = State()
#     image = State()

class admin_viewState(StatesGroup):
    start = State()
    nextNews = State()