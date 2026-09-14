#1. operadores logicos
from operator import truediv

#and
#todas as condicoes precisam ser verdadeiras

idade = 20
possui_carteira = true

resultado = idade >=18 and possui_carteira
print(resultado)

#or
#pelo menos uma condicao precisa ser verdadeira

idade = 16
acompanhado = true

resultado = idade >=18 or acompanhado
print(resultado)

#not
#inverte o resultado de uma condicao

aluno_matriculado = true
print(not aluno_matriculado)

#2. operadores de comparacao

idade = 18

print(idade == 18)
print(idade != 18)
print(idade > 18)
print(idade < 18)
print(idade >= 18)
print(idade <= 18)

#3. estrutura if

idade = 18

if idade >= 18:
    print("maior de idade")

#4. estrutura if/else

idade = 16

if idade >= 18:
    print("maior de idade")

else :
    print("menor de idade")
