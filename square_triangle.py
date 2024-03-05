import numpy as np
import matplotlib.pyplot as plt
from random import *
with open("pos.dat", "r") as fin:
    data = fin.readlines()

X_ = [float(line.split()[0]) for line in data[0:]]
Y_ = [float(line.split()[1]) for line in data[0:]]


y_ = np.array(X_)
x_ = np.array(Y_)



plt.plot(x_, y_, label='Данные 1',  markersize = 3, color = 'black',  linewidth = 1)


x0 = 0.0
y0 = 100.0
vx0 = 1
vy0 = 1
g = -9.81

timeline = np.linspace(0, 10, 100)

x = x0 + vx0 * timeline
y = y0 + vy0 * timeline + 0.5 * g * timeline**2
plt.plot(x, y , label='Данные 2',  markersize = 3, color = 'red',  linewidth = 1)


plt.grid()
plt.legend()

plt.show()


import itertools
import numpy as np
import math
import decimal

class Vector():
    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        elif isinstance(other, (int, float)):
            return Vector(self.x + other, self.y + other, self.z + other)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        if isinstance(other, Vector):
            return np.dot([self.x, self.y, self.z], [other.x, other.y, other.z])
        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other, self.z * other)

    def __abs__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def __str__(self):
        return f"x = {self.x}, y = {self.y}, z = {self.z}"

def center_of_mass(*args):
    x = [coord[0] for coord in args]
    y = [coord[1] for coord in args]
    z = [coord[2] for coord in args]

    len_lists = len(x)

    cm_x = sum(x) / len_lists
    cm_y = sum(y) / len_lists
    cm_z = sum(z) / len_lists

    return Vector(cm_x, cm_y, cm_z)

def max_square(vectors):
    square_list = []
    for i in itertools.combinations(vectors, 3):
        v1, v2, v3 = Vector(*i[0]), Vector(*i[1]), Vector(*i[2])

        len_1 = decimal.Decimal(abs(v1 - v2))
        len_2 = decimal.Decimal(abs(v2 - v3))
        len_3 = decimal.Decimal(abs(v1 - v3))

        p = decimal.Decimal((len_1 + len_2 + len_3) / 2)

        square = decimal.Decimal(math.sqrt(p * abs(p - len_1) * abs(p - len_2) * abs(p - len_3)))
        square_list.append(square)

    return round(max(square_list), 5)

print('Введите радиус-векторы точек (координаты) каждый в новой строчке.')
vectors = []
while True:
    try:
        lines = input().split()
        if not lines:
            break
        vectors.append(list(map(float, lines)))
    except ValueError:
        print("Некорректный ввод. Введите числа.")

sum_vector = Vector(0, 0, 0)
for v in vectors:
    sum_vector += Vector(*v)

center_of_mass_vector = center_of_mass(*vectors)
print("Сумма векторов:", sum_vector)
print("Центр масс:", center_of_mass_vector)
print("Максимальная площадь:", max_square(vectors))


