"""
Напишите следующие функции:
○Нахождение корней квадратного уравнения
○Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
○Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
○Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.

"""
import math
from random import randint


def korni(a, b, c):
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


print(korni(1, 2, 1))
