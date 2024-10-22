valor = []

for _ in range(10):
    entrada = input("Digite um val numérico inteiro: ")

    if entrada.isdigit():
        valor.append(int(entrada))

if valor:
    media = sum(valor) / len(valor)
    print(f"A média dos valores é: {media}")
else:
    print("Nenhum val numérico válido foi fornecido.")