from email.policy import default
from peewee import *
from enum import Enum, IntEnum
import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from settings.db.db_config import DbConfig


db = PostgresqlDatabase(database=DbConfig.DATABAZE,
                        user=DbConfig.USER,
                        password=DbConfig.PASSWORD,
                        host=DbConfig.HOST,
                        port=DbConfig.PORT)


class UserState(IntEnum):
    BAN = 1
    NEW = 2
    REGULAR = 3
    VIP = 4
    ADMIN = 5


class TgState(IntEnum):
    START_COMMAND = 1
    GET_NAME_STEP = 2
    GET_GENDER_STEP = 3
    GET_AGE_STEP = 4
    GET_SCHOOL_STEP = 5
    GET_PHOTO_STEP = 6
    GET_PROFILE_TEXT_STEP = 7
    END_REG_STEP = 8
    SHOW_HUMAN_PROFILE_STEP = 9
    SHOW_LIKE_STEP = 10


class GenderState(IntEnum):
    MALE = 1
    FEMALE = 2
    UNKNOWN = 3


class LikeState(IntEnum):
    NEW = 1
    DELIVERED = 2


class BaseModel(Model):
    id = PrimaryKeyField(unique=True)

    class Meta:
        database = db
        order = 'id'


class Telegram(BaseModel):
    tg_id = IntegerField()
    tg_name = CharField(default=None, null=True)
    tg_sername = CharField(default=None, null=True)
    tg_username = CharField(default=None, null=True)

    class Meta:
        db_table = 'Telegram'


class Photo(BaseModel):
    foto_tg_id = CharField(default=None)
    foto_extension = CharField(default=None, null=True)

    class Meta:
        db_table = 'Photos'


class User(BaseModel):
    telegram = ForeignKeyField(Telegram)
    name = CharField(default=None, null=True)
    gender = IntegerField(default=None, null=True) #значение соответствует GenderState
    year = IntegerField(default=None, null=True)
    school = CharField(default=None, null=True)
    profile_text = CharField(default=None, null=True)
    state = IntegerField(default=None, null=True) #значение соответствует UserState
    status = FloatField(default=None, null=True)

    class Meta:
        db_table = 'Users'


class User_Photo(BaseModel):
    user_id = ForeignKeyField(User)
    photo_id = ForeignKeyField(Photo)

    class Meta:
        db_table = 'Users_Photos'


class Like(BaseModel):
    from_user_id = ForeignKeyField(User)
    for_user_id = ForeignKeyField(User)
    state = IntegerField() #значение соответствует LikeState
    data = DateTimeField()

    class Meta:
        db_table = 'Likes'


class TgState(BaseModel):
    user_id = ForeignKeyField(User)
    tg_state = IntegerField(default=None) #значение соответствует TgState

    class Meta:
        db_table = 'TgStates'
