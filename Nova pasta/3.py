av = {}

valores = int(input("Quantos valores você quer adicionar ao dicionário? "))

for _ in range(valores):
    key = input("Digite a key: ")
    valor = input("Digite o val: ")
    av[key] = valor

print(av)