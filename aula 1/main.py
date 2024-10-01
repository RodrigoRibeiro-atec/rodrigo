#cmt

"""
cmt
varias
linhas
"""

#prt
print("Ola mundo")


#var
nome = "Valor" # String (cadeia de caracteres)
idade = 10 # max int em c -> 2,147,482,647, max int em Py -> não existe
nota = 10.9 # int( 6 a 7 casas decimais ) e double (14)
aprovado = True # 


print(nome)
nome = 10 
print(nome)


soma = idade + 3
print(soma)


soma2 = nota + 2
print(soma2)


nome = "Valor"
soma3 = nome + "Foo"
print(soma3)


nome = "Valor"
# soma4 = nome + 2024
#print(soma4)


op5 = nome * 2
print(op5)

#print v2


nome = "rodrigo"
ano = 2024

# "Ola Mundo, rodrigo em 2024"


#str(ano) converte para string 

print("Ola mundo,",  nome  ,"em" , str(ano))

print("Ola mundo,"+  nome  + "em" + str(ano))

print("Ola mundo,",  nome  ,"em" ,ano)

print(f"Ola mundo, {nome.upper()} em {ano}")


# -> % <-

op2 = 10 % 3
print(op2)

op2 = 12 % 3
print(op2)


op2 = 10 / 3
print(op2)


op2 = 10 // 3
print(op2)


#ler dados do teclado

nome2 = input("Digite seu nome: ")
print(f"ola", nome2)

#ifs
idade = 10
if idade > 18:
    print("adulto")
else:
    print("não adulto")
    
    
#faça um programa quer peça dois numeros e imprima a soma

numero1 = int(input("Digite o primeiro número: "))

numero2 = int(input("Digite o segundo número: "))

soma = numero1 + numero2

print("A soma de", numero1, "e", numero2, "e:", soma)


#faça um programa que peça as 4 notas e mostre a media

nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
nota3 = int(input("Digite a terceira nota: "))
nota4 = int(input("Digite a quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

print("A média das notas e:", media)
