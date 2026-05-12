#Вариант 8
#Простой генератор квадратов чисел

def gen_squares(n):
    for i in range(1, n + 1):
        yield i * i


if __name__ == "__main__":
    print("Квадраты чисел от 1 до 5:")
    for value in gen_squares(5):
        print(value, end=' ')
    print()  