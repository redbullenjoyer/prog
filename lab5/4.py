#Вариант 8
#Генераторное выражение (однострочник)

even_gen = (x for x in range(21) if x % 2 == 0)

if __name__ == "__main__":
    print("Чётные числа от 0 до 20:")
    for value in even_gen:
        print(value, end=' ')
    print()