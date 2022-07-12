from typing import Any


class TelegramRuntime:
    id: Any
    tg_id: int
    tg_name: str
    tg_sername: str
    tg_username: str

class PhotoRuntime:
    id: Any
    foto_tg_id: str
    foto_extension: str

class UserRuntime:
    id: Any
    telegram: int
    name: str
    gender: int
    year: int
    school: str
    profile_text: str
    state: int
    status: float

class UserPhotoRuntime:
    id: Any
    user_id: int
    photo_id: int

class LikeRuntime:
    id: Any
    from_user_id: int
    for_user_id: int
    state: int
    data: Any

class TgStateRuntime:
    id: Any
    user_id: int
    tg_state: int