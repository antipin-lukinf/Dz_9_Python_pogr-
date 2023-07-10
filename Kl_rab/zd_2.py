"""
Задание №2
📌 Дорабатываем задачу 1.
📌 Превратите внешнюю функцию в декоратор.
📌 Он должен проверять входят ли переданные в функцию угадайку числа в диапазоны [1, 100] и [1, 10].
📌 Если не входят, вызывать функцию со случайными числами
из диапазонов.
"""

import random
from typing import Callable


def outer(func) -> Callable:
    # num_range = int(input('Введите число от 0 до 100 : '))
    # attempts = int(input('Введите количество попыток от 1 до 10 : '))
    # num_sc = random.randint(1, num_range)
    def wrapper(guess: int, attempts: int):
        guess = guess if 1 < guess < 100 else random.randint(1, 100)
        attempts = attempts if 1 < attempts < 10 else random.randint(1, 10)

        return func(guess, attempts)

    return wrapper


@outer
def game_guess(num_sc, attempts) -> None:
    while attempts:
        print(f'Осталось {attempts} попыток.', end=' ')
        attempts -= 1
        num = int(input('Введите число : '))
        if num == num_sc:
            print('Вы угадали')
            break
        else:
            advice = ['меньше', 'больше']
            print(f'Твое число {advice[num > num_sc]}')
    else:
        print(f'Попытки закончились и ты не угадал, было загаданно число {num_sc}')
    # return inner


# @outer()
# def main():
#     game = outer()
#     game()


if __name__ == '__main__':
    game_guess(200, 300)
