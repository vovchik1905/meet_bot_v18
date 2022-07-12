from typing import Any
from aiogram import types
from bot_model.app.states.handler_states import HandlerStates
from settings.logic.condition.conditions import Condition
from bot_model.app.db.object_model import *

class Logic:
    """
    Класс логики команд и шагов.
    """
    @staticmethod
    def start_command_logic(answer: types.Message) -> HandlerStates:
        """
        """
        return HandlerStates.MAIN_MENU_STEP_WORKER
    
    @staticmethod
    def help_command_logic(answer: types.Message) -> HandlerStates:
        """
        """
        return HandlerStates.HELP_COMMAND
    
    @staticmethod
    def reg_command_logic(answer: types.Message) -> HandlerStates:
        """
        """
        if UserRuntime.state == 1:
            return HandlerStates.NONE
        return HandlerStates.GET_NAME_STEP
    
    @staticmethod
    def main_menu_step_logic(answer: types.Message) -> HandlerStates:
        """
        """
        return HandlerStates.MAIN_MENU_STEP_WORKER
    
    @staticmethod
    def get_name_step_logic(answer: types.Message) -> HandlerStates:
        """
        """
        return HandlerStates.GET_GENDER_STEP
    
    @staticmethod
    def get_gender_step_logic(answer: types.Message) -> HandlerStates:
        """
        """
        gender = answer.text
        if gender == Condition.GENDER_MAN_VALUE or gender == Condition.GENDER_HUMAN_VALUE:
            return HandlerStates.GET_AGE_STEP
        return HandlerStates.GET_GENDER_STEP
    
    @staticmethod
    def get_age_step_logic(answer: types.Message) -> HandlerStates:
        """
        """
        age = answer.text
        if age.isdigit():
            if int(age) >= Condition.AGE_LOW_LIMIT and int(age) <= Condition.AGE_HIGH_LIMIT:
                return HandlerStates.GET_SCHOOL_STEP
        return HandlerStates.GET_AGE_STEP
    
    @staticmethod
    def get_school_step_logic(answer: types.Message) -> HandlerStates:
        """
        """
        school_value = answer.text
        if school_value in Condition.SCHOOL_ARR:
            return HandlerStates.GET_PHOTO_STEP
        return HandlerStates.GET_SCHOOL_STEP
    
    def get_photo_step_logic(answer: types.Message) -> HandlerStates:
        """
        """
        return HandlerStates.GET_TEXT_STEP
    
    def get_text_step_logic(answer: types.Message) -> HandlerStates:
        """
        """
        return HandlerStates.MAIN_MENU_STEP_WORKER
    
    def main_menu_step_worker_logic(answer: types.Message) -> HandlerStates:
        keyboard_value = answer.text
        
        if keyboard_value == Condition.MAIN_MENU_SHOW_MY_PROFILE:
            
            if TgStateRuntime.tg_state >= 8:
                return HandlerStates.SHOW_MY_PROFILE_STEP
            
            elif TgStateRuntime.tg_state == 7:
                return HandlerStates.GET_TEXT_STEP
            
            elif TgStateRuntime.tg_state == 6:
                return HandlerStates.GET_PHOTO_STEP
            
            elif TgStateRuntime.tg_state == 5:
                return HandlerStates.GET_SCHOOL_STEP
            
            elif TgStateRuntime.tg_state == 4:
                return HandlerStates.GET_AGE_STEP
            
            elif TgStateRuntime.tg_state == 3:
                return HandlerStates.GET_GENDER_STEP
            
            elif TgStateRuntime.tg_state == 2:
                return HandlerStates.GET_NAME_STEP

        elif keyboard_value == Condition.MAIN_MENU_SHOW_HUMAN_PROFILE:
            return HandlerStates.SHOW_HUMAN_PROFILE_STEP
        elif keyboard_value == Condition.MAIN_MENU_FINISH_VIEWING:
            return HandlerStates.FINISH_VIEWING_STEP
        elif keyboard_value == Condition.MAIN_MENU_AFFILIATE_PROGRAM:
            return HandlerStates.AFFILIATE_PROGRAM_STEP
        #elif keyboard_value == Condition.HELP_COMMAND:
        #    pass
        else:
            return HandlerStates.MAIN_MENU_STEP_WORKER
    
    def show_my_profile_step_logic(answer: types.Message) -> HandlerStates:
        keyboard_value = answer.text
        if keyboard_value == Condition.MAIN_MENU:
            return HandlerStates.MAIN_MENU_STEP_WORKER
        elif keyboard_value == Condition.CHANGE_MY_PHOTO:
            return HandlerStates.GET_PHOTO_STEP
        elif keyboard_value == Condition.CHANGE_MY_TEXT:
            return HandlerStates.GET_TEXT_STEP
        elif keyboard_value == Condition.REG_MY_PROFILE:
            return HandlerStates.GET_NAME_STEP
        else:
            return HandlerStates.SHOW_MY_PROFILE_STEP
    
    def show_human_profile_step_logic(answer: types.Message) -> HandlerStates:
        keyboard_value = answer.text
        if keyboard_value == Condition.SHOW_HUMAN_PROFILE_MENU_LIKE:
            return HandlerStates.SHOW_HUMAN_PROFILE_STEP
        elif keyboard_value == Condition.SHOW_HUMAN_PROFILE_MENU_DIZZ:
            return HandlerStates.SHOW_HUMAN_PROFILE_STEP
        elif keyboard_value == Condition.SHOW_HUMAN_PROFILE_MENU_LIKE_AND_TEXT:
            return HandlerStates.LIKE_AND_TEXT
        elif keyboard_value == Condition.MAIN_MENU:
            return HandlerStates.MAIN_MENU_STEP_WORKER
        else:
            return HandlerStates.SHOW_HUMAN_PROFILE_STEP
    
    def like_and_text_human_profile_step_logic(answer: types.Message) -> HandlerStates:
        return HandlerStates.SHOW_HUMAN_PROFILE_STEP
    
    def affiliate_program_step_logic(answer: types.Message) -> HandlerStates:
        return HandlerStates.MAIN_MENU_STEP_WORKER
    
    def finish_viewing_step_logic(answer: types.Message) -> HandlerStates:
        keyboard_value = answer.text
        if keyboard_value == Condition.CHECK_YES:
            return HandlerStates.NONE
        elif keyboard_value == Condition.CHECK_NO:
            return HandlerStates.MAIN_MENU_STEP_WORKER