# Английские сокращения
#
# В английском языке приняты следующие сокращения:
#
#     I am — I'm
#     You are — You're
#     He is — He's
#     She is — She's
#     It is — It's
#     We are — We're
#     They are — They're
#
# Напишите программу, которая получает из первого аргумента командной строки фразу на английском языке, а затем заменяет в ней все полные сочетания на сокращения (в соответствии со списком выше).
# Пример использования:
# > python program.py "I am programmer."
# > I'm programmer.

import sys
a = sys.argv[1]
a = a.replace("I am", "I'm").\
replace("You are", "You're").\
replace("He is", "He's").\
replace("She is", "She's").\
replace("It is", "It's").\
replace("We are", "We're").\
replace("They are", "They're")
print(a)

# Шифруем номер
#
# Напишите программу, которая принимает первым аргументом командной строки телефонный номер, а затем шифрует его и выводит результат.
#
# Программа использует простой шифр, заменяя цифры номера на буквы или сочетания букв:
#
#     0 — a
#     1 — (пробел)
#     2 — b
#     3 — e
#     4 — l
#     5 — mu
#     6 — n
#     7 — o
#     8 — lee
#     9 — f
#
# Обратите внимание, что номер телефона заканчивается точкой, которую шифровать не надо.
# Пример использования:
# > python program.py 89514568156.
# > leefmu lmunlee mun.

import sys
number = sys.argv[1]
number = number.\
replace("0","a").\
replace("1"," ").\
replace("2","b").\
replace("3","e").\
replace("4","l").\
replace("5","mu").\
replace("6","n").\
replace("7","o").\
replace("8","lee").\
replace("9","f")
print(number)

# Расшифровываем номер
#
# Используя таблицу соответствий цифр буквам из прошлого урока, напишите программу, которая первым аргументом командной строки принимает зашифрованный телефонный номер, а затем дешифрует его и выводит результат.
#
# Шифр из прошлго урока:
#
#     0 — a
#     1 — (пробел)
#     2 — b
#     3 — e
#     4 — l
#     5 — mu
#     6 — n
#     7 — o
#     8 — lee
#     9 — f
#
# Обратите внимание, что номер телефона заканчивается точкой, которую шифровать не надо.
# Пример использования:
# > python program.py "leefmu lmunlee mun."
# > 89514568156.


import sys
number = sys.argv[1]
number = number.\
replace("a","0").replace("lee","8").\
replace(" ","1").\
replace("b","2").\
replace("e","3").\
replace("l","4").\
replace("mu","5").\
replace("n","6").\
replace("o","7").\
replace("f","9")
print(number)




















