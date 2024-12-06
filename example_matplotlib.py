import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

x = np.linspace(-1, 3, 100)
def g(_x):
    return np.where(_x > 0., _x**2., 0.)

# Построение графика
plt.plot(x, g(x), label="g(x)", color='darkgreen', linestyle='-')

# Ограничения осей
plt.xlim(-1, 3)
plt.ylim(0, 9)

# Настройка сетки
plt.grid(which='both', linestyle=':', linewidth=0.5)
plt.minorticks_on()

# Подписи осей
plt.xlabel("x")
plt.ylabel("y")

# Заголовок и легенда
plt.title("График функции g(x)")
plt.legend(fontsize=12)  # Увеличение шрифта легенды

# Добавление стрелки с увеличенным шрифтом подписи
plt.annotate("Начало роста", xy=(0, 0), xytext=(-0.5, 2),
             fontsize=12,  # Увеличение шрифта подписи
             arrowprops=dict(facecolor='black', arrowstyle='->'))

# Добавление правой и верхней границ
plt.gca().spines['right'].set_visible(True)
plt.gca().spines['top'].set_visible(True)

# Отображение графика
plt.show()

plt.savefig("g(x).png")

### Разделение рисунка на графики

fig, ax = plt.subplots(1,2)

ax[0].plot(x, g(x), label="g(x)", color='darkgreen', linestyle='-')
ax[1].plot(x, g(np.sqrt(x)), label=r"g($\sqrt{x}$))", color='darkblue', linestyle=':')

# Ограничения осей
ax[0].set_xlim(-1, 3)
ax[0].set_ylim(0, 9)

ax[1].set_xlim(-1, 3)
ax[1].set_ylim(0, 9)

# Настройка сетки
ax[0].grid(which='both', linestyle=':', linewidth=0.5)
ax[0].minorticks_on()

ax[1].grid(which='both', linestyle=':', linewidth=0.5)
ax[1].minorticks_on()

# Подписи осей
ax[0].set_xlabel("x")
ax[0].set_ylabel("y")

ax[1].set_xlabel("x")
ax[1].set_ylabel("y")

ax[0].legend(fontsize=12) 

ax[1].legend(fontsize=12) 

fig.savefig("g(x)_adv.png")

### Анимация

# Создание фигуры и осей
fig, ax = plt.subplots()
line, = ax.plot(x, g(x), color='darkgreen', label=r"g(x)$\cdot e^{-t}$")

# Настройка осей
ax.set_xlim(-1, 3)
ax.set_ylim(0, 9)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()
ax.grid()

N = 100

# Функция для обновления графика
def update(frame):
    t = frame/N
    y = g(x) * np.exp(-t)
    line.set_data(x, y)
    return line,

# Анимация
frames = np.linspace(1, N, 100)  # Временные шаги
ani = FuncAnimation(fig, update, frames=frames, blit=True)

# Отображение анимации
plt.title(r"Анимация функции g(x)$\cdot e^{-t}$")
plt.show()