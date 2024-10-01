print("Alo mundo")

numero = int(input("Informe um número: "))
print(f"O número informado foi {numero}")

numero1 = int(input("Informe o primeiro número: "))
numero2 = int(input("Informe o segundo número: "))
soma = numero1 + numero2
print(f"A soma dos números é {soma}")

nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))
nota4 = float(input("Informe a quarta nota: "))
media = (nota1 + nota2 + nota3 + nota4) / 4
print(f"A média das notas é {media}")


metros = float(input("Informe o valor em metros: "))
centimetros = metros * 100
print(f"{metros} metros é igual a {centimetros} centímetros")


raio = float(input("Informe o raio do círculo: "))
area = 3.14 * (raio ** 2)
print(f"A área do círculo é {area}")


lado = float(input("Informe o lado do quadrado: "))
area = lado ** 2
print(f"A área do quadrado é {area}")
print(f"O dobro da área é {area * 2}")


salario_hora = float(input("Informe o salário por hora: "))
horas_trabalhadas = float(input("Informe as horas trabalhadas no mês: "))
salario_total = salario_hora * horas_trabalhadas
print(f"O salário total é R${salario_total:.2f}")


fahrenheit = float(input("Informe a temperatura em Fahrenheit: "))
celsius = 5 * ((fahrenheit - 32) / 9)
print(f"{fahrenheit}°F é igual a {celsius}°C")


celsius = float(input("Informe a temperatura em Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
print(f"{celsius}°C é igual a {fahrenheit}°F")


numero1 = int(input("Informe o primeiro número: "))
numero2 = int(input("Informe o segundo número: "))
numero3 = float(input("Informe o terceiro número: "))
produto = 2 * numero1 * (numero2 / 2)
soma = 3 * numero1 + numero3
cubo = numero3 ** 3
print(f"O produto é {produto}")
print(f"A soma é {soma}")
print(f"O cubo é {cubo}")


altura = float(input("Informe a altura: "))
peso_ideal = (72.7 * altura) - 58
print(f"O peso ideal é {peso_ideal:.2f} kg")


altura = float(input("Informe a altura: "))
genero = input("Informe o gênero (M/F): ")
if genero.upper() == "M":
    peso_ideal = (72.7 * altura) - 58
else:
    peso_ideal = (62.1 * altura) - 44.7
print(f"O peso ideal é {peso_ideal:.2f} kg")


peso_peixes = int(input("Digite o peso dos peixes: "))
limite = 50
excesso = max(0, peso_peixes - limite)
multa = excesso * 4.00
print(f"Excesso: {excesso} kg")
print(f"Multa: R$ {multa}")



salario_hora = float(input("Informe o salário por hora: "))
horas_trabalhadas = float(input("Informe as horas trabalhadas no mês: "))
salario_total = salario_hora * horas_trabalhadas
ir = salario_total * 0.11
inss = salario_total * 0.08
sindicato = salario_total * 0.05
descontos = ir + inss + sindicato
salario_liquido = salario_total - descontos
print(f"Salário Bruto: R${salario_total:.2f}")
print(f"IR (11%): R${ir:.2f}")
print(f"INSS (8%): R${inss:.2f}")
print(f"Sindicato (5%): R${sindicato:.2f}")
print(f"Salário Líquido: R${salario_liquido:.2f}")
