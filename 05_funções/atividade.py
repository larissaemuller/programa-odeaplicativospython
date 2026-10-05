def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    return media


def verificar_situacao(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"


def exibir_resultado(nome, nota1, nota2, nota3, media, situacao):
    print("\n===== RESULTADO DO ESTUDANTE =====")
    print("Nome:", nome)
    print("Nota 1:", nota1)
    print("Nota 2:", nota2)
    print("Nota 3:", nota3)
    print("Média:", round(media, 2))
    print("Situação:", situacao)


# Programa principal
nome = input("Digite o nome do estudante: ")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = calcular_media(nota1, nota2, nota3)
situacao = verificar_situacao(media)

exibir_resultado(nome, nota1, nota2, nota3, media, situacao)