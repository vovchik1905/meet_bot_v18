import asyncio
from typing import Any
from xmlrpc.client import Boolean
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram import types
from settings.view.messages.messages import Message

from bot_model.app.states.handler_states import HandlerStates
from bot_model.app.logic.logic import Logic
from bot_model.app.db.db import DbWorker
from bot_model.app.views.views import View
from settings.view.commands.commands import BotCommands

from abc import ABC, abstractmethod, abstractproperty


class HandlerModel(ABC):
    """
    Parents:
        ABC
    Description:
        Абстрактный класс, является моделью для CommandModel и StepModel.
    """
    @abstractmethod
    def __init__(self, dp: Dispatcher, handler_state: HandlerStates, f_view: View, 
                f_logic: Logic, f_db: DbWorker) -> None:
        """
        Parameters:
            handler_state: HandlerStates
            dp: Dispatcher
            f_view: View
            f_logic: Logic
            f_db: DbWorker
        ------------------
        Returns:
            None
        ------------------
        Description:
            Абстрактый конструктор HandlerModel.
        """
        self.dp = dp
        self.handler_state = handler_state
        self.f_view = f_view
        self.f_logic = f_logic
        self.f_db = f_db
    
    @abstractproperty
    def action(self):
        pass


class CommandModel(HandlerModel):
    """
    Parents:
        HandlerModel
    Description:
        Класс - модель команд тг боту.
    """    
    def __init__(self, dp: Dispatcher, handler_state: HandlerStates,
                f_view: View, f_logic: Logic, f_db: DbWorker,
                command: BotCommands) -> None:
        """
        """
        super().__init__(dp, handler_state, f_view, f_logic, f_db)
        self.command = command

    @property
    def action(self):
        self.f_view(self.dp, self.handler_state, self.f_logic, self.f_db, self.command)


class StepModel(HandlerModel):
    """
    Parents:
        HandlerModel
    Description:
        Класс - модель шага тг бота.
    """
    def __init__(self, dp: Dispatcher, handler_state: HandlerStates,
                f_view: View, f_logic: Logic, f_db: DbWorker) -> None:
        """
        """
        super().__init__(dp, handler_state, f_view, f_logic, f_db)

    @property
    def action(self):
        """
        """
        self.f_view(self.dp, self.handler_state, self.f_logic, self.f_db)