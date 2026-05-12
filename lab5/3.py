#Вариант 8
#Генератор для перебора вложенного списка (усложнённый)

def flatten_gen(lst):
    for item in lst:
        if isinstance(item, list):
            yield from flatten_gen(item)
        else:
            yield item

if __name__ == "__main__":
    nested = [1, [2, [3, 4], 5], 6]
    print("Вложенный список:", nested)
    print("Выпрямленный список:")
    for value in flatten_gen(nested):
        print(value, end=' ')
    print()