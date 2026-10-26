#1. Encapsulamento
#Proteger o sálario para que só mude seguindo regras

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.__salario = salario #privado: dois sublinhado

    def apresentar(self):
        print(f"sou {self.nome} e ganho R${self.salario}")

    #@property deixa ler o salario com se fosse um atributo
    @property
    def salario(self):
        return self.__salario

    def dar_aumento(self , porcentagem):
        if porcentagem <= 0:
            print(f"aumento invalido para {self.nome}")
            return
        self.__salario = self.__salario * (1 + porcentagem / 100)
        print(f"{self.nome} recebeu {porcentagem}% de aumento")


##########################################
ana = Funcionario("ana", 3000)
ana.dar_aumento(100)
#ana.salario = 4000
print(ana.salario)
ana.apresentar()
ana.dar_aumento(-20)
ana.apresentar()

#o try/except é um bloco usado em programacao para tratar um erro
try:
    ana.salario = 10000
except AttributeError:
    print("não é permitido alterar o salario diretamente.")

try:
    print(ana.__salario)
except AttributeError:
    print("o atributo __salario nao pode ser acessado de fora.")

