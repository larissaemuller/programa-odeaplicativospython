# A CLASSE: o modelo(a planta)
class Celular:
    def __init__(self, marca, modelo, cor, bateria=100):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.bateria = bateria
        self.ligado = False


False


def ligar(self):
    if self.bateria == 0:
        print("Sem bateria! Coloque para carregar")
    else:
         self.ligado = True


True
print(f" {self.modelo} Ligado!")

# OS Objetos: Criados a partir da classe (as "casas")
celular1 = Celular("Sansung", "Galaxy s23", "Preto")
celular2 = Celular("Motorola", "Moto6", "Azul", "Bateria")

# Acessando e alterando atributos
print(celular2.marca)

# Tambem podemos alterar diretamente
celular1.cor = "branco"
print(celular1.cor)

# chamando metodos
celular2.ligar()