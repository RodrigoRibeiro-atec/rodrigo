"""
 1

    2   2

    3   3   3

    .....

    n   n   n   n   n   n  ... n

    

    

    Exep: 

     

     input 

     x = 3

     

     output 

    

    1

    2   2

    3   3   3

     

     

     input 

     x = 5

     

     output 

    

    1

    2   2

    3   3   3

    4   4   4   4

    5   5   5   5   5

     





def imprimir(x:int):

    pass
"""

def niveis(numero):
    for i in range(1, numero + 1):
       print(f" {i} " * i) 

num_niveis = int(input("escreva o número de níveis: "))
niveis(num_niveis)