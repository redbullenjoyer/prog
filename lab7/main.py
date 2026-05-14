
from generators import RepeatApplyGenerator, SquareGenerator

def double(x):
    return x * 2

numbers = [1, 2, 3, 4]

print("генератор приенения")
gen1 = RepeatApplyGenerator(numbers, double, 3)
for value in gen1:
    print(value, end=' ')
print()

print("квадратный генератор")
gen2 = SquareGenerator(numbers)
for value in gen2:
    print(value, end=' ')
print()