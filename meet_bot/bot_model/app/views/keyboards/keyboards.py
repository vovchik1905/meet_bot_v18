import profile
from settings.view.keyboards.keyboards import ButtonHeading, ResizeKeyboard, OneTimeKeyboard
from bot_model.app.views.keyboards.callback_data import CallbackData
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

class GenderKeyboard:
    def __init__(self) -> None:
        self.man_button = KeyboardButton(ButtonHeading.MAN)
        self.human_button = KeyboardButton(ButtonHeading.HUMAN)
        
        self.gender_keyboard = ReplyKeyboardMarkup(resize_keyboard = ResizeKeyboard.GENDER_KEYBOARD,
                                                    one_time_keyboard = OneTimeKeyboard.GENDER_KEYBOARD)
        
        self.gender_keyboard.row(self.man_button, self.human_button)

class SchoolKeyboard:
    def __init__(self) -> None:
        self.first_school = KeyboardButton(ButtonHeading.SCHOOL_FIRST)
        self.second_school = KeyboardButton(ButtonHeading.SCHOOL_SECOND)
        self.third_school = KeyboardButton(ButtonHeading.SCHOOL_THIRD)
        self.fourth_school = KeyboardButton(ButtonHeading.SCHOOL_FOURTH)
        self.fifth_school = KeyboardButton(ButtonHeading.SCHOOL_FIFTH)
        self.sixth_school = KeyboardButton(ButtonHeading.SCHOOL_SIXTH)
        self.seventh_school = KeyboardButton(ButtonHeading.SCHOOL_SEVENTH)
        self.eigth_school = KeyboardButton(ButtonHeading.SCHOOL_EIGHTH)
        

        self.school_keyboard = ReplyKeyboardMarkup(resize_keyboard = ResizeKeyboard.SCHOOL_KEYBOARD,
                                                    one_time_keyboard = OneTimeKeyboard.SCHOOL_KEYBOARD)
        
        self.school_keyboard.row(self.first_school, self.second_school, self.third_school, self.fourth_school)
        self.school_keyboard.row(self.fifth_school, self.sixth_school, self.seventh_school, self.eigth_school)

class MainMenuKeyboard:
    def __init__(self) -> None:
        self.show_human_profile = KeyboardButton(ButtonHeading.SHOW_HUMAN_PROFILE)
        self.show_my_profile = KeyboardButton(ButtonHeading.SHOW_MY_PROFILE)
        self.finish_viewing = KeyboardButton(ButtonHeading.FINISH_VIEWING)
        self.affiliate_program = KeyboardButton(ButtonHeading.AFFILIATE_PROGRAM)
        self.main_menu_keyboard = ReplyKeyboardMarkup(resize_keyboard = ResizeKeyboard.MAIN_MENU_KEYBOARD,
                                                        one_time_keyboard = OneTimeKeyboard.MAIN_MENU_KEYBOARD)
        self.main_menu_keyboard.row(self.show_human_profile,
                                    self.show_my_profile,
                                    self.finish_viewing,
                                    self.affiliate_program)

class LikeMenuKeyboard:
    def __init__(self) -> None:
        self.like_profile = KeyboardButton(ButtonHeading.LIKE)
        self.dizlike_profile = KeyboardButton(ButtonHeading.DIZZ)
        self.like_and_text_profile = KeyboardButton(ButtonHeading.LIKE_AND_TEXT)
        self.main_menu = KeyboardButton(ButtonHeading.MAIN_MENU)
        self.like_menu_keyboard = ReplyKeyboardMarkup(resize_keyboard = ResizeKeyboard.LIKE_MENU_KEYBOARD,
                                                        one_time_keyboard = OneTimeKeyboard.LIKE_MENU_KEYBOARD)
        self.like_menu_keyboard.row(self.like_profile,
                                    self.dizlike_profile,
                                    self.like_and_text_profile,
                                    self.main_menu)

class MyProfileKeyboard:
    def __init__(self) -> None:
        self.reg_my_profile = KeyboardButton(ButtonHeading.REG_MY_PROFILE)
        self.change_my_photo = KeyboardButton(ButtonHeading.CHANGE_MY_PHOTO)
        self.change_my_text = KeyboardButton(ButtonHeading.CHANGE_MY_TEXT)
        self.main_menu = KeyboardButton(ButtonHeading.MAIN_MENU)
        self.my_profile_keyboard = ReplyKeyboardMarkup(resize_keyboard = ResizeKeyboard.MY_PROFILE_KEYBOARD,
                                                        one_time_keyboard = OneTimeKeyboard.MY_PROFILE_KEYBOARD)
        self.my_profile_keyboard.row(self.reg_my_profile,
                                    self.change_my_photo,
                                    self.change_my_text,
                                    self.main_menu)

class AffiliateProgramKeyboard:
    def __init__(self) -> None:
        self.back = KeyboardButton(ButtonHeading.BACK_BUTTON)
        self.affiliate_program_keyboard = ReplyKeyboardMarkup(resize_keyboard = ResizeKeyboard.AFFILIATE_PROGRAM_KEYBOARD,
                                                        one_time_keyboard = OneTimeKeyboard.AFFILIATE_PROGRAM_KEYBOARD)
        self.affiliate_program_keyboard.add(self.back)

class CheckKeyboard:
    def __init__(self) -> None:
        self.yes = KeyboardButton(ButtonHeading.YES_BUTTON)
        self.no = KeyboardButton(ButtonHeading.NO_BUTTON)
        self.check_keyboard = ReplyKeyboardMarkup(resize_keyboard = ResizeKeyboard.AFFILIATE_PROGRAM_KEYBOARD,
                                                        one_time_keyboard = OneTimeKeyboard.AFFILIATE_PROGRAM_KEYBOARD)
        self.check_keyboard.row(self.yes, self.no)

#class ShowHumanProfile:
#    def __init__(self) -> None:
#        self.main_menu = KeyboardButton(ButtonHeading.MAIN_MENU)