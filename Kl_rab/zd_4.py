"""
Задание №4
📌 Создайте декоратор с параметром.
📌 Параметр - целое число, количество запусков декорируемой
функции.
Погружение в Python
"""


def counter(number):
    def dec(func):
        def wrapper(*args, **kwargs):
            result = []
            for _ in range(number):
                result.append(func(*args, **kwargs))
            return result

        return wrapper

    return dec


@counter(5)
def func(a, b):
    return a + b


print(func(2, 4))
