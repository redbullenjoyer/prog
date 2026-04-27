import numpy as np
import matplotlib.pyplot as plt

#Функция из варианта 2

def f(x):
    # Для одиночного числа
    if isinstance(x, (int, float)):
        if x <= 0.25:
            return np.exp(np.sin(x))
        else:
            return np.exp(x) - 1 / np.sqrt(x)
    
    # Для массива
    result = np.zeros_like(x)
    mask1 = x <= 0.25
    result[mask1] = np.exp(np.sin(x[mask1]))
    mask2 = x > 0.25
    result[mask2] = np.exp(x[mask2]) - 1 / np.sqrt(x[mask2])
    return result


def derivative(func, x, eps=1e-6):
    return (func(x + eps) - func(x)) / eps
x0 = 0.3                     # точка касания
x = np.linspace(0.01, 0.5, 500)

# Значения функции и касательной
y = f(x)
y0 = f(x0)
k = derivative(f, x0)
tangent = y0 + k * (x - x0)

# Построение графика
plt.figure(figsize=(10, 6))

# График функции
plt.plot(x, y, color='hotpink', linewidth=2, label='f(x)')

# Касательная
plt.plot(x, tangent, color='pink', linestyle='--', linewidth=2, label='Касательная')

# Точка касания
plt.plot(x0, y0, 'r*',color='deeppink', markersize=12, label='Точка касания(x=0.3)')

# Аннотация
plt.annotate(f'x₀ = {x0}\ny₀ = {y0:.3f}',
             xy=(x0, y0),
             xytext=(0.36, 1.8),
             arrowprops=dict(arrowstyle='->', color='plum'),
             fontsize=10,
             bbox=dict(boxstyle="round,pad=0.3", facecolor="pink", alpha=0.5))

# Оформление
plt.grid(True, linestyle='--', alpha=0.7)
plt.xlabel('x', fontsize=12)
plt.ylabel('f(x)', fontsize=12)
plt.title('=^..^= График функции и касательная =^..^=', fontsize=14)
plt.legend(loc='best')
plt.tight_layout()


plt.show()