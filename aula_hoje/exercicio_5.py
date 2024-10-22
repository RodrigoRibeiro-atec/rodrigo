"""
exep:


input
x=3

output

1
1 2
1 2 3

input

x=5


output

1
1 2
1 2 3
1 2 3 4
1 2 3 4 5


"""

def imprimir_niveis(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

x = int(input("escreva o número de níveis: "))
imprimir_niveis(x)