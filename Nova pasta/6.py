#Crie uma função que conte quantas vezes as letras aparecem numa string
#exemplo 
#aabbbcccccc
#
#output
# a - 2
# b - 3
# c - 5
def quantas_letras(string) -> str:
    quant = {}
    for elm in string:
        if elm.isalpha():  
            if elm in quant:
                quant[elm] += 1
            else:
                quant[elm] = 1
    return quant

result = quantas_letras(" aaaannnneiofhaeoifapja")
print(result)