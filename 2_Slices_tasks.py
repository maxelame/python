# Напишите программу, которая принимает первым аргументом командной строки полный автомобильный номер, а после выводит его регистрационный номер

import sys
number = sys.argv[1]
print(number[1:4])


# Напишите программу, которая получает первым аргументом командной строки текст, а после обрезает его до 10 символов и добавляет в конец три точки.

import sys
text = sys.argv[1]
print(text[0:10] + "." *3)


# Расширение файла
#
# Расширение файла — это последовательность символов, добавляемых к имени файла, которые нужны для идентификации его типа (формата). Это один из распространённых способов, с помощью которых программа может определить тип данных, хранящихся в файле, например:
# image.jpg — это фотографии, rest.mp4 — видео и т.п
#
# Напишите программу, которая первым аргументом командной строки принимает имя файла вместе с расширением, а после выводит только его расширение. Для удобства будем считать, что все расширения состоят из трех символов.

import sys
file = sys.argv[1]
print(file[-3:])


# Имя файла
#
# В прошлом задании мы выводили расширение файла, а теперь давайте печатать его имя.
#
# Напишите программу, которая первым аргументом командной строки принимает имя файла вместе с расширением, а после выводит только его имя. Для удобства будем считать, что все расширения состоят из трех символов.

import sys
file = sys.argv[1]
print(file[:len(file)-4])

























