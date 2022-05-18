"""Только цифры

Напишите программу, которая принимает первым аргументом командной строки автомобильный номер, состоящий из цифр и заглавных букв латинского алфавита, а после очищает все буквы, оставляя только цифры. Количество букв слева и справа может быть произвольным.

В качестве букв могут приниматься только следующие латинские символы: E, T, O, P, A, H, K, C, B, M, Y, X.
Пример использования:
> python program.py A741BC
> 741
python program.py BC2345KM
> 2345
 """

import sys
number = sys.argv[1]
print(number.strip("ETOPAHKCBMYX"))

'''Лицевой счет

Напишите программу, которая принимает первым аргументом командной строки номер лицевого счета, состоящий из 8 цифр. Если номер короткий, то в начале проставляются нули, например 00001451. В результате работы программа должна вывести номер без лидирующих нулей.

Воспользуйтесь методом lstrip, который работает также как и strip, но очищает только левую часть строки.
Пример использования:
> python program.py 00123456
> 123456
python program.py 05550600
> 5550600'''

import sys
number = sys.argv[1]
print(number.lstrip("0"))

"""Убираем нули

Напишите программу, которая принимает первым аргументом командной строки вещественное число и удаляет из него все лишние нули, находящиеся справа.

Воспользуйтесь методом rstrip, который работает также как и strip, но очищает только правую часть строки.
Пример использования:
> python program.py 78.4500
> 78.45
python program.py 078.4500
> 078.45
 """

import sys
number = sys.argv[1]
print(number.rstrip("0"))


"""Начинающий разработчик написал программу для удаления из строки вида «ООО "Компания"» аббревиатуры «ООО», кавычек и лишних пробелов. Однако код оказался ненадежным и в некоторых случаях из строки удаляется часть наименования фирмы. Исправьте программу, чтобы она работала правильно.
Пример использования:
> python program.py "ООО \"Компания\""
> Компания"""

import sys

# Получаем данные
name = sys.argv[1]

# Чистим и выводим данные.
print(name.lstrip("О ").strip("\'\" \\"))

