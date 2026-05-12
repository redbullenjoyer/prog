
# Нерекурсивная версия (sequence_iterative)

def sequence_iterative(k):
    a, b = 1, 1
    for _ in range(2, k + 1):
        a_new = 2 * b + a
        b_new = 2 * a + b
        a, b = a_new, b_new
    return (a, b)


if __name__ == "__main__":
    k = 5
    a, b = sequence_iterative(k)
    print(f"k={k}: a={a}, b={b}")