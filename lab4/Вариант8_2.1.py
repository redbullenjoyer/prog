
# Рекурсивная версия (sequence_recursive)

def sequence_recursive(k):
    if k == 1:
        return (1, 1)
    a_prev, b_prev = sequence_recursive(k - 1)
    a_k = 2 * b_prev + a_prev
    b_k = 2 * a_prev + b_prev
    return (a_k, b_k)


if __name__ == "__main__":
    k = 5
    a, b = sequence_recursive(k)
    print(f"k={k}: a={a}, b={b}")