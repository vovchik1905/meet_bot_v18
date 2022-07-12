from bot_model.app.db.models.db_model import *


def main():
    with db:
        db.create_tables([Telegram, Photo, User, Like, TgState, User_Photo])