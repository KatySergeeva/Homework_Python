import math

def square(x):
    return math.ceil(x**2)

x = float(input("Введите число: "))
print(f"площадь квадрата: {square(x)}")