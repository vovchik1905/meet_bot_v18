from typing import Any
from bot_model.model.baze_model import BazeBotModel
from aiogram.dispatcher import Dispatcher
from aiogram import Bot
from bot_model.app.handler.handler import Handler

class MainBotModel(BazeBotModel):
    def __init__(self, bot_token: str, bot_url: str, bot_name: str, bot_tg_link: str, storage: Any, *args, **kwargs) -> None:
        super().__init__(bot_token, bot_url, bot_name, bot_tg_link, storage)
    
    @property
    def action(self):
        MeetBotHandler = Handler(self.dp)
        MeetBotHandler.start_command
        MeetBotHandler.help_command
        MeetBotHandler.reg_command
        MeetBotHandler.main_menu_command
        MeetBotHandler.get_name_step
        MeetBotHandler.get_gender_step
        MeetBotHandler.get_age_step
        MeetBotHandler.get_school_step
        MeetBotHandler.get_photo_step
        MeetBotHandler.get_text_step
        MeetBotHandler.main_menu_step
        MeetBotHandler.main_menu_step_worker
        MeetBotHandler.show_my_profile_step_worker
        MeetBotHandler.show_human_profile_step_worker
        MeetBotHandler.like_and_text_human_profile_step
        MeetBotHandler.affiliate_program_step
        MeetBotHandler.finish_viewing_step