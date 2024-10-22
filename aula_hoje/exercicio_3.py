import random

class Quad:
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

q = []
for _ in range(400):
    q.append(Quad(random.randint(1, 100)))

area = [quadrado.area() for quadrado in q]

area_maior = area[0]
area_menor = area[0]
indice_area_maior = 0
indice_area_menor = 0

for i in range(1, len(area)):
    if area[i] > area_maior:
        area_maior = area[i]
        indice_area_maior = i
    if area[i] < area_menor:
        area_menor = area[i]
        indice_area_menor = i

for i in range(len(area)):
    print(f"Quadrado {i + 1}: Area = {area}")

print(f"\nO Quadrado {indice_area_maior + 1} tem a maior area: {area_maior}")
print(f"O Quadrado {indice_area_menor+ 1} tem a menor area: {area_menor}")