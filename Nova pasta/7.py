def quant_palavras(string:str):
    pala = string.split(" ")
    dic = {}
    for pala in pala:
        if dic.get(pala) != None:
            dic[pala] = dic[pala]+1
        else:
            dic[pala] = 1
    return dic
res = quant_palavras("Isto é Isto que serve para Isto aquilo assim")
print(res)