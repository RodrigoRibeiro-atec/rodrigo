def ler_e_mostrar_inteiros():
    numeros = [int(input(f"Digite o {i+1}º número inteiro: ")) for i in range(5)]
    print("Números lidos:", numeros)

ler_e_mostrar_inteiros()


def ler_e_mostrar_reais_inverso():
    numeros = [float(input(f"Digite o {i+1}º número real: ")) for i in range(10)]
    print("Números na ordem inversa:", numeros[::-1])

ler_e_mostrar_reais_inverso()


def ler_notas_e_calcular_media():
    notas = [float(input(f"Digite a {i+1}ª nota: ")) for i in range(4)]
    media = sum(notas) / len(notas)
    print("Notas:", notas)
    print("Média:", media)

ler_notas_e_calcular_media()


def contar_consoantes():
    caracteres = [input(f"Digite o {i+1}º caractere: ") for i in range(10)]
    consoantes = [c for c in caracteres if c.isalpha() and c.lower() not in 'aeiou']
    print("Consoantes lidas:", consoantes)
    print("Quantidade de consoantes:", len(consoantes))

contar_consoantes()


def separar_pares_e_impares():
    numeros = [int(input(f"Digite o {i+1}º número inteiro: ")) for i in range(20)]
    pares = [num for num in numeros if num % 2 == 0]
    impares = [num for num in numeros if num % 2 != 0]
    print("Números lidos:", numeros)
    print("Números pares:", pares)
    print("Números ímpares:", impares)

separar_pares_e_impares()

def calcular_media_alunos():
    medias = []
    for i in range(10):
        notas = [float(input(f"Digite a {j+1}ª nota do aluno {i+1}: ")) for j in range(4)]
        media = sum(notas) / len(notas)
        medias.append(media)
    
    alunos_acima_media = sum(1 for media in medias if media >= 7.0)
    print("Número de alunos com média maior ou igual a 7.0:", alunos_acima_media)

calcular_media_alunos()


def somar_multiplicar_numeros():
    numeros = [int(input(f"Digite o {i+1}º número inteiro: ")) for i in range(5)]
    soma = sum(numeros)
    multiplicacao = 1
    for num in numeros:
        multiplicacao *= num
    print("Números lidos:", numeros)
    print("Soma:", soma)
    print("Multiplicação:", multiplicacao)

somar_multiplicar_numeros()


def ler_idade_altura_inversa():
    idades = []
    alturas = []
    for i in range(5):
        idade = int(input(f"Digite a idade da {i+1}ª pessoa: "))
        altura = float(input(f"Digite a altura da {i+1}ª pessoa: "))
        idades.append(idade)
        alturas.append(altura)
    
    print("Idades e alturas na ordem inversa:")
    for idade, altura in zip(reversed(idades), reversed(alturas)):
        print(f"Idade: {idade}, Altura: {altura}")

ler_idade_altura_inversa()


def soma_dos_quadrados():
    A = [int(input(f"Digite o {i+1}º número inteiro: ")) for i in range(10)]
    soma_quadrados = sum(num ** 2 for num in A)
    print("Soma dos quadrados:", soma_quadrados)

soma_dos_quadrados()


def intercalar_dois_vetores():
    A = [input(f"Digite o {i+1}º elemento do vetor A: ") for i in range(10)]
    B = [input(f"Digite o {i+1}º elemento do vetor B: ") for i in range(10)]
    C = [None] * 20
    C[::2] = A
    C[1::2] = B
    print("Vetor intercalado:", C)

intercalar_dois_vetores()


def intercalar_tres_vetores():
    A = [input(f"Digite o {i+1}º elemento do vetor A: ") for i in range(10)]
    B = [input(f"Digite o {i+1}º elemento do vetor B: ") for i in range(10)]
    C = [input(f"Digite o {i+1}º elemento do vetor C: ") for i in range(10)]
    D = [None] * 30
    D[::3] = A
    D[1::3] = B
    D[2::3] = C
    print("Vetor intercalado:", D)

intercalar_tres_vetores()


def alunos_acima_da_media():
    idades = [int(input(f"Digite a idade do aluno {i+1}: ")) for i in range(30)]
    alturas = [float(input(f"Digite a altura do aluno {i+1}: ")) for i in range(30)]
    media_altura = sum(alturas) / len(alturas)
    alunos_count = sum(1 for i in range(30) if idades[i] > 13 and alturas[i] < media_altura)
    print("Alunos com mais de 13 anos e altura inferior à média:", alunos_count)

alunos_acima_da_media()


def temperaturas_acima_da_media():
    temperaturas = [float(input(f"Digite a temperatura média do mês {i+1}: ")) for i in range(12)]
    media_anual = sum(temperaturas) / len(temperaturas)
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
             "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    
    print("Temperaturas acima da média anual:")
    for i, temp in enumerate(temperaturas):
        if temp > media_anual:
            print(f"{meses[i]}: {temp}")

temperaturas_acima_da_media()


def classificar_participacao():
    perguntas = [
        "Telefonou para a vítima? (s/n)",
        "Esteve no local do crime? (s/n)",
        "Mora perto da vítima? (s/n)",
        "Devia para a vítima? (s/n)",
        "Já trabalhou com a vítima? (s/n)"
    ]
    
    respostas = [input(pergunta).strip().lower() == 's' for pergunta in perguntas]
    count = sum(respostas)
    
    if count == 2:
        classificacao = "Suspeita"
    elif 3 <= count <= 4:
        classificacao = "Cúmplice"
    elif count == 5:
        classificacao = "Assassino"
    else:
        classificacao = "Inocente"
    
    print("Classificação:", classificacao)

classificar_participacao()


def notas_estatisticas():
    notas = []
    while True:
        nota = float(input("Digite a nota (-1 para sair): "))
        if nota == -1:
            break
        notas.append(nota)
    
    total = len(notas)
    soma = sum(notas)
    media = soma / total if total > 0 else 0
    acima_media = sum(1 for nota in notas if nota > media)
    abaixo_sete = sum(1 for nota in notas if nota < 7)
    
    print("Quantidade de valores lidos:", total)
    print("Notas na ordem em que foram informadas:", notas)
    print("Notas na ordem inversa:")
    for nota in reversed(notas):
        print(nota)
    print("Soma dos valores:", soma)
    print("Média dos valores:", media)
    print("Quantidade de valores acima da média:", acima_media)
    print("Quantidade de valores abaixo de sete:", abaixo_sete)
    print("Programa encerrado.")

notas_estatisticas()


def salarios_vendedores():
    num_vendedores = int(input("Digite o número de vendedores: "))
    salarios = []

    for i in range(num_vendedores):
        vendas = float(input(f"Digite o total de vendas do vendedor {i+1}: "))
        salario = 200 + (vendas * 0.09)
        salarios.append(salario)

    intervalos = [0] * 10  # 10 intervalos

    for salario in salarios:
        if salario < 200:
            intervalos[0] += 1
        elif salario < 300:
            intervalos[1] += 1
        elif salario < 400:
            intervalos[2] += 1
        elif salario < 500:
            intervalos[3] += 1
        elif salario < 600:
            intervalos[4] += 1
        elif salario < 700:
            intervalos[5] += 1
        elif salario < 800:
            intervalos[6] += 1
        elif salario < 900:
            intervalos[7] += 1
        elif salario < 1000:
            intervalos[8] += 1
        else:
            intervalos[9] += 1

    print("Quantidade de vendedores em cada intervalo:")
    intervalos_nomes = ["<200", "200-299", "300-399", "400-499", "500-599", 
                        "600-699", "700-799", "800-899", "900-999", "1000+"]
    
    for i, quantidade in enumerate(intervalos):
        print(f"Intervalo {intervalos_nomes[i]}: {quantidade}")

salarios_vendedores()



