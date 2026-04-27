
result = 216**6 + 216**4 + 36**6 - 6**14 - 24

s = set()  

n = result
if n == 0:
    s.add(0)
else:
    while n > 0:
        s.add(n % 6)  
        n //= 6

print(f"Результат выражения: {result}")
print(f"Цифры в 6-чной записи: {sorted(s)}")
print(f"Количество различных цифр: {len(s)}")