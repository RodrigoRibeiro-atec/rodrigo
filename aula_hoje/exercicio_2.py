#Crie 4 Quadrados 
#indique o que tem a maior area
def calcular_area_quadrados(lados):
    areas = {}
    for i, lado in enumerate(lados):
        area = lado ** 2
        areas[f'Quadrado {chr(65 + i)}'] = area
    return areas

lados = [2, 3, 4, 5]

areas_quadrados = calcular_area_quadrados(lados)

for quadrado, area in areas_quadrados.items():
    print(f'{quadrado}: Área = {area}')

quadrado_maior_area = None
maior_area = 0

for quadrado, area in areas_quadrados.items():
    if area > maior_area:
        maior_area = area
        quadrado_maior_area = quadrado

print(f'\nO quadrado com a maior área é o {quadrado_maior_area}, com uma área de {maior_area}.')