import numpy as np

###Примеры из презентации

#Создание векторов
vector = np.array([1, 2, 3])
arr = np.arange(0, 10, 1)
x = np.linspace(-np.pi, np.pi, 5)

#print(f"vector = {vector},\narr = {arr},\nx = {x}\n")

#Работа с массивами numpy
norm = np.linalg.norm(vector)
arr_squared = np.power(arr, 2)
y1 = 2 * x + np.pi
y2 = np.sin(x)

def f(_x):
    return np.sin(_x) ** 2 + np.cos(_x) ** 2 

y3 = f(x)

#print(f"norm = {norm},\narr_sq = {arr_squared},\ny1 = {y1},\ny2 = {y2},\ny3 = {y3}\n")

#Метод where и его применение для создания функций
x = np.linspace(-1, 3, 100)

def g(_x):
    return np.where(_x > 0., _x**2., 0.)

#print(f"g(x) = {g(x)}")

#Визуализация (подробнее в example_matplotlib.py)
import matplotlib.pyplot as plt

plt.plot(x, g(x))
plt.savefig("g(x).png")

#Метод np.trapz
I_calc = np.trapz(g(x), x)

print(f"I_calc = {Icalc}")
