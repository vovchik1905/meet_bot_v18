from aiogram.dispatcher.filters.state import State, StatesGroup

class HandlerStates(StatesGroup):
    """
    Класс состояний

    """
    NONE = State()
    START_COMMAND = State()
    HELP_COMMAND = State()
    REG_COMMAND = State()

    GET_NAME_STEP = State()
    GET_GENDER_STEP = State()
    GET_AGE_STEP = State()
    GET_SCHOOL_STEP = State()
    GET_PHOTO_STEP = State()
    GET_TEXT_STEP = State()
    END_REG_STEP = State()

    MAIN_MENU_STEP = State()
    MAIN_MENU_STEP_WORKER = State()
    SHOW_MY_PROFILE_STEP = State()
    SHOW_HUMAN_PROFILE_STEP = State()
    FINISH_VIEWING_STEP = State()
    #FINISH_VIEWING_STEP_CHECK = State()
    AFFILIATE_PROGRAM_STEP = State()
    SHOW_LIKE_STEP = State()

    CHANGE_MY_PHOTO = State()
    CHANGE_MY_TEXT = State()
    REG_MY_PROFILE = State()
    
    LIKE_AND_TEXT = State()
