from time import time, sleep
import functools
from random import randint
import time

# def null_decorator(func):
#     return func
#
#
# def uppercase(func):
#     def wrapper():
#         original_result = func()
#         modified_result = original_result.upper()
#         return modified_result
#     return wrapper
#
#
# @uppercase
# def greet():
#     return 'Hello!'
#
#
# print(greet())    # 'HELLO!'
# print(greet)
# print(uppercase(greet))
# print(null_decorator(greet))
import functools


#===== применение нескольких декораторов
# def strong(func):
#     def wrapper():
#         return '<strong>' + func() + '</strong>'
#     return wrapper
#
#
# def emphasis(func):
#     def wrapper():
#         return '<em>' + func() + '</em>'
#     return wrapper
#
#
# @strong
# @emphasis
# def greet():
#     return 'Hello!'
#
#
# print(greet())

# Как декорировать функцию, принимающую произвольные аргументы?
# def proxy(func):
#     def wrapper(*args, **kwargs):
#         return func(*args, **kwargs)
#     return wrapper


# def trace(func):
#     def wrapper(*args, **kwargs):
#         print(f'TRACE: calling {func.__name__}() '
#               f'with {args}, {kwargs}')
#
#         original_result = func(*args, **kwargs)
#
#         print(f'TRACE: {func.__name__}() '
#               f'returned {original_result!r}')
#
#         return original_result
#     return wrapper
#
#
# @trace
# def say(name, line):
#     return f'{name}: {line}'
#
# say('Jane', 'Hello, World')
# 'TRACE: calling say() with ("Jane", "Hello, World"), {}'
# 'TRACE: say() returned "Jane: Hello, World"'
# 'Jane: Hello, World'

# def repeat(n=5):
#     pass
#
# @repeat(n=5)
# def foo(x, y):
#     print(x + y)

#
# def decorator(func):
#     # here wrapper starts
#     def wrapper():
#         print("Код до выполнения функции")
#         #func()
#         rezult = func()
#         print("Код, который выполняется после выполнения функции")
#         return rezult
#     # here wrapper ends
#     return wrapper
#
#
# @decorator
# def hw():
#     print("Привет, группа!")
#     # добавить возвращаемое значение
#     return 42
#
# print(hw)
# #hw()
# znacenie = hw() + 10
# print(znacenie)


# ДЕкоратор для логирования
def log_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f'Вызвана функция {func.__name__} с аргументами {args} и ключевыми аргументами {kwargs}.')
        start_ti= time()
        # Вызов оборачиваемой функции
        rezult = func(*args, **kwargs)
        end_time = time()
        duration = end_time - start_time
        print(f'Функция {func.__name__} вернула {rezult}.') #вызов оборачиваемой функции
        return rezult

    return wrapper
#
#
# def sum(a, b):
#     return a + b
#print(sum(3,78))


@log_decorator
def hello_world():
    print("Hellow, world!")
    # Случайная пауза от 1 до 5 сек
    случайная_пауза = randint(1, 5)
    print(f"Случайная пауза: {случайная_пауза} сек")
    sleep(случайная_пауза)


print(hello_world())

