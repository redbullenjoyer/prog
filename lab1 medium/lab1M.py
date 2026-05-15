

def run1():
    cities = {
        'Moscow': (550, 370),
        'London': (510, 510),
        'Paris': (480, 480),
    }
    distances = {}
    names = list(cities.keys())
    for i in range(len(names)):
        for j in range(len(names)):
            if i != j:
                x1, y1 = cities[names[i]]
                x2, y2 = cities[names[j]]
                dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
                pair = f"{names[i]} - {names[j]}"
                distances[pair] = dist
    print("Distances between towns:")
    for pair, dist in distances.items():
        print(f"{pair}: {dist:.2f}")

def run2():
    radius = 42
    pi = 3.1415926
    area = pi * radius ** 2
    print(round(area, 4))
    point_1 = (23, 34)
    distance_1 = (point_1[0] ** 2 + point_1[1] ** 2) ** 0.5
    print(distance_1 <= radius)
    point_2 = (30, 30)
    distance_2 = (point_2[0] ** 2 + point_2[1] ** 2) ** 0.5
    print(distance_2 <= radius)

def run3():
    print((1 + 2) * 3)
    print((1 * 2 + 3) * 4 + 5)

def run4():
    my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'
    print(my_favorite_movies[:10])
    print(my_favorite_movies[-15:])
    print(my_favorite_movies[12:25])
    print(my_favorite_movies[27:33])

def run5():
    my_family_height = [
        ['мама', 160],
        ['папа', 182],
        ['брат', 179],
        ['дедушка', 177],
        ['бабушка', 160],
    ]
    print(f'Рост отца - {my_family_height[1][1]} см')
    total = sum([h[1] for h in my_family_height])
    print(f'Общий рост моей семьи - {total} см')

def run6():
    zoo = ['lion', 'kangaroo', 'elephant', 'monkey']
    zoo.insert(1, 'bear')
    print(zoo)
    birds = ['rooster', 'ostrich', 'lark']
    zoo.extend(birds)
    print(zoo)
    zoo.remove('elephant')
    print(zoo)
    lion_index = zoo.index('lion')
    lark_index = zoo.index('lark')
    print(f'Лев сидит в {lion_index + 1} клетке')
    print(f'Жаворонок сидит в {lark_index + 1} клетке')

def run7():
    songs = [
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
    total1 = songs[3][1] + songs[5][1] + songs[8][1]
    print(f'Три песни звучат {round(total1, 2)} минут')
    songs_dict = {
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
    total2 = songs_dict['Sweetest Perfection'] + songs_dict['Policy of Truth'] + songs_dict['Blue Dress']
    print(f'А другие три песни звучат {round(total2, 2)} минут')

def run8():
    secret_message = [
        'квевтфпп6щ3стмзалтнмаршгб5длгуча',
        'дьсеы6лц2бане4т64ь4б3ущея6втщл6б',
        'т3пплвце1н3и2кд4лы12чф1ап3бкычаь',
        'ьд5фму3ежородт9г686буиимыкучшсал',
        'бсц59мегщ2лятьаьгенедыв9фк9ехб1а',
    ]
    word1 = secret_message[0][3]
    word2 = secret_message[1][9:13]
    word3 = secret_message[2][5:15:2]
    word4 = secret_message[3][12:6:-1]
    word5 = secret_message[4][20:15:-1]
    decoded = word1 + ' ' + word2 + ' ' + word3 + ' ' + word4 + ' ' + word5
    print(decoded)

def run9():
    garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза')
    meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка')
    garden_set = set(garden)
    meadow_set = set(meadow)
    print(f'Все виды цветов: {garden_set | meadow_set}')
    print(f'Цветы, которые растут и в саду, и на лугу: {garden_set & meadow_set}')
    print(f'Цветы, которые растут в саду, но не растут на лугу: {garden_set - meadow_set}')
    print(f'Цветы, которые растут на лугу, но не растут в саду: {meadow_set - garden_set}')

def run10():
    sweets = {
        'печенье': [
            {'shop': 'пятерочка', 'price': 9.99},
            {'shop': 'ашан', 'price': 10.99},
        ],
        'конфеты': [
            {'shop': 'магнит', 'price': 30.99},
            {'shop': 'пятерочка', 'price': 32.99},
        ],
        'карамель': [
            {'shop': 'магнит', 'price': 41.99},
            {'shop': 'ашан', 'price': 45.99},
        ],
        'пирожное': [
            {'shop': 'пятерочка', 'price': 59.99},
            {'shop': 'магнит', 'price': 62.99},
        ],
    }
    for sweet, shops_list in sweets.items():
        print(f'\n{sweet}:')
        for s in shops_list:
            print(f"  {s['shop']} - {s['price']} руб.")

def run11():
    sweets = {
        'печенье': [
            {'shop': 'пятерочка', 'price': 9.99},
            {'shop': 'ашан', 'price': 10.99},
        ],
        'конфеты': [
            {'shop': 'магнит', 'price': 30.99},
            {'shop': 'пятерочка', 'price': 32.99},
        ],
        'карамель': [
            {'shop': 'магнит', 'price': 41.99},
            {'shop': 'ашан', 'price': 45.99},
        ],
        'пирожное': [
            {'shop': 'пятерочка', 'price': 59.99},
            {'shop': 'магнит', 'price': 62.99},
        ],
    }
    for sweet, shops_list in sweets.items():
        print(f'\n{sweet}:')
        for s in shops_list:
            print(f"  {s['shop']} - {s['price']} руб.")

def main():
    while True:
        print("\nВыберите задание (1–11) или 0 для выхода:")
        choice = input("> ").strip()
        if choice == '0':
            print("Выход.")
            break
        elif choice == '1':
            run1()
        elif choice == '2':
            run2()
        elif choice == '3':
            run3()
        elif choice == '4':
            run4()
        elif choice == '5':
            run5()
        elif choice == '6':
            run6()
        elif choice == '7':
            run7()
        elif choice == '8':
            run8()
        elif choice == '9':
            run9()
        elif choice == '10':
            run10()
        elif choice == '11':
            run11()
        else:
            print("Некорректный ввод. Введите число от 1 до 11 или 0.")

if __name__ == "__main__":
    main()