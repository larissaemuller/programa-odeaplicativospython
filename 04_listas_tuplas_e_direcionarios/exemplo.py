#Listas, tuplas e dicionários


#1. listas
#listas são utilizadas para armazenar varios valores dentro
#de uma unica variavel.
nomes = ["ana", "carlos", "joão", "maria"]
print(nomes)


#2. acessando elementos da lista
print(nomes[0])




#podemos acessar o ultimo elemento usando 0 -1
print(nomes[-1])


#3. alterando elementos


nomes[0] = "pedro"
print(nomes)


#4. adicionar elementos
#append() adiciona um elemento no final da lista
nomes.append("lucas")
print(nomes)


#insert() adiciona um elemento em uma posição especifica.
nomes.insert(1, "mariana")
print(nomes)


#5. removendo elementos
#remove um elemnto pelo valor


nomes.remove("lucas")
print(nomes)


#pop() remove um elemento pelo indice
nomes.pop(0)
print(nomes)


#6. tamanho da lista
#len() informa a quantidade de elementos
print(len(nomes))


#7. percorrendo uma lista
for nome in nomes:
   print(nome)


#8. verificando se um elemento existe


if "joão" in nomes:
   print("joão esta na lista")


else:
   print("joão nao esta na lista")


#9. lista com diferentes tipos de dados
dados = ["joao", 18 , 1.75 , True]
print(dados)


#10. lista de numeros
notas = [7.5 , 8.0 , 6.5 , 9.0]


soma = 0


for nota in notas:
   soma = soma + nota


media = soma / len(notas)
print(f"media: {media}")


#11. tuplas
#tuplas são semelhantes as listas. As tuplas não podem ser alteraradas.


coordenadas = (10, 20)
print(coordenadas)


print(coordenadas[0])


#12. dicionários
#dicionarios armazenam informações no formato: chave: valor
aluno = {
   "nome": "carlos",
   "idade": 17,
   "nota": 8.5
}
print(aluno)
