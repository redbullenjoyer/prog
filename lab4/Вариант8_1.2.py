

# Нерекурсивная (итеративная) версия линеаризации (linearize_iterative)

def linearize_iterative(lst):
    result = []
    stack = [lst]
    while stack:
        current = stack.pop()
        if isinstance(current, list):
            stack.extend(reversed(current))
        else:
            result.append(current)
    return result


if __name__ == "__main__":
    test = [1, 2, [3, 4, [5, [6, []]]]]
    print(linearize_iterative(test))