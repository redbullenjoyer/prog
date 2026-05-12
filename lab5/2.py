#Вариант 8
#Генератор для бесконечной последовательности

def gen_alternating():
    num = 1
    while True:
        if num % 2 == 1:
            yield num
        else:
            yield -num
        num += 1

if __name__ == "__main__":
    print("Чередование знаков (1, -2, 3, -4, ...):")
    alt = gen_alternating()
    for _ in range(10):
        print(next(alt), end=' ')
    print()