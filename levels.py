from app_dataclasses import Level, Location, MoveChoice


START_LEVEL_ID = 'start'
END_LEVEL_ID = 'end'
END_PICTURES = [
    'https://postimg.cc/4HNTDzWK',
    'https://postimg.cc/gw8d8cw0',
    'https://postimg.cc/G9crTCbc',
    'https://postimg.cc/jwTTXVN4',
    'https://postimg.cc/4YrsYHxM',
    'https://postimg.cc/ygTHpfy4',
]


LEVELS = {
    START_LEVEL_ID: Level(id=START_LEVEL_ID, name='Начало начал', locations=(
        Location(
            id='1',
            name='Базовый лагерь',
            description='Тут десятки искателей приключений в последний раз могут почувствовать себя в безопасности',
            move_choices=(
                MoveChoice(
                    description='Идти в тёмный и ужасный лес', next_location_id='2', next_level_id=START_LEVEL_ID
                ),
                MoveChoice(description='Идти в обычный лес', next_location_id='3', next_level_id=START_LEVEL_ID),
                MoveChoice(description='Идти домой', next_location_id='4_end', next_level_id=START_LEVEL_ID),
                MoveChoice(
                    description='Посидеть в лагере, куда торопиться?',
                    next_location_id='1',
                    next_level_id=START_LEVEL_ID,
                ),
            ),
            pictures=[
                'https://postimg.cc/HjpMMb7F',
                'https://postimg.cc/crC89Zhm',
                'https://postimg.cc/G4sTRQZT',
                'https://postimg.cc/SjDMfj6R',
                'https://postimg.cc/bs5S4MFj',
            ],
        ),
        Location(
            id='2',
            name='Тёмный лес',
            description='Ужасный лес, кто знает, что скрывается в его недрах?',
            move_choices=(
                MoveChoice(description='Идти вперёд', next_location_id='1', next_level_id='middleland'),
                MoveChoice(description='Идти направо', next_location_id='2', next_level_id='middleland'),
                MoveChoice(
                    description='Идти вертикально вверх', next_location_id='5_end', next_level_id=START_LEVEL_ID
                ),
            ),
            pictures=[
                'https://postimg.cc/w7PfBJzN',
                'https://postimg.cc/56jK1gh1',
                'https://postimg.cc/c6FkV25X',
                'https://postimg.cc/nsf34JCc',
                'https://postimg.cc/0zwtKQ5B',
            ],
        ),
        Location(
            id='3',
            name='Обычный лес',
            description='Самый обычный, ничем не примечательный лес',
            move_choices=(
                MoveChoice(description='Идти вперёд', next_location_id='3', next_level_id='middleland'),
                MoveChoice(description='Идти направо', next_location_id='2', next_level_id='middleland'),
                MoveChoice(description='Идти налево', next_location_id='6_end', next_level_id=START_LEVEL_ID),
            ),
            pictures=END_PICTURES,
        ),
        Location(
            id='4_end',
            name='Нет пути назад',
            description='Не-а, не вышел фокус, но идея здравая, жаль, что это тебе не помогло, конец игры',
            move_choices=(),
            pictures=END_PICTURES,
        ),
        Location(
            id='5_end',
            name='Странное место',
            description='Удивительно, но у тебя получилось, но вот только это не было явью. Растение или животное,'
                        ' может злой колдун. Конец игры',
            move_choices=(),
            pictures=END_PICTURES,
        ),
        Location(
            id='6_end',
            name='Не ходи налево',
            description='Ты же знал, что не стоит, но всё равно пошёл, за что и поплатился, не ходи налево, конец игры',
            move_choices=(),
            pictures=END_PICTURES,
        ),
    )),
    'middleland': Level(id='middleland', name='Средеземье', locations=(
        Location(
            id='1',
            name='Мрачная развилка',
            description='Уже при подходе к этому месту мрак подступил со всех сторон, нужно уходить как можно быстрее',
            move_choices=(
                MoveChoice(
                    description='Броситься в пещеру', next_location_id='4_end', next_level_id=START_LEVEL_ID
                ),
                MoveChoice(
                    description='Помчаться дальше по дороге', next_location_id='1', next_level_id=END_LEVEL_ID
                ),
                MoveChoice(description='Обстоятельно подумать', next_location_id='5_end', next_level_id='middleland'),
            ),
            pictures=[
                'https://postimg.cc/RqZH426Y',
                'https://postimg.cc/2LybGBNY',
                'https://postimg.cc/Q9XWBy6H',
                'https://postimg.cc/s1HZXK5g',
                'https://postimg.cc/N9p2RkVb',
            ],
        ),
        Location(
            id='2',
            name='Подозрительная поляна',
            description='Что-то в этом месте не даёт покоя, пора двигаться',
            move_choices=(
                MoveChoice(description='Идти вперёд', next_location_id='2', next_level_id=END_LEVEL_ID),
                MoveChoice(description='Подождать ради интереса', next_location_id='5_end', next_level_id='middleland'),
            ),
            pictures=[
                'https://postimg.cc/WDxzPpKm',
                'https://postimg.cc/bZCd399B',
                'https://postimg.cc/w3LygJ91',
                'https://postimg.cc/64J8C6f6',
                'https://postimg.cc/nXcC4PBm',
            ],
        ),
        Location(
            id='3',
            name='Нисколько не подозрительная дорога',
            description='Дальнейший путь усеян брошенными мечами и луками, ничего подозрительного',
            move_choices=(
                MoveChoice(description='Идти вперёд', next_location_id='6_end', next_level_id='middleland'),
                MoveChoice(description='Обойти', next_location_id='2', next_level_id=END_LEVEL_ID),
            ),
            pictures=[
                'https://postimg.cc/sGZcK2WM',
                'https://postimg.cc/SXTfh97X',
                'https://postimg.cc/jCGv2zVP',
                'https://postimg.cc/w3t09wr9',
            ],
        ),
        Location(
            id='4_end',
            name='Пещера',
            description='Не повезло, хозяин пещеры был внутри, помянем, конец игры',
            move_choices=(),
            pictures=END_PICTURES,
        ),
        Location(
            id='5_end',
            name='Ждун',
            description='Быть может, если бы ты был схож с камнем, то всё бы получилось, но а пока конец игры',
            move_choices=(),
            pictures=END_PICTURES,
        ),
        Location(
            id='6_end',
            name='Страха нет',
            description='Бесстрашно пойдя вперёд, что-то произошло, твой меч упал на землю, а ты... Конец игры',
            move_choices=(),
            pictures=END_PICTURES,
        ),
    )),
    END_LEVEL_ID: Level(id=END_LEVEL_ID, name='КОНЕЦ', locations=(
        Location(
            id='1',
            name='Победа',
            description='Как говорится, winner, winner chicken dinner, приятного аппетита',
            move_choices=(),
            pictures=[
                'https://postimg.cc/8sbH5YSv',
                'https://postimg.cc/bsB1ScFZ',
                'https://postimg.cc/5XQLw7Zn',
                'https://postimg.cc/0zhGFRpT',
                'https://postimg.cc/CBS8pFdQ',
            ],
        ),
        Location(
            id='2',
            name='Битва с боссом',
            description='Соберись, нужно победить эту махину',
            move_choices=(
                MoveChoice(
                    description='Проявить чудеса ловкости и победить',
                    next_location_id='4_end',
                    next_level_id=END_LEVEL_ID,
                ),
                MoveChoice(
                    description='Подождать, утро вечера мудренее', next_location_id='5_end', next_level_id=END_LEVEL_ID
                ),
                MoveChoice(description='RUUUUUN', next_level_id='1', next_location_id=END_LEVEL_ID),
            ),
            pictures=[
                'https://postimg.cc/PpC0QkQP',
                'https://postimg.cc/mzKJd6mV',
                'https://postimg.cc/WdnR284b',
                'https://postimg.cc/HJsqjMJ0',
            ],
        ),
        Location(
            id='4_end',
            name='Ну, почти',
            description='Как говориться, грация кошки, реакция картошки, конец игры',
            move_choices=(),
            pictures=END_PICTURES,
        ),
        Location(
            id='5_end',
            name='Ждун',
            description='Быть может, если бы ты был схож с камнем, то всё бы получилось, но а пока конец игры',
            move_choices=(),
            pictures=END_PICTURES,
        ),
    )),
}
