# Создайте программу, которая получает из первого аргумента командной строки имя ученика,
# а после выводит на экран фразу "Hello <ученик>".

import sys
print("Hello", sys.argv[1])


# Создайте программу, которая получает из первого аргумента командной строки год рождения пользователя,
# а после выводит на экран фразу "Год рождения: <год>".

import sys
print("Год рождения:", sys.argv[1])


# Через командную строку (или параметры PyCharm) можно передавать не один параметр, а сразу несколько.
# Для этого их нужно разделить пробелом:

import sys
first_name = sys.argv[1]
last_name = sys.argv[2]
print("Hello", first_name,last_name)

# Напишите программу, которая получает из аргументов командной строки два аргумента:
# марку и модель автомобиля, а после выводит на экран фразу "Автомобиль: <марка> <модель>".

import sys
marka = sys.argv[1]
model = sys.argv[2]
print("Автомобиль:",marka,model)
