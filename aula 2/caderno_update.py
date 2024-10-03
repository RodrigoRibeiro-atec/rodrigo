#cmt

"""
cmt
varias
linhas
"""

#prt
#print("Ola mundo")


#var
#nome = "Valor" # String (cadeia de caracteres)
#idade = 10 # max int em c -> 2,147,482,647, max int em Py -> não existe
#nota = 10.9 # int( 6 a 7 casas decimais ) e double (14)
#aprovado = True # 


#print(nome)
#nome = 10 
#print(nome)


#soma = idade + 3
#print(soma)


#soma2 = nota + 2
#print(soma2)


#nome = "Valor"
#soma3 = nome + "Foo"
#print(soma3)


#nome = "Valor"
# soma4 = nome + 2024
#print(soma4)


#op5 = nome * 2
#print(op5)

#print v2


#nome = "rodrigo"
#ano = 2024

# "Ola Mundo, rodrigo em 2024"


#str(ano) converte para string 

#print("Ola mundo,",  nome  ,"em" , str(ano))

#print("Ola mundo,"+  nome  + "em" + str(ano))

#print("Ola mundo,",  nome  ,"em" ,ano)

#print(f"Ola mundo, {nome.upper()} em {ano}")


# -> % <-

#op2 = 10 % 3
#print(op2)

#op2 = 12 % 3
#print(op2)


#op2 = 10 / 3
#print(op2)


#op2 = 10 // 3
#print(op2)


#ler dados do teclado

#nome2 = input("Digite seu nome: ")
#print(f"ola", nome2)

#ifs
#idade = 10
#if idade > 18:
    #print("adulto")
#else:
    #print("não adulto")
    
    
#faça um programa quer peça dois numeros e imprima a soma

#numero1 = int(input("Digite o primeiro número: "))

#numero2 = int(input("Digite o segundo número: "))

#soma = numero1 + numero2

#print("A soma de", numero1, "e", numero2, "e:", soma)


#faça um programa que peça as 4 notas e mostre a media

#nota1 = int(input("Digite a primeira nota: "))
#nota2 = int(input("Digite a segunda nota: "))
#nota3 = int(input("Digite a terceira nota: "))
#nota4 = int(input("Digite a quarta nota: "))

#media = (nota1 + nota2 + nota3 + nota4) / 4

#print("A média das notas e:", media)




#Condições / Controlo de fluxo

#boolean

'''

T e T -> T
T e F -> F
F e T -> T
F e F -> F




T ou T -> T
T ou F -> T
F ou T -> T
F ou F -> F


T xou T -> F
T xou F -> T
F xou T -> T
F xou F -> F



'''

ano = 2024


# if (se)

if ano == 2024:
    print("ano = 2024")
else:
    print("Outro ano")
    
print("fora do if")

#Faça um programa que peça dois númros e imprima o maior deles
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 > num2:
    print(f"O maior número é: {num1}")
elif num2 > num1:
    print(f"O maior número é: {num2}")
else:
    print("Numero maior e:",num2)

print("--" * 10)

num = 5

# F e T -> F

# num = 5
#       F       and     T

if num % 2 == 0 and num % 5 == 0:
    print("par e div por 5")
    
else:
    print("impar ou não divisivel por 5")
    
 #FAÇA um programa que verifique se uma letra digitada é "F" ou "M"
#conforme a letra escrever:
#F-Femenino
#M-Masculino
#Genoro invalido   
letra = input("Digite uma letra (F, f, M, m): ")

if letra == 'F' or letra == 'f':
    print("F-Feminino")
elif letra == 'M' or letra == 'm':
    print("M-Masculino")
else:
    print("Gênero inválido")


    
    
'''
== <- comparações 


= <- atribuição


'''


# else if ( se não se )

# else ( se não)





# switch ( escolha )
num =5

match num:
    case 0:
        print("o num e 0")
    
    case 1:
        print("o num e 1")
    
    case 5:
        print("o num e 5")
        
    case _:
        print("outro valor")


menu = """
############Menu############
# OP1 ............ 1 #
# OP2 ............ 2 #
# OP3 ............ 3 #

 ########################"""
print(menu)

op = input("Selecione a op:")

match op:
    case "1":
        print("o num e 1")
    
    case "2":
        print("o num e 2")
    
    case "3":
        print("o num e 3")
        
    case _:
        print("outro valor")

#loops

#for (par)


#while ( enquanto - faça)

count = 0
while op != "q":
    print(f"\tloop: {count}")
    
    op = input("\tInsira o valor 'q': ")
    
    count += 1

num = 0

while num < 10:
    print(num)
    num += 1
    
#range
range(0,10,2)
"""

a- LB

b- UB

c- step,se oculto c = 1

range(1,5)
1,2,3,4


range(5)
0,1,2,3,4


range(0,10,2)
0,2,4,6,8
"""
print("---"* 10)
for elm in range (0,11,2):
    print(elm)
    
    
    
print("---"* 10)
for elm in range (0,100):
    print(elm)
    if elm == 50:
        break
    
  
nomes = [    "Ana", "Bruno", "Carlos", "Daniela", 
         "Eduardo", "Fernanda", "Gabriel", "Helena", "Igor",
         "Julia",    "Karla", "Lucas", "Mariana", "Nicolas", 
         "Olivia", "Pedro", "Quintino", "Rafael", "Sara",
         "Tatiana",    "Ursula", "Vinicius", "Wagner", 
         "Xavier", "Yasmin"]  

for nome in nomes:
    print(nome)
    
print(nome.count("Daniela"))


print(nome.__len__())
print(len(nomes))


print(nomes.__contains__("Sara"))
print(nomes.__contains__("Ana"))
print("Pedro"  in nomes)

#nomes.sort 

print("----------------"* 5)
nomes.sort()
print(nomes)

"""
var
tuplos
op com var
if
elif
else
and/or
match
while
for 
list
tipos de dados
type cast- int("..."), srt(.....)
"""


"""
Faça um programa que peça uma nota, entre zero e dez.
Mostre uma mensagem caso o valor seja inválido e 
continue pedindo até que o usuário informe um valor válido.

"""
while True:
    nota = input("Informe uma nota entre 0 e 10: ")
    if nota.isdigit() and 0 <= int(nota) <= 10:
        print("Nota válida!")
        break
    else:
        print("Valor inválido. Por favor, informe uma nota entre 0 e 10.")