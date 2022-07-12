from typing import Any
from aiogram.dispatcher import Dispatcher
from aiogram import types
from bot_model.app.logic.logic import Logic
from bot_model.app.db.db import DbWorker
from bot_model.app.states.handler_states import HandlerStates
from settings.view.commands.commands import BotCommands
from settings.view.messages.messages import Message
from aiogram.dispatcher import FSMContext
from bot_model.app.views.views_model import CommandViewModel, StepViewModelMessage, StepViewModelMedia

from bot_model.app.views.keyboards.keyboards import GenderKeyboard, SchoolKeyboard

class View:
    """
    Description:
        Класс для работы с фронтом тг.
    """

    def start_command_view(dp: Dispatcher, handler_state: HandlerStates, f_logic: Logic, f_db: DbWorker, command: BotCommands) -> None:
        start_command = CommandViewModel(dp, handler_state, f_logic, f_db, command)
        start_command.create
    
    def help_command_view(dp: Dispatcher, handler_state: HandlerStates, f_logic: Logic, f_db: DbWorker, command: BotCommands) -> None:
        #help_command = CommandViewModel(dp, handler_state, f_logic, f_db, command)
        #help_command.create
        #@dp.message_handler(commands=command)
        #async def command_view_model(message: types.Message, state: FSMContext):
        pass
    
    def reg_command_view(dp: Dispatcher, handler_state: HandlerStates, f_logic: Logic, f_db: DbWorker, command: BotCommands) -> None:
        #reg_command = CommandViewModel(dp, handler_state, f_logic, f_db, command)
        #reg_command.create
        pass
    
    def main_menu_command_view(dp: Dispatcher, handler_state: HandlerStates, f_logic: Logic, f_db: DbWorker, command: BotCommands) -> None:
        #main_menu_command = CommandViewModel(dp, handler_state, f_logic, f_db, command)
        #main_menu_command.create
        pass
    
    def get_name_step_view(dp: Dispatcher, handler_state: HandlerStates, f_logic: Logic, f_db: DbWorker) -> None:
        get_name_step = StepViewModelMessage(dp, handler_state, f_logic, f_db)
        get_name_step.create

    def get_gender_step_view(dp: Dispatcher, handler_state: HandlerStates, f_logic: Logic, f_db: DbWorker) -> None:
        get_gender_step = StepViewModelMessage(dp, handler_state, f_logic, f_db)
        get_gender_step.create
    
    def get_age_step_view(dp: Dispatcher, handler_state: HandlerStates, f_logic: Logic, f_db: DbWorker) -> None:
        get_age_step = StepViewModelMessage(dp, handler_state, f_logic, f_db)
        get_age_step.create
    
    def get_school_step_view(dp: Dispatcher, handler_state: HandlerStates, f_logic: Logic, f_db: DbWorker) -> None:
        get_school_step = StepViewModelMessage(dp, handler_state, f_logic, f_db)
        get_school_step.create
    
    def get_photo_step_view(dp: Dispatcher, handler_state: HandlerStates, f_logic: Logic, f_db: DbWorker) -> None:
        get_photo_step = StepViewModelMedia(dp, handler_state, f_logic, f_db)
        get_photo_step.create
    
    def get_text_step_view(dp: Dispatcher, handler_state: HandlerStates, f_logic: Logic, f_db: DbWorker) -> None:
        get_text_step = StepViewModelMessage(dp, handler_state, f_logic, f_db)
        get_text_step.create
    
    def main_menu_step_view(dp: Dispatcher, handler_state: HandlerStates, f_logic: Logic, f_db: DbWorker) -> None:
        main_menu_command = StepViewModelMessage(dp, handler_state, f_logic, f_db)
        main_menu_command.create
    
    def main_menu_step_worker_view(dp: Dispatcher, handler_state: HandlerStates, f_logic: Logic, f_db: DbWorker) -> None:
        main_menu_step_worker = StepViewModelMessage(dp, handler_state, f_logic, f_db)
        main_menu_step_worker.create
    
    def show_my_profile_step_view(dp: Dispatcher, handler_state: HandlerStates, f_logic: Logic, f_db: DbWorker) -> None:
        show_my_profile_step = StepViewModelMessage(dp, handler_state, f_logic, f_db)
        show_my_profile_step.create
    
    def show_human_profile_step_view(dp: Dispatcher, handler_state: HandlerStates, f_logic: Logic, f_db: DbWorker) -> None:
        show_my_profile_step = StepViewModelMessage(dp, handler_state, f_logic, f_db)
        show_my_profile_step.create
    
    def like_and_text_human_profile_step(dp: Dispatcher, handler_state: HandlerStates, f_logic: Logic, f_db: DbWorker) -> None:
        like_and_text_human_profile_step = StepViewModelMessage(dp, handler_state, f_logic, f_db)
        like_and_text_human_profile_step.create
    
    def affiliate_program_step(dp: Dispatcher, handler_state: HandlerStates, f_logic: Logic, f_db: DbWorker) -> None:
        affiliate_program_step = StepViewModelMessage(dp, handler_state, f_logic, f_db)
        affiliate_program_step.create
    
    def finish_viewing_step(dp: Dispatcher, handler_state: HandlerStates, f_logic: Logic, f_db: DbWorker) -> None:
        finish_viewing_step = StepViewModelMessage(dp, handler_state, f_logic, f_db)
        finish_viewing_step.create
