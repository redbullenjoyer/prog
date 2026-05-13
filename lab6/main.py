# Вариант 8
from my_generators import apply_generator, helpers

def double(x):
    return x * 2

def square(x):
    return x ** 2

numbers = [1, 2, 3, 4]

gen1 = apply_generator.repeat_apply(numbers, double, 3)
helpers.print_generator_result(gen1, "После 3 применений 'double' к [1,2,3,4]:")

gen2 = apply_generator.repeat_apply(numbers, square, 2)
helpers.print_generator_result(gen2, "После 2 применений 'square' к [1,2,3,4]:")