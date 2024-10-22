"""
1 - Crie um dicionário com os seus dados: nome e turma
2 - Usando o dicionario criado anteriormente, imprima o seu nome 
3 - Adicione a sua localidade
4 - mostre a msg

"Ola, o meu nome e <Nome>, sou de <Localidade> e estou na turma <turma>

"""

dic = { "nome": "Diogo", "turma": "PIPL0923"}
print(f"Nome: {dic["nome"]}")

print(dic)

dic["Localidade"] = "Rua dos São joão"

print(dic)

print(f"Ola, o meu nome e {dic['nome']}, sou de {dic['Localidade']} e estou na turma {dic['turma']} ")