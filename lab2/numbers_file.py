import turtle as t

inp = open('scratch.txt', 'r', encoding='utf8')
n = int(((inp.readline()).strip()))
maps = [[0] * 2 for i in range(n)]

# считывание шрифта из файла
for a in range(0, n):
    for b in range(2):
        str = ((inp.readline()).strip()) #Считываем и обрубаем перенос
        maps[a][b] = list(map(float, str.split())) # Забиваем в массив
inp.close()
for a in range(n):  # вывод считанного лля проверки
    for b in range(2):
        print(maps[a][b])

# Сначала создадим функции для рисования цифр, потом интерфейс для  их вызова


def number(n: int, maps):
    map1 = maps[n][0]
    map2 = maps[n][1]
    for angle, length in map1:
        t.left(angle)
        t.forward(length)
    t.penup()
    for angle, length in map2:
        t.left(angle)
        t.forward(length)
    t.pendown()


# Интерфейс вызова
str = int(input())
str = bin(str)
str = str[2:]
print(str)
for i in str:
    number(int(i), maps)