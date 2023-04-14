# https://www.codewars.com/kata/50ee6b0bdeab583673000025
# a = "code"
# b = "wa.rs"
# name = a +' '+ b
# print(name)

# https://www.codewars.com/kata/55a70521798b14d4750000a4
# def greet(name):
#     return f"Hello, {'andy'} how are you doing today?"
#     pass

# https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3
# def abbrev_name(name):
#     a = list(name.split())
#     return a[0][0].upper() + '.' +a[1][0].upper()
# print(abbrev_name('andrew zhan'))

# https://www.codewars.com/kata/554b4ac871d6813a03000035
# def high_and_low(numbers):
#     b = numbers.split(' ', -1)
#     x = [int(i) for i in b]
#     c = min(x)
#     d = max(x)
#     print(x, c, d)
#     numbers = str(c) + ' ' + str(d)
#     return numbers
#
# high_and_low('1 2 3')

# https://www.codewars.com/kata/57a55c8b72292d057b000594
# def reverse(st):
#     a = st.split()
#     a.reverse()
#     st = ' '.join(a)
#     print(st)
#     return st
#
# reverse('am an expert at this I')

# https://www.codewars.com/kata/5966e33c4e686b508700002d
# def sum_str(a, b):
#     if not str(a):
#         a = 0
#     if not str(b):
#         b = 0
#     sum = str(int(a) + int(b))
#     print(sum)
#     return sum
#     pass
#
# sum_str('', '')

# # https://www.codewars.com/kata/57e1e61ba396b3727c000251
# def string_clean(s):
#     a = list(s)
#     b = []
#     print(a)
#     for symbol in a:
#         if not symbol.isdigit():
#             b.append(symbol)
#     print(b)
#     s = ''.join(b)
#     print(s)
#     return s
# string_clean('This looks5 grea8t!')

# https://www.codewars.com/kata/57a0e5c372292dd76d000d7e
# def repeat_str(repeat, string):
#     string = string * repeat
#     print(string)
#     return string
#
# repeat_str(4, 'Hi')

# https://www.codewars.com/kata/5121303128ef4b495f000001
# class Person():
#     def __init__(self, name):
#         self.name = name
#     def greet(self, other_name):
#         return f'Hello {other_name}, my name is {self.name}'
#
# jack = Person("Jack")
# jill = Person("Jill")
# print(jack.greet(jill.name))

# https://www.codewars.com/kata/62c93765cef6f10030dfa92b
# def get_jumps(start, finish):
# start = 1
# finish = 10
# jumps = finish // start + finish % start

# https://www.codewars.com/kata/56d19b2ac05aed1a20000430
# def

# https://www.codewars.com/kata/55ddb0ea5a133623b6000043
# def class_name_changer(cls, new_name):
#     flag = True
#     if not
#     pass;
# __class__.__name__

# https://www.codewars.com/kata/5c79c07b4ba1e100097f4e1a
# def yoga(classroom, poses):
#     poses_done = 0
#     for i in poses:
#         for row in classroom:
#             row_sum = sum(row)
#             for j in row:
#                 if row_sum + j >= i:
#                     poses_done += 1
#     return poses_done
#     pass

# https://www.codewars.com/kata/580755730b5a77650500010c
# def sort_my_string(s):
#     a = []
#     b = []
#     for i in range(len(s)):
#         if i % 2 == 0:
#             a.append(s[i])
#         else:
#            b.append(s[i])
#     return f"{''.join(a)} {''.join(b)}"

# альтернатива
# def sort_my_string(s):
#     a = s[::2]
#     b = s[1::2]
#     return f"{a} {b}"

# https://www.codewars.com/kata/62c93765cef6f10030dfa92b
# def solution(start, finish):
#     answer = (finish - start) % 3 + (finish - start) // 3
#     return answer

# https://www.codewars.com/kata/56d19b2ac05aed1a20000430
# def between_extremes(numbers):
#     return max(numbers) - min(numbers)
#     pass

# альтернатива
# between_extremes = lambda numbers: max(numbers) - min(numbers)

# https://www.codewars.com/kata/586beb5ba44cfc44ed0006c3
# def sum_even_numbers(seq):
#     return sum(x for x in seq if x % 2 == 0)
#     pass

# альтернатива
# sum_even_numbers = lambda x: sum(i for i in x if i % 2 ==0)
# sum_even_numbers = lambda x: sum(filter(lambda y: y % 2 == 0, x))

# https://www.codewars.com/kata/53d32bea2f2a21f666000256
# def largest(n, xs):
#     x = []
#     for i in range(0,n):
#         i = max(xs)
#         x.insert(0, i)
#         xs.remove(i)
#     return x
#     pass

# альтернатива
# def largest(n, xs):
#     xs.sort()
#     ls = xs[::-1]
#     result = ls[:n]
#     return result[::-1]

# альтернатива
# def largest(n, xs):
#     xs.sort()
#     return xs[-n:]

# https://www.codewars.com/kata/5966f6343c0702d1dc00004c
# def give_change(amount):
#     lst = [0, 0, 0, 0, 0, 0]
#     arr = [100, 50, 20, 10, 5, 1]
#     for i in range(len(arr)):
#         lst[i] = amount // arr[i]
#         amount -= arr[i] * lst[i]
#     return tuple(lst[::-1])
#     pass

# https://www.codewars.com/kata/5882b052bdeafec15e0000e6
# class Quark:
#     baryon_number = 1/3
#     colors = ['red', 'blue', 'green']
#     flavors = ['up', 'down', 'strange', 'charm', 'top', 'bottom']
#
#     def __init__(self, color, flavor):
#         self.color = color
#         self.flavor = flavor
#
#     def get_color(self):
#         return self.color
#
#     def get_flavor(self):
#         return self.flavor
#
#     def interact(self, other_quark):
#         self.color, other_quark.color = other_quark.color, self.color
#         return self.color, other_quark.color

# https://www.codewars.com/kata/55b75fcf67e558d3750000a3
# class Block:
#     args = []
#     def __init__(self, args):
#         self.width = args[0]
#         self.length = args[1]
#         self.height = args[2]
#
#     def get_width(self):
#         return self.width
#
#     def get_length(self):
#         return self.length
#
#     def get_height(self):
#         return self.height
#
#     def get_volume(self):
#         return self.width * self.length * self.height
#
#     def get_surface_area(self):
#         return 2 * (self.width * self.length + self.length * self.height + self.width * self.height)
#
# b = Block([2, 4 ,6])
# print(b.get_surface_area())

# https://www.codewars.com/kata/55c1d030da313ed05100005d
# class Sphere(object):
#
#     def __init__(self, radius, mass):
#         self.radius = radius
#         self.mass = mass
#
#     def get_radius(self):
#         return self.radius
#
#     def get_mass(self):
#         return self.mass
#
#     def get_volume(self):
#         return round(4 / 3 * 3.141592653589793 * self.radius * self.radius * self.radius, 5)
#
#     def get_surface_area(self):
#         return round(4 * 3.141592653589793 * self.radius * self.radius, 5)
#
#     def get_density(self):
#         return round(self.mass / (4 / 3 * 3.141592653589793 * self.radius * self.radius * self.radius), 5)
#
# b = Sphere(2, 50)
# print(b.get_density())

# https://www.codewars.com/kata/632408defa1507004aa4f2b5
# class Class:
#     _counter = 1
#
#     @staticmethod
#     def get_number():
#         if Class._counter == 1:
#             Class._counter += 1
#             return 1
#         else:
#             Class._counter += 1
#             return 2 ** (Class._counter - 2)
#
# print(Class.get_number())
# print(Class.get_number())
# print(Class.get_number())
# print(Class.get_number())
# print(Class.get_number())

# https://www.codewars.com/kata/54fe05c4762e2e3047000add
# class Ship:
#     def __init__(self, draft, crew):
#         self.draft = draft
#         self.crew = crew
#
#     def is_worth_it(self):
#         return self.draft - self.crew * 1.5 >= 20
#
# Titanic = Ship(15, 10)
# print(Titanic.is_worth_it())

# https://www.codewars.com/kata/5956d127a817c7c51b000026
# class Student:
#
#     def __init__(self, first_name, last_name, grades=None):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.grades = grades or []
#
#     def add_grade(self, grade):
#         self.grades.append(grade)
#
#     def get_average(self):
#         return sum(self.grades) / len(self.grades)

# https://www.codewars.com/kata/571d2e9eeed4a150d30011e7
# def scoreboard(participants):
#     scores = []
#     for participant in participants:
#         chickenwings = participant.get("chickenwings", 0)
#         hamburgers = participant.get("hamburgers", 0)
#         hotdogs = participant.get("hotdogs", 0)
#         score = chickenwings*5 + hamburgers*3 + hotdogs*2
#         scores.append({"name": participant["name"], "score": score})
#     scores.sort(key=lambda x: (-x["score"], x["name"]))
#     return scores
#
# participants = [
#   {"name": "Kyle Reese", "chickenwings": 5, "hamburgers": 10, "hotdogs": 9},
#   {"name": "Sarah Connor", "chickenwings": 3, "hamburgers": 7, "hotdogs": 5},
#   {"name": "John Connor", "chickenwings": 8, "hamburgers": 4, "hotdogs": 16},
#   {"name": "Big Bob", "c": 20, "hamburgers": 4, "hotdogs": 11}
# ]
# scores = scoreboard(participants)
# print(scores)

# https://www.codewars.com/kata/55ddb0ea5a133623b6000043
# def rename_class(cls, new_name):
#     if not new_name.isalnum() or not new_name[0].isupper():
#         raise ValueError("Invalid class name")
#     cls.__name__ = new_name

# https://www.codewars.com/kata/55ddcef532f8678af1000006
# class ReNameAbleClass(object):
#     @classmethod
#     def change_class_name(cls, new_name):
#         if not new_name.isalnum() or not new_name[0].isupper():
#             raise ValueError("Invalid class name")
#         cls.__name__ = new_name
#         pass
#
#     @classmethod
#     def __str__(cls):
#         return f'Class name is: {cls.__name__}'
#         pass

# https://www.codewars.com/kata/513f887e484edf3eb3000001
# class Person():
#
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.full_name = first_name + ' ' + last_name

# https://www.codewars.com/kata/596343a24489a8b2a00000a2
# def is_it_a_num(s: str) -> str:
#     f = filter(str.isdecimal, s)
#     s = "".join(f)
#     if len(s) == 0 or s[0] != '0' or len(s) != 11:
#         return f'Not a phone number'
#     else:
#         return s
#     pass
#
#
# is_it_a_num('S:)0207ERGQREG88349F82!efRF)')
# is_it_a_num('sjfniebienvr12312312312ehfWh')
# is_it_a_num('0192387415456')
# is_it_a_num('v   uf  f 0tt2eg qe0b 8rtyq4eyq564()(((((165')
# is_it_a_num('stop calling me no I have never been in an accident')

# https://www.codewars.com/kata/559cc2d2b802a5c94700000c
# def consecutive(arr):
#     arr.sort()
#     count = 0
#     for i in range(len(arr) - 1):
#         diff = arr[i+1] - arr[i] - 1
#         count += diff
#     return count

# https://www.codewars.com/kata/563fb342f47611dae800003c
# def trim(phrase, size):
#     if len(phrase) <= size:
#         # return phrase
#         print(phrase)
#     if len(phrase) <= 3:
#         # return phrase
#         print(phrase[::size] + '...')
#     if len(phrase[::size]) > 11:
#         # return phrase[::11] + '...'
#         print(phrase[::11] + '...')
#     if len(phrase[::size]) <= 11:
#         # return phrase[::size] + '...'
#         print(phrase[::size] + '...')
    # phrase1 = phrase[::size]
    # if len(phrase[::size]) < len(phrase) and len(phrase[::size]) == 14:
    #     return f"phrase[::size] + '...'"
    # raise NotImplementedError('trim')

# def trim(phrase, size):
#     if len(phrase) <= size:
#         # return phrase
#         print(phrase)
#     else:
#         if len(phrase) <= 3:
#         # return phrase
#             print(phrase[::size] + '...')
#         else:
#             if len(phrase[::size]) >= 11:
#         # return phrase[::11] + '...'
#                 print(phrase[::12] + '...')
#             else:
#                 if len(phrase[::size]) <= 11:
#         # return phrase[::size] + '...'
#                     print(phrase[::size] + '...')

# def trim(phrase, size):
#     if len(phrase) > size:
#         if len(phrase) > 3:
#             if len(phrase[::size]) > 11:
#                 print(phrase[::11] + '...')
#             else:
#                 print(phrase[::size] + '...')
#         else:
#             print(phrase[::size] + '...')
#     else:
#         print(phrase)
#
#
# trim("Creating kata is fun", 14)
# trim("He", 1)
# trim("Hey", 2)
# trim("Hey", 3)
# trim("Coding rocks", 12)
# trim("Code Wars is pretty rad", 50)
# trim("London is freezing", 18)

# https://www.codewars.com/kata/55960bbb182094bc4800007b
# def insert_dash(num):
#     num_str = str(num)
#     result = ''
#     for i in range(len(num_str)):
#         if i > 0 and int(num_str[i-1]) % 2 == 1 and int(num_str[i]) % 2 == 1:
#             result += '-'
#         result += num_str[i]
#     return result
