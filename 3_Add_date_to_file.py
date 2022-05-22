'''Рядом с программой находится файл со списком продуктов products.txt.
Напишите программу, которая добавляет в этот файл два новых продукта: Масло и Мясо.
Записи должны добавляться с новой строки каждая.
В исходном файле продукты также записаны с новой строки, при этом после последней записи перевода строки нет.
Пример запуска программы:
> python program.py

После того как программа выполнится, система сама откроет файл products.txt и проверит его содержимое.
 '''
products_file = open("products.txt", "a", encoding = "utf8")
products_file.write("\nМасло\nМясо")
#products_file.write("\nМясо")

'''Новый продукт

Рядом с программой находится файл со списком продуктов products.txt.
Напишите программу, которая принимает первым аргументом командной строки новый товар, а затем добавляет его с новой строки в файл products.txt.
Исходный файл находится в кодировке utf-8 и продукты в нём записаны с новой строки каждый, при этом после последней записи также стоит перевод строки.
Пример запуска программы:
> python program.py Молоко

После того как программа выполнится, система сама откроет файл products.txt и проверит его содержимое.'''
 
import sys
milk = str(sys.argv[1])
products_file = open ("products.txt", "a", encoding = "utf8")
products_file.write(milk + "\n")
