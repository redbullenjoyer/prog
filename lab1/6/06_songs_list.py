#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть список песен группы Depeche Mode со временем звучания с точностью до долей минут
# Точность указывается в функции round(a, b)
# где a, это число которое надо округлить, а b количество знаков после запятой
# более подробно про функцию round смотрите в документации https://docs.python.org/3/search.html?q=round

violator_songs_list = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]

# распечатайте общее время звучания трех песен: 'Halo', 'Enjoy the Silence' и 'Clean' в формате
#   Три песни звучат ХХХ.XX минут
# Обратите внимание, что делать много вычислений внутри print() - плохой стиль.
# Лучше заранее вычислить необходимое, а затем в print(xxx, yyy, zzz)

# Находим время звучания каждой песни из списка
halo_time = violator_songs_list[3][1]  # 'Halo' под индексом 3
enjoy_time = violator_songs_list[5][1]  # 'Enjoy the Silence' под индексом 5
clean_time = violator_songs_list[8][1]  # 'Clean' под индексом 8

# Суммируем время
total_time_1 = halo_time + enjoy_time + clean_time

# Округляем результат до 2 знаков после запятой
total_time_rounded_1 = round(total_time_1, 2)

# Выводим результат
print(f'Три песни звучат {total_time_rounded_1} минут')

# Есть словарь песен группы Depeche Mode
violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}

# распечатайте общее время звучания трех песен: 'Sweetest Perfection', 'Policy of Truth' и 'Blue Dress'
#   А другие три песни звучат ХХХ минут

# Находим время звучания каждой песни из словаря
sweetest_time = violator_songs_dict['Sweetest Perfection']
policy_time = violator_songs_dict['Policy of Truth']
blue_dress_time = violator_songs_dict['Blue Dress']

# Суммируем время
total_time_2 = sweetest_time + policy_time + blue_dress_time

# Округляем результат до 2 знаков после запятой
total_time_rounded_2 = round(total_time_2, 2)

# Выводим результат
print(f'А другие три песни звучат {total_time_rounded_2} минут')