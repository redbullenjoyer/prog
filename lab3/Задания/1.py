
import itertools

alphabet = ['К', 'А', 'Т', 'Е', 'Р']
count = 0

for word in itertools.product(alphabet, repeat=6):
    if word[0] == 'Р' and word[-1] == 'К':
        count += 1

print(count)