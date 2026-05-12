#Рекурсивная версия линеаризации (linearize_recursive)

def linearize_recursive(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(linearize_recursive(item))
        else:
            result.append(item)
    return result


if __name__ == "__main__":
    test = [1, 2, [3, 4, [5, [6, []]]]]
    print(linearize_recursive(test))