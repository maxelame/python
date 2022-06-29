'''Проверка пароля

В редакторе ниже находится переменная password с правильным паролем пользователя. Напишите программу, которая первым аргументом командной строки принимает пароль, а затем, проверяет, верный ли он.

Если переданный пароль верный, то программа должна вывести "Доступ открыт", а если пароль неверный, то "Доступ закрыт".
Пример использования:
> python program.py admin
> Доступ закрыт
 '''

import sys
new_password  = sys.argv[1]
password = "idY*49amd6z"

if new_password == password:
    print("Доступ открыт")
else:
    print("Доступ закрыт")

'''Проверка реального пароля

В реальных программах пароли хранят в зашифрованном виде, чтобы в случае утечки их было сложно взломать. Когда пользователь пытается авторизоваться на сайте, то его пароль сперва зашифровывается, а затем этот шифр сравнивается с зашифрованным паролем в программе или в базе данных.

Простейшая схема шифрования с помощью алгоритма md5* выглядит так:

# Импортируем в программу библиотеку для шифрования.
import hashlib 

# Задаем "сырой" (незашифрованный) пароль.
raw_password = 'password'

# Кодируем "сырой" пароль.
# Нужно для того, чтобы воспользоваться md5.
raw_password = raw_password.encode()

# Получаем шифр-объект.
hash_password = hashlib.md5(raw_password)

# Получаем зашифрованный пароль.
hash_password = hash_password.hexdigest()

# Выводим зашифрованный пароль.
print(hash_password)
5f4dcc3b5aa765d61d8327deb882cf99

# Именно строка вида "5f4dcc3b5aa765d61d8327deb882cf99" 
# обычно хранится в программе или базе данных.

В редакторе ниже в переменной hash_password хранится зашифрованный пароль. Напишите программу, которая первым аргументом командной строки принимает "сырой" пароль пользователя, а затем, проверяет, верный ли он.

Если переданный пароль верный, то программа должна вывести "Доступ открыт", а если пароль неверный, то "Доступ закрыт".
Пример использования:
> python program.py admin
> Доступ закрыт

Примечание. В настоящий момент алгоритм md5 является небезопасным. Не используйте его в реальных программах.'''

import sys
password = sys.argv[1]
import hashlib
# Задаем "сырой" (незашифрованный) пароль.
raw_password = password
# Кодируем "сырой" пароль.
# Нужно для того, чтобы воспользоваться md5.
raw_password = raw_password.encode()
# Получаем шифр-объект.
new_hash_password = hashlib.md5(raw_password)

# Получаем зашифрованный пароль.
new_hash_password = new_hash_password.hexdigest()

hash_password = 'c8b667f4e6953d59b6ae9b9659772333'

if new_hash_password == hash_password:
    print("Доступ открыт")
else:
    print("Доступ закрыт")


'''Четность числа

Напишите программу, которая первым аргументом командной строки принимает целое число, а затем выводит слово "четное" если число четное и "нечетное" в противном случае.
Пример использования:
> python program.py 17
> нечетное'''

import sys
number = int(sys.argv[1])
if number % 2:
    print("нечетное")
else:
    print("четное")

'''Сравнение целых чисел

Напишите программу, которая принимает из аргументов командной строки два произвольных целых числа, а затем выводит то, которое больше по значению. Если числа равны, то можно выводить любое.
Пример использования:
> python program.py 17 33
> 33'''

import sys
numbers = list(map(int, sys.argv[1:]))
#numbers.sort(key = int)
#print(numbers[-1])
if numbers[0] > numbers[-1]:
    print(numbers[0])
else:
    print(numbers[-1])
#if numbers[0] < numbers[-1]:
#    print(numbers[-1])
#if numbers[0] == numbers[-1]:
#    print(numbers[0])

'''Цены на 99

Напишите программу, которая первым аргументом командной строки принимает цену товара, а затем, если цена оканчивается на 99, увеличивает её на единицу. В остальных случаях цену менять не нужно.

В конце программа должна вывести итоговую цену товара.
Пример использования:
> python program.py 121
> 121
> python program.py 199
> 200'''

import sys
number = int(sys.argv[1])
list_number = list(sys.argv[1])
#print(list_number)
if list_number[-1]==list_number[-2]=='9':
    print(number+1)
else:
    print(number)

'''Проверка длины пароля

В переменной password содержится пароль введенный пользователем. Выведите фразу «Пароль слишком короткий» (без кавычек), если длина пароля меньше 6 символов и фразу «Пароль подходит» в противном случае.'''

import sys
password = sys.argv[1]
if len(password) < 6:
    print("Пароль слишком короткий")
else:
    print("Пароль подходит")

'''Новый товар

Чтобы проверить, есть ли в списке элемент, нужно воспользоваться оператором in или not in:

values = [1, 2, 3, 5, 8, 13]
print(1 in values)
True
print(4 in values)
False
print(1 not in values)
False
print(4 not in values)
True

Так как оператор in возвращает True или False, то всё выражение value in values можно использовать в условиях:

if value in values:
    ...

В редакторе ниже находится список products с товарами. Напишите программу, которая первым аргументом командной строки принимает название товара, а затем, если переданного товара в списке нет, то добавляет его туда. Если переданный товар уже есть в списке, то ничего делать не надо.

В конце программа должна отсортировать список и вывести все товары через запятую с пробелом.
Пример использования:
> python program.py Огурцы
> Масло, Молоко, Овсянка, Огурцы, Хлеб, Яйца
'''
import sys
# получаем строку
product = sys.argv[1]
# есть список
products = ["Молоко", "Масло", "Хлеб", "Овсянка", "Яйца"]
# проверяем есть ли new_product в products
if product not in products:
    products.append(product)
# сортируем списки
products.sort()
# выводим
print(", ".join(products))

'''Авторизация

В редакторе ниже находится словарь users, который в качестве ключей хранит имена пользователей, в качестве значений их пароли.

Напишите программу, которая первым аргументом командной строки принимает имя пользователя, а вторым — его пароль. Далее программа должна проверить переданные логин и пароль и вывести "Доступ открыт" если пароль верный и "Доступ закрыт" если пароль ошибочный.

Если пользователя, который передается в программу, в словаре нет, то нужно вывести "Пользователь не найден".
Пример использования:
> python program.py user2 abcde
> Доступ открыт
 '''

"""
import sys
user, password = sys.argv[1], sys.argv[2]
users = {
    "user1": "password1",
    "user2": "abcde",
    "user3": "123456",
    "user4": "lovelove",
    "user5": "kdmUdmk84M",
}
if user not in users:
    print ("Пользователь не найден")
elif user in users:
    if users.get(user) == password:
        print ("Доступ открыт")
    else:
        print ("Доступ закрыт")
"""
import sys

users = {
    "user1": "password1",
    "user2": "abcde",
    "user3": "123456",
    "user4": "lovelove",
    "user5": "kdmUdmk84M",
}

# Получаем имя пользователя.
username = sys.argv[1]
password = sys.argv[2]

# Получаем пароль пользователя.
user_password = users.get(username)

if user_password is None:
    print("Пользователь не найден")
elif user_password == password:
    print("Доступ открыт")
else:
    print("Доступ закрыт")


'''Проверка длины пароля, часть 2

В переменной password содержится пароль введенный пользователем.
Выведите фразу «Пароль слишком короткий» (без кавычек), если длина пароля меньше 6 символов.
Если длина от 6 до 8 символов, то выведите «Хорошо, но можно и лучше».
Если длина более 8 символов — «Пароль подходит».
 
'''
