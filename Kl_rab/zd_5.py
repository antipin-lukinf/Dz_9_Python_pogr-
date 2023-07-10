"""
Задание №5
📌 Объедините функции из прошлых задач.
📌 Функцию угадайку задекорируйте:
○ декораторами для сохранения параметров,
○ декоратором контроля значений и
○ декоратором для многократного запуска.
📌 Выберите верный порядок декораторов.
"""
import json
import os
import random
from functools import wraps
from typing import Callable


def counter(number):

    def dec(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = []
            for _ in range(number):
                result.append(func(*args, **kwargs))
            return tuple(result)

        return wrapper

    return dec


def checker(func) -> Callable:
    # num_range = int(input('Введите число от 0 до 100 : '))
    # attempts = int(input('Введите количество попыток от 1 до 10 : '))
    # num_sc = random.randint(1, num_range)
    @wraps(func)
    def wrapper(guess: int, attempts: int):
        guess = guess if 1 < guess < 100 else random.randint(1, 100)
        attempts = attempts if 1 < attempts < 10 else random.randint(1, 10)

        return func(guess, attempts)

    return wrapper


def writer(file_name) -> Callable:
    def inner_func(func):
        @wraps(func)
        def wrapper(number, tries):
            my_dict = {str(func(number, tries)): (number, tries)}

            if os.path.exists(file_name):
                with open(file_name, 'a', encoding='utf-8') as f:
                    json.dump(my_dict, f, ensure_ascii=False, indent=4)
            else:
                with open(file_name, 'w', encoding='utf-8') as f:
                    json.dump(my_dict, f, ensure_ascii=False, indent=4)
            return func(number, tries)

        return wrapper

    return inner_func


@writer('guess_game.json')
@checker
@counter(3)
def game_guess(num_sc, attempts):
    """Игра угадайка"""
    result_attempts = 0
    while attempts:
        print(f'Осталось {attempts} попыток.', end=' ')
        attempts -= 1
        num = int(input('Введите число : '))
        if num == num_sc:
            print('Вы угадали')
            return result_attempts
        else:
            advice = ['меньше', 'больше']
            print(f'Твое число {advice[num > num_sc]}')
            result_attempts += 1
    else:
        print(f'Попытки закончились и ты не угадал, было загаданно число {num_sc}')
    return result_attempts

help(game_guess)
# game_guess(10, 567)
