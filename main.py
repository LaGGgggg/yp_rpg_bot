from logging import basicConfig, error, INFO
from pathlib import Path
from os import environ
from dotenv import load_dotenv
from random import choice, shuffle
from copy import deepcopy

from telebot import TeleBot, types

from user_info import UserInfoManager
from app_dataclasses import Level, Location
from levels import LEVELS


BOT_TOKEN: str


def set_up() -> bool:

    global BOT_TOKEN, AVATAR_URL

    # Logging:
    basicConfig(level=INFO)

    # Environment variables:

    dotenv_path = Path(__file__).resolve().parent / '.env'

    load_dotenv(dotenv_path)

    BOT_TOKEN = environ.get('BOT_TOKEN', default=None)

    if not BOT_TOKEN:

        error('BOT_TOKEN environment variable is not set!')

        return False

    return True


def run_bot() -> None:

    choice_prefix = 'question_choice_'
    choice_ids_divider = '&'

    bot = TeleBot(BOT_TOKEN)

    main_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    main_markup.add(types.KeyboardButton(text='/help'))
    main_markup.add(types.KeyboardButton(text='/start_run'))
    main_markup.add(types.KeyboardButton(text='/restart'))

    def _move_user_to_next_location(message_or_callback_query: types.Message | types.CallbackQuery) -> None:

        with UserInfoManager(message_or_callback_query.from_user.id) as user_info_manager:

            if isinstance(message_or_callback_query, types.CallbackQuery):

                message_to_reply = message_or_callback_query.message

                user_next_location_id, user_next_level_id = message_or_callback_query.data.replace(
                    choice_prefix, ''
                ).split(choice_ids_divider)

                user_info_manager.change_user_location_id(user_next_location_id)
                user_info_manager.change_user_level_id(user_next_level_id)

                user_level: Level = LEVELS[user_next_level_id]
                user_location: Location = user_level.get_location_by_id(user_next_location_id)

            else:

                message_to_reply = message_or_callback_query

                user_level: Level = LEVELS[user_info_manager.get_user_level_id()]
                user_location: Location = user_level.get_location_by_id(user_info_manager.get_user_location_id())

            reply_message = f'Уровень: {user_level.name}\n'
            reply_message += f'Локация: {user_location.name}\n{user_location.description}'

            if user_location.move_choices:

                reply_markup = types.InlineKeyboardMarkup()

                for move_choice in user_location.move_choices:
                    reply_markup.add(types.InlineKeyboardButton(
                        text=move_choice.description,
                        callback_data=f'{choice_prefix}{move_choice.next_location_id}{choice_ids_divider}'
                                      f'{move_choice.next_level_id}',  # callback data example: "prefix_1&3"
                    ))

            else:

                reply_markup = main_markup

                user_info_manager.reset_user_data()

            random_pictures = deepcopy(user_location.pictures)
            shuffle(random_pictures)

            bot.send_media_group(
                message_to_reply.chat.id, [types.InputMediaPhoto(picture) for picture in random_pictures[:2]]
            )

            bot.reply_to(message_to_reply, reply_message, reply_markup=reply_markup)

    @bot.message_handler(commands=['start_run'])
    def start_handler(message: types.Message):

        bot.reply_to(message, 'Хорошо, начнём/продолжим:')

        _move_user_to_next_location(message)

    @bot.callback_query_handler(func=lambda call: choice_prefix in call.data)
    def question_answer_handler(call: types.CallbackQuery):
        _move_user_to_next_location(call)

    @bot.message_handler(commands=['help', 'start'])
    def help_handler(message: types.Message):

        reply_message = (
            'Привет, я - бот-квест, вот мой функционал:\n'
            '/help или /start - список всех команд (ты уже тут)\n'
            '/start_run - запуск/продолжение забега\n'
            '/restart - перезапуск забега'
        )

        bot.reply_to(message, reply_message, reply_markup=main_markup, parse_mode='HTML')

    @bot.message_handler(commands=['restart'])
    def restart_handler(message: types.Message):

        with UserInfoManager(message.from_user.id) as user_info_manager:
            user_info_manager.reset_user_data()

        bot.reply_to(message, 'Начинаем заново!')

        _move_user_to_next_location(message)

    @bot.message_handler(content_types=['text'])
    def text_handler(message: types.Message):

        replies = (
            'О, круто!',
            'Верно подмечено!',
            'Как с языка снял',
            'Какой ты всё-таки умный',
            'По-любому что-то умное написал',
            'Как лаконично то!',
        )

        bot.reply_to(message, choice(replies), reply_markup=main_markup)

    bot.infinity_polling()


def main():

    if set_up():
        run_bot()

    else:
        error('Setup cannot be completed, some errors occurred')


if __name__ == '__main__':
    main()
