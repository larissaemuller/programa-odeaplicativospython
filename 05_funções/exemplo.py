#o que é uma função:
#uma funcao é um bloco de código criado para realizar uma determinada tarefa
#ela permite organizar e reutilizar código.

#1. Criando uma função
#utilizar a palavra def para uma função

def saudacao():
    print("Olá seja bem-vindo!")

saudacao()

#2. Criando uma funcao com parâmetro
#parâmetros permitem enviar informações para a função.

def saudacao2(nome):
    print(f"Olá {nome}")

saudacao2("Ana")
saudacao2("Maria")


#3. Mais de um parâmetro
def apresentar(nome , idade):
    print(f"nome: {nome}")
    print(f"idade: {idade}")

apresentar("Maria", 17)
apresentar("Ana", 20)

#4. funcao com calculo

def somar(numero1, numero2):
    resultado = numero1 + numero2
    print(f"resultado: {resultado}")

somar(10,20)
somar(10,90)

#5. retornando um valor
#return devolve um valor par ao local onde a funcao foi chamada

def somar(numero1, numero2):
    return numero1 + numero2

print(somar(10,5))

#6. Funcao com condicao

def verificarIdade(idade):
    if idade >= 18:
        return "maior de idade"
    else:
        return "menor de idade"
print(verificarIdade(18))

#7. Parâmetro com valor padrão

def saudacao3(nome = "aluno"):
    print(f"Olá {nome}")

saudacao3("Ana")
saudacao3()

#8. funcao utilizando lista

def calcularMedia(notas):
    soma = 0
    for nota in notas:
        soma += nota

    return soma/len(notas)

notas = [8 , 7 , 9 , 10]
media = calcularMedia(notas)
print(f"Média: {media}")


#9. funcoes para organizar um programa

def cadastrar_produto():

    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço:"))
    return nome, preco

def exibir_produto(nome , preco):

    print("\n====Produto====")
    print(f"Nome: {nome}")
    print(f"preço: {preco:.2f}")

nome, preco = cadastrar_produto()
exibir_produto(nome, preco)