from bot_model.model.main_model import MainBotModel
from settings.private.bot_config import BotConfig
from aiogram.contrib.fsm_storage.memory import MemoryStorage

def MeetBot():
    storage = MemoryStorage()
    MeetBot = MainBotModel(BotConfig.TOKEN, BotConfig.URL, BotConfig.NAME, BotConfig.TG_LINK, storage)
    MeetBot.action
    MeetBot.start