
results = []

for a in range(10):
    for b in range(10):
        
        num_str = f"12345{a}7{b}8"
        number = int(num_str)
        
        if number % 23 == 0:
            results.append((number, number // 23))

# сортируем результаты по возрастанию
results.sort()

# ыыводим в таблицу
print("Число      | Результат деления на 23")
print("-" * 35)
for num, div in results:
    print(f"{num}      | {div}")