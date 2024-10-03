#Página 1

print("Enter two numbers:")
num1 = float(input("Number 1: "))
num2 = float(input("Number 2: "))

if num1 > num2:
    print("The larger number is:", num1)
else:
    print("The larger number is:", num2)
    
print("Enter a value:")
value = float(input("Value: "))

if value > 0:
    print("The value is positive.")
else:
    print("The value is negative.")
    
print("Enter a letter:")
letter = input("Letter: ")

if letter.upper() == "F":
    print("F - Feminino")
elif letter.upper() == "M":
    print("M - Masculino")
else:
    print("Sexo Inválido")
    
print("Enter a letter:")
letter = input("Letter: ")

vowels = "AEIOUaeiou"
if letter in vowels:
    print("The letter is a vowel.")
else:
    print("The letter is a consonant.")
    
    
print("Enter two grades:")
grade1 = float(input("Grade 1: "))
grade2 = float(input("Grade 2: "))

average = (grade1 + grade2) / 2

if average >= 7:
    print("Aprovado")
elif average == 10:
    print("Aprovado com Distinção")
else:
    print("Reprovado")
    

print("Enter three numbers:")
num1 = float(input("Number 1: "))
num2 = float(input("Number 2: "))
num3 = float(input("Number 3: "))

if num1 > num2 and num1 > num3:
    print("The largest number is:", num1)
elif num2 > num1 and num2 > num3:
    print("The largest number is:", num2)
else:
    print("The largest number is:", num3)
    
print("Introduza os preços de três produtos:")
preco1 = float(input("Preço 1: "))
preco2 = float(input("Preço 2: "))
preco3 = float(input("Preço 3: "))

if preco1 < preco2 and preco1 < preco3:
    print("Você deve comprar o produto 1")
elif preco2 < preco1 and preco2 < preco3:
    print("Você deve comprar o produto 2")
else:
    print("Você deve comprar o produto 3")
    
    
print("Em que turno você estuda?")
turno = input("Turno: ")

if turno.upper() == "M":
    print("Bom Dia!")
elif turno.upper() == "V":
    print("Boa Tarde!")
elif turno.upper() == "N":
    print("Boa Noite!")
else:
    print("Valor Inválido!")
    
    
print("Introduza o salário atual:")
salario = float(input("Salário: "))

if salario <= 280:
    aumento = salario * 0.20
elif salario <= 700:
    aumento = salario * 0.15
elif salario <= 1500:
    aumento = salario * 0.10
else:
    aumento = salario * 0.05

novo_salario = salario + aumento

print("O salário antes do reajuste é:", salario)
print("O percentual de aumento aplicado é:", aumento / salario * 100, "%")
print("O valor do aumento é:", aumento)
print("O novo salário é:", novo_salario)


print("Introduza um número:")
numero = int(input("Número: "))

if numero == 1:
    print("Domingo")
elif numero == 2:
    print("Segunda-feira")
elif numero == 3:
    print("Terça-feira")
elif numero == 4:
    print("Quarta-feira")
elif numero == 5:
    print("Quinta-feira")
elif numero == 6:
    print("Sexta-feira")
elif numero == 7:
    print("Sábado")
else:
    print("Valor inválido")
    
    
print("Introduza as duas notas parciais:")
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))

media = (nota1 + nota2) / 2

if media >= 9 and media <= 10:
    conceito = "A"
elif media >= 7.5 and media < 9:
    conceito = "B"
elif media >= 6 and media < 7.5:
    conceito = "C"
elif media >= 4 and media < 6:
    conceito = "D"
else:
    conceito = "E"

if conceito in ["A", "B", "C"]:
    print("Aprovado")
else:
    print("Reprovado")

print("Notas:", nota1 , nota2)
print("Média:", media)
print("Conceito:", conceito)


print("Introduza os 3 lados de um triângulo:")
lado1 = float(input("Lado 1: "))
lado2 = float(input("Lado 2: "))
lado3 = float(input("Lado 3: "))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    if lado1 == lado2 and lado2 == lado3:
        print("O triângulo é equilátero")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("O triângulo é isósceles")
    else:
        print("O triângulo é escaleno")
else:
    print("Os lados não formam um triângulo")
    
    
print("Introduza um número correspondente a um determinado ano:")
ano = int(input("Ano: "))

if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    print("O ano é bissexto")
else:
    print("O ano não é bissexto")
    
    
print("Introduza as três notas parciais:")
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print("Aprovado")
elif media == 10:
    print("Aprovado com Distinção")
else:
    print("Reprovado")

print("Introduza o valor do saque:")
valor = int(input("Valor: "))

if valor >= 10 and valor <= 600:
    notas100 = valor // 100
    valor %= 100
    notas50 = valor // 50
    valor %= 50
    notas10 = valor // 10
    valor %= 10
    notas5 = valor // 5
    valor %= 5
    notas1 = valor

    print("Notas de 100:", notas100)
    print("Notas de 50:", notas50)
    print("Notas de 10:", notas10)
    print("Notas de 5:", notas5)
    print("Notas de 1:", notas1)
else:
    print("O valor não é válido")
    
print("Introduza um número inteiro:")
numero = int(input("Número: "))

if numero % 2 == 0:
    print("O número é par")
else:
    print("O número é impar")

print("Introduza um número:")
numero = float(input("Número: "))

if numero == int(numero):
    print("O número é inteiro")
else:
    print("O número é decimal")

print("Responda às seguintes perguntas:")
respostas = []

respostas.append(input("Telefonou para a vítima? (S/N): "))
respostas.append(input("Esteve no local do crime? (S/N): "))
respostas.append(input("Mora perto da vítima? (S/N): "))
respostas.append(input("Devia para a vítima? (S/N): "))
respostas.append(input("Já trabalhou com a vítima? (S/N): "))

contagem = 0
for resposta in respostas:
    if resposta.upper() == "S":
        contagem += 1

if contagem == 2:
    print("Você é suspeito")
elif contagem >= 3 and contagem <= 4:
    print("Você é cúmplice")
elif contagem == 5:
    print("Você é assassino")
else:
    print("Você é inocente")
    
print("Introduza o número de litros vendidos:")
litros = float(input("Litros: "))

print("Introduza o tipo de combustível (A-álcool, G-gasolina):")
tipo = input("Tipo: ")

if tipo.upper() == "A":
    if litros <= 20:
        preco = litros * 1.90 * 0.97
    else:
        preco = litros * 1.90 * 0.95
elif tipo.upper() == "G":
    if litros <= 20:
        preco = litros * 2.50 * 0.96
    else:
        preco = litros * 2.50 * 0.94
else:
    print("Tipo de combustível inválido")
    preco = None

if preco is not None:
    print("Preço a ser pago:", preco)
    

print("Introduza a quantidade de morangos adquiridos (em Kg):")
morangos = float(input("Morangos: "))

print("Introduza a quantidade de maças adquiridas (em Kg):")
macas = float(input("Maças: "))

preco_morangos = morangos * 2.50
preco_macas = macas * 1.80

if morangos > 5:
    preco_morangos *= 0.88
if macas > 5:
    preco_macas *= 0.83

preco_total = preco_morangos + preco_macas

if preco_total > 25 or morangos + macas > 8:
    preco_total *= 0.90

print("Preço a ser pago:", preco_total)


print("Introduza o tipo de carne comprada (F-File Duplo, A-Alcatra, P-Picanha):")
tipo = input("Tipo: ")

print("Introduza a quantidade de carne comprada (em Kg):")
quantidade = float(input("Quantidade: "))

if tipo.upper() == "F":
    preco = quantidade * 4.90
elif tipo.upper() == "A":
    preco = quantidade * 5.90
elif tipo.upper() == "P":
    preco = quantidade * 6.90
else:
    print("Tipo de carne inválido")
    preco = None

if preco is not None:
    if quantidade > 5:
        preco *= 1.18
    if input("Pagamento com cartão Tabajara? (S/N): ").upper() == "S":
        preco *= 0.95
    print("Preço a ser pago:", preco)
    
    








