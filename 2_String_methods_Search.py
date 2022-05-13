Только рубли

Напишите программу, которая получает из первого аргумента командной строки число содержащее сумму товара в рублях с копейками, а после выводит только рубли. Используйте только возможности строк.
Пример использования в командной строке Windows:
> python program.py 125.78
> 125

import sys
cash = sys.argv[1]
point_position = cash.find(".")
cash = cash[:point_position]
print(cash)

# =========================================================

H1-заголовок

Напишите программу, которая получает из первого аргумента командной строки HTML-текст, а после извлекает из него содержание <H1>-заголовка.
Пример использования в командной строке Windows:
> python program.py '<p>текст</p><h1>Заголовок</h1><p>еще текст</p>'
> Заголовок


import sys
string = sys.argv[1]
H1_start_position = string.find("h1>")+3
H1_end_position = string.find("</h1")
print(string[H1_start_position:H1_end_position])


# =========================================================

Меняем заголовок

В прошлом задании вы научились определять содержание H1-заголовка, теперь надо его изменить.

Напишите программу, которая получает из первого аргумента командной строки HTML-текст, а из второго параметра значение для заголовка. После программа должна заменить содержание <H1>-заголовка на полученное значение.
Пример использования в командной строке Windows:
> python program.py "<p>текст</p><h1>Заголовок</h1><p>еще текст</p>" "Главный"
> <p>текст</p><h1>Главный</h1><p>еще текст</p>


import sys
text  = sys.argv[1]
text2 = sys.argv[2]
start_h1 = text.find("<h1>")+4
end_h1 = text.find("</h1>")
text = text[:start_h1]+text2+text[end_h1:]
print(text)


