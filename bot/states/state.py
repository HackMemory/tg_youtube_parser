from aiogram.dispatcher.filters.state import State, StatesGroup

class SetSearchName(StatesGroup):
    """
    State class for search-name.
    """
    name = State()

class SetSearchKeyword(StatesGroup):
    """
    State class for search-keyword.
    """
    keyword = State()