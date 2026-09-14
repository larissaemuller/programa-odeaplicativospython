
#1 estrutura condicionais

nota = 6

if nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")

            #2 condições com operadores lógicos
            # and -> todas condições devem ser verdadeiras
            # or -> pelo menos uma condição deve ser verdadeira
            # not -> inverte o resultado

idade = 20
ingresso = True

        if idade >= 18 and ingresso:
            print("Entrada permitida")

        else:
            print("Entrada não permitida")

            #3 estrutura de repetição

            contador = 1

            while contador <= 5:
                print(contador)
                contador += 1

                #4 estrutura de repetição for
             for numero in range(1,6):
            print (numero)

                #5 percorrendo uma lista
            nomes = ["ana", "carlos", "joao", "maria"]

            for nome in nomes:
            print(nome)

            #6 break
            #0 break interrompe completamente a repetição
            #0 pass nao executa nenhuma funcao
            #0 continue interrompe apenas a repeticao atual

            for numero in range(1,11):
                if numero == 7:
                    #break
                    #pass
                    continue

                 print(numero)

            #7 condicao dentro de repeticao
            for numero in range(1,11):

                if numero % 2 == 0:
                    print(f"{numero} é par")

                else:
                    print(f"{numero} é impar")
