from tabnanny import check
from aiogram import types
from typing import Any
from bot_model.app.states.handler_states import HandlerStates
from bot_model.app.views.keyboards.keyboards import GenderKeyboard, SchoolKeyboard, MainMenuKeyboard, LikeMenuKeyboard, MyProfileKeyboard, AffiliateProgramKeyboard, CheckKeyboard
from bot_model.app.db.object_model import *
from bot_model.app.db.models.db_model import *
from settings.view.messages.messages import Message
from settings.logic.condition.conditions import Condition
from bot_model.app.db.scripts.db_requests import DbRequest

class DbWorker:
    """
    Класс работы с базой данных.
    """
    
    def start_command_db_worker(next_state: HandlerStates, answer: types.Message) -> Any:
        """
        """
        main_menu_keyboard_obj = MainMenuKeyboard()
        main_menu_keyboard = main_menu_keyboard_obj.main_menu_keyboard

        TelegramRuntime.tg_id = answer.from_user.id
        TelegramRuntime.tg_name = answer.from_user.first_name
        TelegramRuntime.tg_sername = answer.from_user.last_name
        TelegramRuntime.tg_username = answer.from_user.username
        TelegramRuntime.id = Telegram.get_or_none(tg_id = TelegramRuntime.tg_id)
        if TelegramRuntime.id is None:
            create_telegram = Telegram(tg_id = TelegramRuntime.tg_id,
                                            tg_name = TelegramRuntime.tg_name,
                                            tg_sername = TelegramRuntime.tg_sername,
                                            tg_username = TelegramRuntime.tg_username)
            TelegramRuntime.id = create_telegram.save()
            UserRuntime.state = 2
            UserRuntime.status = 5.0
            create_user = User(telegram=TelegramRuntime.id, state = UserRuntime.state, status = UserRuntime.status)
            UserRuntime.id = create_user.save()

            TgStateRuntime.tg_state = 2
            TgStateRuntime.user_id = UserRuntime.id
            create_tg_states = TgState(user_id = TgStateRuntime.user_id, tg_state = TgStateRuntime.tg_state)
            TgStateRuntime.id = create_tg_states.save()
            return (Message.START_COMMAND, main_menu_keyboard, True)
        
        else:
            UserRuntime.id = User.select().where(User.telegram == TelegramRuntime.id).get()
            UserRuntime.state = User.get(User.id == UserRuntime.id).state
            UserRuntime.status = User.get(User.id == UserRuntime.id).status
            TgStateRuntime.id = TgState.select().where(TgState.user_id == UserRuntime.id).get()
            TgStateRuntime.tg_state = TgState.get(TgState.id == TgStateRuntime.id).tg_state
            
            if TgStateRuntime.tg_state >= 8:
                UserRuntime.name = User.get(User.id == UserRuntime.id).name
                UserRuntime.gender = User.get(User.id == UserRuntime.id).gender
                UserRuntime.year = User.get(User.id == UserRuntime.id).year
                UserRuntime.school = User.get(User.id == UserRuntime.id).school
                
                UserPhotoRuntime.user_id = UserRuntime.id
                UserPhotoRuntime.id = User_Photo.select().where(User_Photo.user_id == UserPhotoRuntime.user_id).get()
                UserPhotoRuntime.photo_id = User_Photo.get(User_Photo.id == UserPhotoRuntime.id).photo_id
                PhotoRuntime.id = UserPhotoRuntime.photo_id
                PhotoRuntime.foto_tg_id = Photo.get(Photo.id == PhotoRuntime.id).foto_tg_id
                PhotoRuntime.foto_extension = Photo.get(Photo.id == PhotoRuntime.id).foto_extension
                
                UserRuntime.profile_text = User.get(User.id == UserRuntime.id).profile_text

            if UserRuntime.state == 1:
                return (Message.USER_BAN, None, True)

            return (Message.START_COMMAND, main_menu_keyboard, True)
    
    def help_command_db_worker(next_state: HandlerStates, answer: types.Message):
        """
        """
        return (Message.HELP_COMMAND, None, True)

    def reg_command_db_worker(next_state: HandlerStates, answer: types.Message):
        """
        """
        if UserRuntime.state == 1:
                return (Message.USER_BAN, None, True)
        return (Message.GET_NAME_STEP, None, True)

    def get_name_step_db_worker(next_state: HandlerStates, answer: types.Message):
        """
        """

        gender_keyboard_obj = GenderKeyboard()
        gender_keyboard = gender_keyboard_obj.gender_keyboard

        UserRuntime.name = answer.text
        DbRequest.update_user_name(UserRuntime.name)
        TgStateRuntime.tg_state = 3
        DbRequest.update_tg_state(TgStateRuntime.tg_state)
        return (Message.GET_GENDER_STEP, gender_keyboard, True)
    
    def get_gender_step_db_worker(next_state: HandlerStates, answer: types.Message):
        """
        """

        if next_state == HandlerStates.GET_GENDER_STEP:
            gender_keyboard_obj = GenderKeyboard()
            gender_keyboard = gender_keyboard_obj.gender_keyboard
            return (Message.RETRY_GET_GENDER_STEP, gender_keyboard, True)
        
        elif next_state == HandlerStates.GET_AGE_STEP:
            gender = answer.text
            if gender == Condition.GENDER_MAN_VALUE:
                UserRuntime.gender = 1
            elif gender == Condition.GENDER_HUMAN_VALUE:
                UserRuntime.gender = 2
            
            DbRequest.update_user_gender(UserRuntime.gender)
            TgStateRuntime.tg_state = 4
            DbRequest.update_tg_state(TgStateRuntime.tg_state)
            return (Message.GET_AGE_STEP, None, True)

    def get_age_step_db_worker(next_state: HandlerStates, answer: types.Message):
        """
        """

        if next_state == HandlerStates.GET_SCHOOL_STEP:
            school_keyboard_obj = SchoolKeyboard()
            school_keyboard = school_keyboard_obj.school_keyboard
            UserRuntime.year = answer.text
            DbRequest.update_user_year(UserRuntime.year)
            TgStateRuntime.tg_state = 5
            DbRequest.update_tg_state(TgStateRuntime.tg_state)
            return (Message.GET_SCHOOL_STEP, school_keyboard, True)
        
        elif next_state == HandlerStates.GET_AGE_STEP:
            return (Message.RETRY_GET_AGE_STEP, None, True)

    def get_school_step_db_worker(next_state: HandlerStates, answer: types.Message):
        """
        """

        if next_state == HandlerStates.GET_PHOTO_STEP:
            UserRuntime.school = answer.text
            DbRequest.update_user_school(UserRuntime.school)
            TgStateRuntime.tg_state = 6
            DbRequest.update_tg_state(TgStateRuntime.tg_state)
            return (Message.GET_PHOTO_STEP, None, True)
        
        elif next_state == HandlerStates.GET_SCHOOL_STEP:
            school_keyboard_obj = SchoolKeyboard()
            school_keyboard = school_keyboard_obj.school_keyboard
            return (Message.RETRY_GET_SCHOOL_STEP, school_keyboard, True)

    def get_photo_step_db_worker(next_state: HandlerStates, answer: types.Message):
        """"""
        PhotoRuntime.foto_tg_id = answer.photo[-1].file_id

        create_photo = Photo(foto_tg_id = PhotoRuntime.foto_tg_id)
        PhotoRuntime.id = create_photo.save()
        
        UserPhotoRuntime.user_id = UserRuntime.id
        UserPhotoRuntime.photo_id = PhotoRuntime.id
        create_user_photo = User_Photo(user_id = UserPhotoRuntime.user_id, photo_id = UserPhotoRuntime.photo_id)
        UserPhotoRuntime.id = create_user_photo.save()
        TgStateRuntime.tg_state = 7
        DbRequest.update_tg_state(TgStateRuntime.tg_state)
        return (Message.GET_TEXT_STEP, None, True)
    
    def get_text_step_db_worker(next_state: HandlerStates, answer: types.Message):
        """
        """

        main_menu_keyboard_obj = MainMenuKeyboard()
        main_menu_keyboard = main_menu_keyboard_obj.main_menu_keyboard
        UserRuntime.profile_text = answer.text
        DbRequest.update_user_text(UserRuntime.profile_text)
        Message.MSG_DATA = Message.END_REG_STEP + f"\n {UserRuntime.name} {UserRuntime.year}:\n    {UserRuntime.profile_text}"
        TgStateRuntime.tg_state = 8
        DbRequest.update_tg_state(TgStateRuntime.tg_state)
        return (Message.MSG_DATA, main_menu_keyboard, True)

    def main_menu_step_db_worker(next_state: HandlerStates, answer: types.Message):
        main_menu_keyboard_obj = MainMenuKeyboard()
        main_menu_keyboard = main_menu_keyboard_obj.main_menu_keyboard
        return (Message.MAIN_MENU_STEP, main_menu_keyboard, True)
    
    def main_menu_step_action_db_worker(next_state: HandlerStates, answer: types.Message):
        
        if next_state == HandlerStates.SHOW_MY_PROFILE_STEP:
            my_profile_keyboard_obj = MyProfileKeyboard()
            my_profile_keyboard = my_profile_keyboard_obj.my_profile_keyboard
            Message.MSG_DATA = Message.SHOW_MY_PROFILE_STEP + f"\n {UserRuntime.name} {UserRuntime.year}:\n    {UserRuntime.profile_text}"
            return (Message.MSG_DATA, my_profile_keyboard, True)

        elif next_state == HandlerStates.SHOW_HUMAN_PROFILE_STEP:
            like_menu_keyboard_obj = LikeMenuKeyboard()
            like_menu_keyboard = like_menu_keyboard_obj.like_menu_keyboard
            return (Message.SHOW_HUMAN_PROFILE_STEP, like_menu_keyboard, True)

        elif next_state == HandlerStates.FINISH_VIEWING_STEP:
            check_keyboard_obj = CheckKeyboard()
            check_keyboard = check_keyboard_obj.check_keyboard
            return (Message.FINISH_VIEWING_STEP, check_keyboard, True)
        
        elif next_state == HandlerStates.AFFILIATE_PROGRAM_STEP:
            affiliate_program_keyboard_obj = AffiliateProgramKeyboard()
            affiliate_program_keyboard = affiliate_program_keyboard_obj.affiliate_program_keyboard
            return (Message.AFFILIATE_PROGRAM_STEP, affiliate_program_keyboard, True)
        
        elif next_state == HandlerStates.GET_NAME_STEP:
            return (Message.GET_NAME_STEP, None, True)

        elif next_state == HandlerStates.GET_GENDER_STEP:
            return (Message.GET_GENDER_STEP, None, True)

        elif next_state == HandlerStates.GET_AGE_STEP:
            return (Message.GET_AGE_STEP, None, True)
        
        elif next_state == HandlerStates.GET_SCHOOL_STEP:
            return (Message.GET_SCHOOL_STEP, None, True)

        elif next_state == HandlerStates.GET_PHOTO_STEP:
            return (Message.GET_PHOTO_STEP, None, True)

        elif next_state == HandlerStates.GET_TEXT_STEP:
            return (Message.GET_TEXT_STEP, None, True)

        elif next_state == HandlerStates.MAIN_MENU_STEP_WORKER:
            main_menu_keyboard_obj = MainMenuKeyboard()
            main_menu_keyboard = main_menu_keyboard_obj.main_menu_keyboard
            return (Message.INVALID_MSG, main_menu_keyboard, True)

    def show_my_profile_step_db_worker(next_state: HandlerStates, answer: types.Message):
        
        if next_state == HandlerStates.MAIN_MENU_STEP_WORKER:
            main_menu_keyboard_obj = MainMenuKeyboard()
            main_menu_keyboard = main_menu_keyboard_obj.main_menu_keyboard
            return (Message.MAIN_MENU_STEP, main_menu_keyboard, True)
        elif next_state == HandlerStates.GET_PHOTO_STEP:
            return (Message.GET_PHOTO_STEP, None, True)
        elif next_state == HandlerStates.GET_TEXT_STEP:
            return (Message.GET_TEXT_STEP, None, True)
        elif next_state == HandlerStates.GET_NAME_STEP:
            return (Message.GET_NAME_STEP, None, True)
        elif next_state == HandlerStates.SHOW_MY_PROFILE_STEP:
            my_profile_keyboard_obj = MyProfileKeyboard()
            my_profile_keyboard = my_profile_keyboard_obj.my_profile_keyboard
            return (Message.INVALID_MSG, my_profile_keyboard, True)

    def show_human_profile_step_db_worker(next_state: HandlerStates, answer: types.Message):
        if next_state == HandlerStates.SHOW_HUMAN_PROFILE_STEP and answer.text == Condition.SHOW_HUMAN_PROFILE_MENU_LIKE:
            like_menu_keyboard_obj = LikeMenuKeyboard()
            like_menu_keyboard = like_menu_keyboard_obj.like_menu_keyboard
            return (Message.LIKE_HUMAN_PROFILE, like_menu_keyboard, True)
        elif next_state == HandlerStates.SHOW_HUMAN_PROFILE_STEP and answer.text == Condition.SHOW_HUMAN_PROFILE_MENU_DIZZ:
            like_menu_keyboard_obj = LikeMenuKeyboard()
            like_menu_keyboard = like_menu_keyboard_obj.like_menu_keyboard
            return (Message.DIZZ_HUMAN_PROFILE, like_menu_keyboard, True)
        elif next_state == HandlerStates.LIKE_AND_TEXT:
            return (Message.LIKE_AND_TEXT_HUMAN_PROFILE, None, True)
        elif next_state == HandlerStates.MAIN_MENU_STEP_WORKER:
            main_menu_keyboard_obj = MainMenuKeyboard()
            main_menu_keyboard = main_menu_keyboard_obj.main_menu_keyboard
            return (Message.MAIN_MENU_STEP, main_menu_keyboard, True)
        elif next_state == HandlerStates.SHOW_HUMAN_PROFILE_STEP:
            like_menu_keyboard_obj = LikeMenuKeyboard()
            like_menu_keyboard = like_menu_keyboard_obj.like_menu_keyboard
            return (Message.INVALID_MSG, like_menu_keyboard, True)

    def like_and_text_human_profile_step_db_worker(next_state: HandlerStates, answer: types.Message):
        like_menu_keyboard_obj = LikeMenuKeyboard()
        like_menu_keyboard = like_menu_keyboard_obj.like_menu_keyboard
        return (Message.LIKE_HUMAN_PROFILE, like_menu_keyboard, True)

    def affiliate_program_step_db_worker(next_state: HandlerStates, answer: types.Message):
        main_menu_keyboard_obj = MainMenuKeyboard()
        main_menu_keyboard = main_menu_keyboard_obj.main_menu_keyboard
        return (Message.MAIN_MENU_STEP, main_menu_keyboard, True)
    
    def finish_viewing_step_db_worker(next_state: HandlerStates, answer: types.Message):
        if next_state == HandlerStates.NONE:
            return (Message.FINISH_VIEWING_STEP_TRUE, None, True)
        elif next_state == HandlerStates.MAIN_MENU_STEP_WORKER:
            main_menu_keyboard_obj = MainMenuKeyboard()
            main_menu_keyboard = main_menu_keyboard_obj.main_menu_keyboard
            return (Message.MAIN_MENU_STEP, main_menu_keyboard, True)
        

    def show_like_step_db_worker(next_state: HandlerStates, answer: types.Message):
        pass