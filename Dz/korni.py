"""
Напишите следующие функции:
○Нахождение корней квадратного уравнения
○Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
○Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
○Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.

"""
import csv
import math
import os
from functools import wraps
from random import randint
from typing import Callable
import ast


def gen_csv(file_name) -> Callable:
    def inn_func(func):
        @wraps(func)
        def wrapper():
            my_arguments = []

            count_string = randint(100, 1000)
            for i in range(count_string):
                a = randint(0, 20)
                b = randint(0, 20)
                c = randint(0, 20)
                # atr = f'{a}, {b}, {c}'
                # exec("tempvar = " + atr)
                my_arguments.append({'a': a, 'b': b, 'c': c})



            if os.path.exists(file_name):
                with open(file_name, 'w', newline='', encoding='utf-8') as f:
                    columns = ['a', 'b', 'c']
                    writer = csv.DictWriter(f, fieldnames=columns)
                    writer.writeheader()

                    writer.writerows(my_arguments)
            else:
                with open(file_name, 'w', newline='', encoding='utf-8') as f:
                    columns = ['a', 'b', 'c']
                    writer = csv.DictWriter(f, fieldnames=columns)
                    writer.writeheader()

                    writer.writerows(my_arguments)
            return func()

        return wrapper

    return inn_func


@gen_csv('my_arguments.csv')
def korni():
    a = 1
    b = 2
    c = 3
    diskr = b ** 2 - 4 * a * c
    if diskr > 0:
        x1 = (-b + math.sqrt(diskr)) / (2 * a)
        x2 = (-b - math.sqrt(diskr)) / (2 * a)
        return "x1 = %.2f \nx2 = %.2f" % (x1, x2)
    elif diskr == 0:
        x1 = (-b + math.sqrt(diskr)) / (2 * a)
        return "x1 = %.2f" % x1
    else:
        return False


print(korni())
