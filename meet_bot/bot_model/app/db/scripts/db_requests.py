from typing import Any
import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from bot_model.app.db.models.db_model import *
from settings.db.db_config import DbConfig
from bot_model.app.db.object_model import *


class DbRequest:
    """
    """
    
    @staticmethod
    def update_tg_state(tg_state: int):
        with db:
            update_tg_states = TgState.get(TgState.id == TgStateRuntime.id)
            update_tg_states.tg_state = tg_state
            update_tg_states.save()
    
    @staticmethod
    def update_user_name(user_name: str):
        with db:
            updete_user_name = User.get(User.id == UserRuntime.id)
            updete_user_name.name = user_name
            updete_user_name.save()
    
    @staticmethod
    def update_user_gender(user_gender: int):
        with db:
            updete_user_gender = User.get(User.id == UserRuntime.id)
            updete_user_gender.gender = user_gender
            updete_user_gender.save()
    
    @staticmethod
    def update_user_year(user_year: int):
        with db:
            updete_user_year = User.get(User.id == UserRuntime.id)
            updete_user_year.year = user_year
            updete_user_year.save()
    
    @staticmethod
    def update_user_school(user_school: str):
        with db:
            updete_user_school = User.get(User.id == UserRuntime.id)
            updete_user_school.school = user_school
            updete_user_school.save()
    
    @staticmethod
    def create_photo(photo_tg_id: str):
        with db:
            create_photo = Photo(foto_tg_id = PhotoRuntime.foto_tg_id)
            PhotoRuntime.id = create_photo.save()
    
    @staticmethod
    def update_user_text(user_text: str):
        with db:
            updete_user_profile_text = User.get(User.id == UserRuntime.id)
            updete_user_profile_text.profile_text = UserRuntime.profile_text
            updete_user_profile_text.save()