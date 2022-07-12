from typing import Any
from aiogram.dispatcher import Dispatcher
from aiogram import types
from bot_model.app.logic.logic import Logic
from bot_model.app.db.db import DbWorker
from bot_model.app.states.handler_states import HandlerStates
from settings.view.commands.commands import BotCommands
from settings.view.messages.messages import Message
from aiogram.dispatcher import FSMContext
from abc import ABC, abstractmethod, abstractproperty

class ViewModel(ABC):
    @abstractmethod
    def __init__(self, dp: Dispatcher, handler_state: HandlerStates, f_logic: Logic,
                f_db: DbWorker) -> None:
        self.dp = dp
        self.handler_state = handler_state
        self.f_logic = f_logic
        self.f_db = f_db
    
    @abstractproperty
    def create(self):
        pass

class CommandViewModel(ViewModel):
    def __init__(self, dp: Dispatcher, handler_state: HandlerStates, f_logic: Logic, f_db: DbWorker, command: BotCommands) -> None:
        super().__init__(dp, handler_state, f_logic, f_db)
        self.command = command
    
    @property
    def create(self):
        """
        """
        @self.dp.message_handler(commands=self.command)
        async def command_view_model(message: types.Message, state: FSMContext):
            """
            """
            async def output(data: Any, keyboard = None) -> None:
                await message.answer(data, reply_markup = keyboard)
            
            #print(message.from_user.id)
            next_state = self.f_logic(message)
            db_data, keyboard, bool_state = self.f_db(next_state, message)
            
            if next_state is self.handler_state:
                if bool_state:
                    await output(db_data, keyboard)
            elif next_state is HandlerStates.NONE:
                if bool_state:
                    await output(db_data, keyboard)
                    await next_state.set() #new
                    await state.finish()
            else:
                if bool_state:
                    await output(db_data, keyboard)
                    await next_state.set()

class StepViewModelMessage(ViewModel):
    """
    """
    def __init__(self, dp: Dispatcher, handler_state: HandlerStates, f_logic: Logic, f_db: DbWorker) -> None:
        super().__init__(dp, handler_state, f_logic, f_db)
    
    @property
    def create(self):
        @self.dp.message_handler(state = self.handler_state)
        async def step_view_model(message: types.Message, state: FSMContext):
            """
            """
            async def output(data: Any, keyboard = None) -> None:
                await message.answer(data, reply_markup = keyboard)
            
            next_state = self.f_logic(message)
            db_data, keyboard, bool_state = self.f_db(next_state, message)
            
            if next_state is self.handler_state:
                if bool_state:
                    if db_data is not None:
                        await output(db_data, keyboard)
            
            elif next_state is HandlerStates.NONE:
                if bool_state:
                    if db_data is not None:
                        await output(db_data, keyboard)
                    await state.finish()
            
            else:
                if bool_state:
                    if db_data is not None:
                        await output(db_data, keyboard)
                    await next_state.set()

class StepViewModelMedia(ViewModel):
    """
    """
    def __init__(self, dp: Dispatcher, handler_state: HandlerStates, f_logic: Logic, f_db: DbWorker) -> None:
        super().__init__(dp, handler_state, f_logic, f_db)
    
    @property
    def create(self):
        @self.dp.message_handler(state = self.handler_state, content_types = types.ContentType.PHOTO)
        async def step_view_model(message: types.Message, state: FSMContext):
            """
            """
            async def output(data: Any, keyboard = None) -> None:
                await message.answer(data, reply_markup = keyboard)
            
            next_state = self.f_logic(message)
            db_data, keyboard, bool_state = self.f_db(next_state, message)
            
            if next_state is self.handler_state:
                if bool_state:
                    if db_data is not None:
                        await output(db_data, keyboard)
            
            elif next_state is HandlerStates.NONE:
                if bool_state:
                    if db_data is not None:
                        await output(db_data, keyboard)
                    await state.finish()
            
            else:
                if bool_state:
                    if db_data is not None:
                        await output(db_data, keyboard)
                    await next_state.set()