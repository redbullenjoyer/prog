def repeat_apply(sequence, func, times):
    if times < 1:
        raise ValueError("Количество применений должно быть >= 1")
    
    for element in sequence:
        result = element
        for _ in range(times):
            result = func(result)
        yield result