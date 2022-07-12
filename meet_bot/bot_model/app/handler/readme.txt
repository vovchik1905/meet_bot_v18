from aiogram.dispatcher import Dispatcher

from settings.view.messages.messages import Message
from settings.view.commands.commands import BotCommands
from settings.view.keyboards.keyboards import Keyboard_heading
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

    def __init__(self, handler_state: HandlerStates, dp: Dispatcher, f_view: View, f_logic: Logic, f_db: DbWorker) -> None:
        self.handler_state = handler_state
        self.dp = dp
        self.f_view = f_view
        self.f_logic = f_logic
        self.f_db = f_db

    @property
    def start_command(self, command: BotCommands) -> None:
        start_command = CommandModel(self.handler_state, self.dp, self.f_view, self.f_logic, self.f_db, command)
        start_command.action

    @property
    def help_command(self, command: BotCommands) -> None:
        help_command = CommandModel(self.handler_state, self.dp, self.f_view, self.f_logic, self.f_db, command)
        help_command.action

    @property
    def reg_command(self, command: BotCommands) -> None:
        reg_command = CommandModel(self.handler_state, self.dp, self.f_view, self.f_logic, self.f_db, command)
        reg_command.action

    @property
    def show_command(self, command: BotCommands) -> None:
        show_command = CommandModel(self.handler_state, self.dp, self.f_view, self.f_logic, self.f_db, command)
        show_command.action

    @property
    def main_menu_command(self, command: BotCommands) -> None:
        main_menu_command = CommandModel(self.handler_state, self.dp, self.f_view, self.f_logic, self.f_db, command)
        main_menu_command.action

    @property
    def show_my_profile_command(self, command: BotCommands) -> None:
        show_my_profile_command = CommandModel(self.handler_state, self.dp, self.f_view, self.f_logic, self.f_db, command)
        show_my_profile_command.action

    @property
    def show_human_profile_command(self, command: BotCommands) -> None:
        show_human_profile_command = CommandModel(self.handler_state, self.dp, self.f_view, self.f_logic, self.f_db, command)
        show_human_profile_command.action
    
    @property
    def show_like_command(self, command: BotCommands) -> None:
        show_like_command = CommandModel(self.handler_state, self.dp, self.f_view, self.f_logic, self.f_db, command)
        show_like_command.action

    #---------------------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------

    @property
    def get_name_step(self) -> None:
        get_name_step = StepModel(self.handler_state, self.dp, self.f_view, self.f_logic, self.f_db)
        get_name_step.action

    @property
    def get_gender_step(self) -> None:
        get_gender_step = StepModel(self.handler_state, self.dp, self.f_view, self.f_logic, self.f_db)
        get_gender_step.action
    
    @property
    def get_age_step(self) -> None:
        get_age_step = StepModel(self.handler_state, self.dp, self.f_view, self.f_logic, self.f_db)
        get_age_step.action
    
    @property
    def get_school_step(self) -> None:
        get_school_step = StepModel(self.handler_state, self.dp, self.f_view, self.f_logic, self.f_db)
        get_school_step.action
    
    @property
    def get_photo_step(self) -> None:
        get_photo_step = StepModel(self.handler_state, self.dp, self.f_view, self.f_logic, self.f_db)
        get_photo_step.action
    
    @property
    def main_menu_step(self) -> None:
        main_menu_step = StepModel(self.handler_state, self.dp, self.f_view, self.f_logic, self.f_db)
        main_menu_step.action
    
    @property
    def show_my_profile_step(self) -> None:
        show_my_profile_step = StepModel(self.handler_state, self.dp, self.f_view, self.f_logic, self.f_db)
        show_my_profile_step.action
    
    @property
    def show_human_profile_step(self) -> None:
        show_human_profile_step = StepModel(self.handler_state, self.dp, self.f_view, self.f_logic, self.f_db)
        show_human_profile_step.action
    
    @property
    def show_like_step(self) -> None:
        show_like_step = StepModel(self.handler_state, self.dp, self.f_view, self.f_logic, self.f_db)
        show_like_step.action