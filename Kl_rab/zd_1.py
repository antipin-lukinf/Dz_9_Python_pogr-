"""
Задание №1
📌 Создайте функцию-замыкание, которая запрашивает два целых
числа:
○ от 1 до 100 для загадывания,
○ от 1 до 10 для количества попыток
📌 Функция возвращает функцию, которая через консоль просит
угадать загаданное число за указанное число попыток.
"""
import random
from typing import Callable


def outer() -> Callable:
    num_range = int(input('Введите число от 0 до 100 : '))
    attempts = int(input('Введите количество попыток от 1 до 10 : '))
    num_sc = random.randint(1, num_range)

    def inner() -> None:
        nonlocal num_range, attempts
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
        return inner


def main():
    game = outer()
    game()


if __name__ == '__main__':
    main()
