import turtle as t
import random as rand

t.penup()
vx = float(rand.randint(40, 70))  # Скорость по оси Х
vy = float(rand.randint(60, 90))
m = 1  # Масса объекта
ax = ay = 0.0
g = 9.8  # ускорение поля тяжести

k = 0.05  # Коэфициент сопротивления воздуха
dt = 0.03  # Элементарное приращение
T = 0  # Скорость черепахи
fultime = 1500  # Полное время моделирования
scalex = 1  # Масштаб отображения по оси Х
scaley = 1
x = -600.0 * scalex
y = 0.0

timer = 0
t.speed(T)
t.pendown()
while timer < fultime: # сам иттератор
    ay = -(vy * k / m) - g
    ax = -vx * k / m
    vx += ax * dt
    vy += ay * dt
    x += vx * dt + ax * (dt ** 2) / 2
    y += vy * dt + ay * (dt ** 2) / 2
    t.goto(x * scalex, y * scaley)
    timer += dt
    if y < 0:
        y = 0
        vy = -vy
