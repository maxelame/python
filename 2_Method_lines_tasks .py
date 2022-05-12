# Фамилия Имя Отчество
#
# Напишите программу, которая принимает три аргумента командной строки: фамилию, имя и отчество, а затем выводит их в правильной форме: первая буква заглавная, остальные строчные.
# Пример использования:
# > python program.py иванов иван иванович
# > Иванов Иван Иванович
# Подсказка:
#
# Воспользуйтесь методом capitalize.



import sys
a, b, c = sys.argv[1], sys.argv[2], sys.argv[3]
print(a.capitalize(),b.capitalize(),c.capitalize())

# Меняем регистр
#
# Напишите программу, которая получает из первого аргумента командной строки слово,
# а после заменяет в нем заглавные буквы на строчные и наоборот.
# Пример использования:
# > python swapcase.py Python
# > pYTHON
# Подсказка:
#
# Используйте метод swapcase.

import sys
a = sys.argv[1]
print(a.swapcase())

# Меняем регистр
#
# Напишите программу, которая получает из первого аргумента командной строки слово,
# а после заменяет в нем заглавные буквы на строчные и наоборот.
# Пример использования:
# > python swapcase.py Python
# > pYTHON
# Подсказка:
#
# Используйте метод swapcase.

import sys
a = sys.argv[1]
print(a.swapcase())

# Основной заголовок
#
# Напишите программу, которая получает из первого аргумента командной строки слово, а после печатает это слово большими буквами. Слово должно быть помещено в центр строки длиной 20 символов и отбито справа и слева пробелами.
# Пример использования:
#
# Обратите внимание, что слева и справа от WORD стоят пробелы,
# а длина всей выводимой строки — 20 символов.
# > python upper.py word
# >         WORD
# Подсказка:
#
# Используйте методы upper и center.

import sys
word = sys.argv[1]
word = word.upper()
word = word.center(20,)
print(word)


# Количество повторений
#
# Напишите программу, которая получает из первого аргумента командной строки слово, а из второго букву и выводит сколько раз эта буква встречается в переданном слове.
# Пример использования:
# > python count.py programming r
# > 2
# Подсказка:
#
# Используйте метод count.

import sys
a, b = sys.argv[1], sys.argv[2]
print(a.count(b, 0, len())


# Мужчины и женщины
#
# В очереди за билетами в кино стоят мужчины и женщины. Нужно посчитать количество мужчин и количество женщин.
#
# Напишите программу, которая получает из первого аргумента командной строки набор символов m (мужчины) и w (женщины). Затем программа должна посчитать количество мужчин и женщин и вывести результаты на экран в виде импровизированной диаграммы (см. пример использования).
# Пример использования:
# > python mw.py mmwmwwmwwwmmw
# > m (6) ******
# > w (7) *******


import sys
mw = sys.argv[1]
m = mw.count('m',0,len(mw))
w = mw.count('w',0,len(mw))
print("m", '('+ str(m) +')', '*' *m)
print("w", '('+ str(w)  +')', '*' *w)
