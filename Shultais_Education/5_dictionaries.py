'''Цвета радуги, 3

Создайте словарь rainbow, в котором ключами будут английские названия цветов (red, orange, yellow, green, blue, indigo, violet), а значениями их переводы на русский язык (красный, оранжевый, желтый, зеленый, голубой, синий, фиолетовый).
 '''
rainbow = {
            "red" : "красный",
            "orange" : "оранжевый",
            "yellow" : "желтый",
            "green" : "зеленый",
            "blue" : "голубой",
            "indigo" : "синий",
            "violet" : "фиолетовый"
            }


'''Доступ по ключу

Используя словарь из прошлой задачи, напишите программу, которая получает первым аргументом командной строки название ключа словаря, а затем выводит значение связанное с этим ключом.
Пример использования:
> python program.py red
> красный
 '''

import sys
key = sys.argv[1]
rainbow = {
            "red" : "красный",
            "orange" : "оранжевый",
            "yellow" : "желтый",
            "green" : "зеленый",
            "blue" : "голубой",
            "indigo" : "синий",
            "violet" : "фиолетовый"
            }
print(rainbow[key])


'''Доход за квартал

В редакторе ниже создан словарь quarters, который хранит поквартальные доходы. Каждому кварталу соответствует определенная пара ключ: значение. В качестве значений выступает список месячных доходов.

Напишите программу, которая принимает из первого аргумента командной строки номер квартала, а затем выводит доход за этот квартал.
Пример использования:
> python program.py 1
> 847
 '''

import sys
q = sys.argv[1]
key = str("quarter_"+q)
quarters = {
    "quarter_1": [137, 565, 145],
    "quarter_2": [145, 738, 1145],
    "quarter_3": [1345, 1141, 879],
    "quarter_4": [784, 689, 543]
}
print(sum(quarters[key]))

'''Числа на русском и английском

Ниже в редакторе находится словарь digits, который содержит набор чисел и их названия на русском и английском языках. Обратите внимание, что ключами словаря выступают целые числа (так тоже можно), а значениями вложенные словари.

Напишите программу, которая принимает из аргументов командной строки два параметра: цифру и язык, а затем выводит название цифры на этом языке.

Учитывайте, что если ключ словаря задан числом, то при доступе по ключу, в квадратных скобках нужно также указывать число.
Пример использования:
> python program.py 4 ru
> четыре
 '''

import sys
# Принимаем цифру и язык
number, language = int(sys.argv[1]), sys.argv[2].lower().strip()
digits = {
    1: {"ru": "один", "en": "one"},
    2: {"ru": "два", "en": "two"},
    3: {"ru": "три", "en": "three"},
    4: {"ru": "четыре", "en": "four"},
    5: {"ru": "пять", "en": "five"},
    6: {"ru": "шесть", "en": "six"},
    7: {"ru": "семь", "en": "seven"},
    8: {"ru": "восемь", "en": "eight"},
    9: {"ru": "девять", "en": "nine"},
    0: {"ru": "ноль", "en": "zero"}
}
print(digits[number][language])


'''Рентабельность

Рентабельность продаж рассчитывается по следующей формуле: (доходы − расходы) / доходы x 100.
В редакторе ниже находится словарь finance, который содержит данные по доходам (income) и расходам (expenses) за все месяцы 2019 и 2020 годов.

Напишите программу, которая получает из аргументов командной строки два параметра: год и месяц, а затем выводит рентабельность продаж за этот период.
Пример использования:
> python program.py 2019 1
> 65%
 '''

import sys
year, month = int(sys.argv[1]), int(sys.argv[2])
finance = {
    2019: {
        1: {"income": 987, "expenses": 345},
        2: {"income": 1987, "expenses": 1247},
        3: {"income": 3011, "expenses": 2098},
        4: {"income": 3400, "expenses": 2798},
        5: {"income": 1987, "expenses": 1783},
        6: {"income": 2684, "expenses": 2004},
        7: {"income": 2008, "expenses": 1555},
        8: {"income": 2498, "expenses": 2210},
        9: {"income": 1714, "expenses": 789},
        10: {"income": 6971, "expenses": 6971},
        11: {"income": 345, "expenses": 147},
        12: {"income": 2487, "expenses": 2101}
    },
    2020: {
        1: {"income": 1487, "expenses": 578},
        2: {"income": 2654, "expenses": 1743},
        3: {"income": 3654, "expenses": 2478},
        4: {"income": 3614, "expenses": 6971},
        5: {"income": 2971, "expenses": 3240},
        6: {"income": 2876, "expenses": 2147},
        7: {"income": 3456, "expenses": 3047},
        8: {"income": 3129, "expenses": 3017},
        9: {"income": 1998, "expenses": 1149},
        10: {"income": 2478, "expenses": 2014},
        11: {"income": 2649, "expenses": 2970},
        12: {"income": 3001, "expenses": 1345}
    }
}
rent = round(100-100*(finance[year][month]["expenses"]) / (finance[year][month]["income"]))
print("{}%" .format(rent))

'''Сравнение периодов

В списке fin ниже, хранятся словари с финансовой информацией за год. income — это доходы предприятия за месяц, а expenses — расходы. Всего в списке 12 словарей, по одному на каждый месяц года.

Напишите программу, которая принимает из аргументов командной строки два параметра: начальный и конечный месяц, а затем сравнивает между собой прибыли переданных периодов.

Номера месяцев передаются в соответствии их календарному порядку: 1 — январь, 12 — декабрь. Прибыль за месяц рассчитывается по следующей формуле: доход − расход. Программа должна вывести насколько прибыль второго периода больше/меньше первого.
Пример использования (сравниваем январь и февраль).
Прибыль в феврале на 98 рублей больше:
> python program.py 1 2
> 98
 '''


import sys
month_1, month_2 = int(sys.argv[1])-1, int(sys.argv[2])-1
fin = [
    {"income": 987, "expenses": 345},
    {"income": 1987, "expenses": 1247},
    {"income": 3011, "expenses": 2098},
    {"income": 3400, "expenses": 2798},
    {"income": 1987, "expenses": 1783},
    {"income": 2684, "expenses": 2004},
    {"income": 2008, "expenses": 1555},
    {"income": 2498, "expenses": 2210},
    {"income": 1714, "expenses": 1789},
    {"income": 6971, "expenses": 6971},
    {"income": 345, "expenses": 147},
    {"income": 2487, "expenses": 2101}
]
profit_1 = fin[month_1]["income"]-fin[month_1]["expenses"]
profit_2 = fin[month_2]["income"]-fin[month_2]["expenses"]
profit = profit_2 - profit_1
print(profit)

'''Последний рейтинг

Ниже находится словарь imdb с рейтингом фильмов по версии IMDB. Ключ словаря отвечает за идентификатор фильма, а значение содержит список словарей, каждый из которых состоит из одного элемента с ключом rating.

Напишите программу, которая получает из аргументов командной строки идентификатор фильма, а затем выводит последнее значение рейтинга, который ему поставили пользователи.
Пример использования:
> python program.py 68646
> 9'''

import sys
id_film = int(sys.argv[1])
# Данные.
imdb = {
    111161: [{"rating": 8}, {"rating": 9}, {"rating": 10}, {"rating": 9}, {"rating": 10}],
    68646: [{"rating": 8}, {"rating": 10}, {"rating": 9}, {"rating": 9}, {"rating": 9}],
    468569: [{"rating": 10}, {"rating": 10}, {"rating": 8}, {"rating": 8}],
    71562: [{"rating": 9}, {"rating": 9}, {"rating": 10}],
    167260: [{"rating": 8}, {"rating": 7}, {"rating": 9}, {"rating": 9}, {"rating": 8}, {"rating": 9}]
}
print(imdb[id_film][-1]["rating"])

'''Изменение значения

Ниже в редакторе содержится словарь user с пользовательскими данными. Напишите программу, которая принимает из аргументов командной строки два параметра: ключ и значение, а затем обновляет значение в словаре user если ключ существует или добавляет в словарь новый ключ с переданным значением.
Пример использования
> python program.py age 18
> {'first_name': 'Егор', 'last_name': 'Михеев', 'sex': 'm', 'age': '18'}'''

import sys
key, value = sys.argv[1], sys.argv[2]
user = {
    "first_name": "Егор",
    "last_name": "Михеев",
    "sex": "m"
}
user_new = {
    key: value,
   }

user.update(user_new)
print(user)


'''Чиним программу

Начинающий разработчик написал программу, которая принимает из аргументов командной строки модель, новую цену и новое количество товара, а затем меняет эти данные в словаре product. Но программа не работает, исправьте в ней все ошибки.
Пример использования:

> python program.py UE32M5550AU 23990 3
> {'model': 'UE32M5550AU', 'brand': 'Samsung', 'price': 23990, 'count': 3}'''


import sys

# Получаем данные.
new_model = sys.argv[1]
new_price = int(sys.argv[2])
new_count = int(sys.argv[3])

# Исходный словарь.
product = {
    "model": "UE43NU7097U",
    "brand": "Samsung",
    "price": 27990,
    "count": 7
}

# Обновляем данные.
#product["count"] = new_count
product.update(model = new_model, price = new_price, count = new_count)

# Выводим результат.
print(product)

'''Изменение значения

Ниже в редакторе содержится словарь user с пользовательскими данными. Напишите программу, которая принимает из аргументов командной строки два параметра: ключ и значение, а затем обновляет значение в словаре user если ключ существует или добавляет в словарь новый ключ с переданным значением.
Пример использования
> python program.py age 18
> {'first_name': 'Егор', 'last_name': 'Михеев', 'sex': 'm', 'age': '18'}
 '''
import sys
key, value = sys.argv[1], sys.argv[2]
user = {
    "first_name": "Егор",
    "last_name": "Михеев",
    "sex": "m"
}
user_new = {
    key: value,
   }

user.update(user_new)
print(user)

'''Чиним программу

Начинающий разработчик написал программу, которая принимает из аргументов командной строки модель, новую цену и новое количество товара, а затем меняет эти данные в словаре product. Но программа не работает, исправьте в ней все ошибки.
Пример использования:

> python program.py UE32M5550AU 23990 3
> {'model': 'UE32M5550AU', 'brand': 'Samsung', 'price': 23990, 'count': 3}'''

import sys

# Получаем данные.
new_model = sys.argv[1]
new_price = int(sys.argv[2])
new_count = int(sys.argv[3])

# Исходный словарь.
product = {
    "model": "UE43NU7097U",
    "brand": "Samsung",
    "price": 27990,
    "count": 7
}

# Обновляем данные.
#product["count"] = new_count
product.update(model = new_model, price = new_price, count = new_count)

# Выводим результат.
print(product)


'''Значения по умолчанию

Напишите программу, которая принимает из аргументов командной строки один аргумент — ключ словаря, а затем выводит значение словаря car, связанное с этим ключом. Если значения с таким ключом нет, то программа должна выводить слово «неизвестно» (без кавычек).
Пример использования:
> python program.py mark
> Nissan
> python program.py run
> неизвестно
 '''









