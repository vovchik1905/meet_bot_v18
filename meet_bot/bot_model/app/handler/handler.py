from aiogram.dispatcher import Dispatcher

from settings.view.messages.messages import Message
from settings.view.commands.commands import BotCommands
from settings.view.keyboards.keyboards import ButtonHeading
from settings.logic.condition.conditions import Condition
from bot_model.app.handler.handler_model import CommandModel, StepModel
from bot_model.app.views.views import View
from bot_model.app.logic.logic import Logic
from bot_model.app.db.db import DbWorker
from bot_model.app.states.handler_states import HandlerStates

class Handler:
    """
    Parents:
        None
    Description:
        В классе создаются объекты CommandModel и StepModel.
    """

    def __init__(self, dp: Dispatcher) -> None:
        self.dp = dp

    @property
    def start_command(self) -> None:
        start_command = CommandModel(self.dp, HandlerStates.START_COMMAND,
                                    View.start_command_view, Logic.start_command_logic,
                                    DbWorker.start_command_db_worker, BotCommands.START_COMMAND)
        start_command.action
    
    @property
    def help_command(self) -> None:
        help_command = CommandModel(self.dp, HandlerStates.HELP_COMMAND,
                                    View.help_command_view, Logic.help_command_logic,
                                    DbWorker.help_command_db_worker, BotCommands.HELP_COMMAND)
        help_command.action
    
    @property
    def reg_command(self) -> None:
        reg_command = CommandModel(self.dp, HandlerStates.REG_COMMAND,
                                    View.reg_command_view, Logic.reg_command_logic,
                                    DbWorker.reg_command_db_worker, BotCommands.REG_COMMAND)
        reg_command.action
    
    @property
    def main_menu_command(self) -> None:
        main_menu_command = CommandModel(self.dp, HandlerStates.MAIN_MENU_STEP,
                                    View.main_menu_command_view, Logic.main_menu_step_logic,
                                    DbWorker.main_menu_step_db_worker, BotCommands.MAIN_MENU)
        main_menu_command.action
    
    @property
    def get_name_step(self) -> None:
        get_name_step = StepModel(self.dp, HandlerStates.GET_NAME_STEP,
                                View.get_name_step_view, Logic.get_name_step_logic,
                                DbWorker.get_name_step_db_worker)
        get_name_step.action
    
    @property
    def get_gender_step(self) -> None:
        get_gender_step = StepModel(self.dp, HandlerStates.GET_GENDER_STEP,
                                View.get_gender_step_view, Logic.get_gender_step_logic,
                                DbWorker.get_gender_step_db_worker)
        get_gender_step.action
    
    @property
    def get_age_step(self) -> None:
        get_age_step = StepModel(self.dp, HandlerStates.GET_AGE_STEP,
                                View.get_age_step_view, Logic.get_age_step_logic,
                                DbWorker.get_age_step_db_worker)
        get_age_step.action
    
    @property
    def get_school_step(self) -> None:
        get_age_step = StepModel(self.dp, HandlerStates.GET_SCHOOL_STEP,
                                View.get_school_step_view, Logic.get_school_step_logic,
                                DbWorker.get_school_step_db_worker)
        get_age_step.action
    
    @property
    def get_photo_step(self) -> None:
        get_photo_step = StepModel(self.dp, HandlerStates.GET_PHOTO_STEP,
                                View.get_photo_step_view, Logic.get_photo_step_logic,
                                DbWorker.get_photo_step_db_worker)
        get_photo_step.action
    
    @property
    def get_text_step(self) -> None:
        get_text_step = StepModel(self.dp, HandlerStates.GET_TEXT_STEP,
                                View.get_text_step_view, Logic.get_text_step_logic,
                                DbWorker.get_text_step_db_worker)
        get_text_step.action

    @property
    def main_menu_step(self) -> None:
        get_photo_step = StepModel(self.dp, HandlerStates.MAIN_MENU_STEP,
                                View.main_menu_step_view, Logic.main_menu_step_logic,
                                DbWorker.main_menu_step_db_worker)
        get_photo_step.action
    
    @property
    def main_menu_step_worker(self) -> None:
        get_photo_step = StepModel(self.dp, HandlerStates.MAIN_MENU_STEP_WORKER,
                                View.main_menu_step_worker_view, Logic.main_menu_step_worker_logic,
                                DbWorker.main_menu_step_action_db_worker)
        get_photo_step.action
    
    @property
    def show_my_profile_step_worker(self) -> None:
        show_my_profile_step = StepModel(self.dp, HandlerStates.SHOW_MY_PROFILE_STEP,
                                View.show_my_profile_step_view, Logic.show_my_profile_step_logic,
                                DbWorker.show_my_profile_step_db_worker)
        show_my_profile_step.action
    
    @property
    def show_human_profile_step_worker(self) -> None:
        show_human_profile_step = StepModel(self.dp, HandlerStates.SHOW_HUMAN_PROFILE_STEP,
                                View.show_human_profile_step_view, Logic.show_human_profile_step_logic,
                                DbWorker.show_human_profile_step_db_worker)
        show_human_profile_step.action
    
    @property
    def like_and_text_human_profile_step(self) -> None:
        like_and_text_step = StepModel(self.dp, HandlerStates.LIKE_AND_TEXT,
                                View.like_and_text_human_profile_step, Logic.like_and_text_human_profile_step_logic,
                                DbWorker.like_and_text_human_profile_step_db_worker)
        like_and_text_step.action
    
    @property
    def affiliate_program_step(self) -> None:
        affiliate_program_step = StepModel(self.dp, HandlerStates.AFFILIATE_PROGRAM_STEP,
                                View.affiliate_program_step, Logic.affiliate_program_step_logic,
                                DbWorker.affiliate_program_step_db_worker)
        affiliate_program_step.action
    
    @property
    def finish_viewing_step(self) -> None:
        finish_viewing_step = StepModel(self.dp, HandlerStates.FINISH_VIEWING_STEP,
                                View.finish_viewing_step, Logic.finish_viewing_step_logic,
                                DbWorker.finish_viewing_step_db_worker)
        finish_viewing_step.action