#1. Cadastro de filmes

# 1. Criar uma lista com 5 filmes
filmes = [
    "Interestelar",
    "O Senhor dos Anéis",
    "Matrix",
    "Vingadores: Ultimato",
    "Jurassic Park"
]

# 2. Exibir todos os filmes
print("Filmes cadastrados:")
for filme in filmes:
    print(filme)

# 3. Exibir o primeiro filme
print("\nPrimeiro filme:", filmes[0])

# 4. Exibir o último filme
print("Último filme:", filmes[-1])

# 5. Adicionar um novo filme ao final
filmes.append("Titanic")
print("\nApós adicionar um filme:", filmes)

# 6. Inserir um novo filme em uma posição específica
filmes.insert(2, "Avatar")
print("Após inserir um filme na posição 2:", filmes)

# 7. Remover um filme
filmes.remove("Matrix")
print("Após remover Matrix:", filmes)

# 8. Alterar o nome de um filme
filmes[0] = "Interestelar 2"
print("Após alterar o primeiro filme:", filmes)

# 9. Exibir a quantidade de filmes
print("Quantidade de filmes:", len(filmes))

# 10. Verificar se um filme está presente
filme_procurado = "Titanic"

if filme_procurado in filmes:
    print(f"{filme_procurado} está cadastrado.")
else:
    print(f"{filme_procurado} não está cadastrado.")


#2. Controle de notas

# 1. Criar uma lista com 5 notas
notas = [8.5, 7.0, 9.0, 6.5, 10.0]

# 2. Exibir todas as notas
print("Notas do estudante:")
for nota in notas:
    print(nota)

# 3. Calcular a soma
soma = sum(notas)
print("\nSoma das notas:", soma)

# 4. Calcular a média
media = soma / len(notas)
print("Média:", media)

# 5. Identificar a maior nota
print("Maior nota:", max(notas))

# 6. Identificar a menor nota
print("Menor nota:", min(notas))

# 7. Verificar se existe uma nota igual a 10
if 10 in notas:
    print("Existe uma nota igual a 10.")
else:
    print("Não existe uma nota igual a 10.")

# 8 e 9. Verificar aprovação
if media >= 7:
    print("Estudante aprovado!")
else:
    print("Estudante reprovado!")


#3. Informações de um produto usando tupla

# Criar uma tupla com as informações do produto
produto = ("Notebook", "Informática", 3500.00, 12345)

# 1. Exibir cada informação individualmente
print("Nome:", produto[0])
print("Categoria:", produto[1])
print("Preço:", produto[2])
print("Código:", produto[3])

# 2. Exibir todas as informações usando repetição
print("\nInformações do produto:")

for informacao in produto:
    print(informacao)

# 3. Informar a quantidade de informações
print("\nQuantidade de informações:", len(produto))

# 4. Tentar alterar uma informação
try:
    produto[2] = 3000.00
except TypeError:
    print("\nNão é possível alterar a informação.")

# 5. Explicação
print(
    "Isso acontece porque as tuplas são imutáveis. "
    "Depois de criadas, seus elementos não podem ser modificados."
)


#4. Cadastro de funcionário

# Criar o dicionário do funcionário
funcionario = {
    "nome": "Carlos",
    "idade": 30,
    "cargo": "Analista de Sistemas",
    "salario": 4500.00,
    "setor": "Tecnologia"
}

# 1. Exibir cada informação
print("Nome:", funcionario["nome"])
print("Idade:", funcionario["idade"])
print("Cargo:", funcionario["cargo"])
print("Salário:", funcionario["salario"])
print("Setor:", funcionario["setor"])

# 2. Alterar o salário
funcionario["salario"] = 5000.00

# 3. Adicionar uma nova informação
funcionario["cidade"] = "Joinville"

# 4. Remover uma informação
del funcionario["cidade"]

# 5. Verificar se uma chave existe
if "cargo" in funcionario:
    print("\nA chave 'cargo' existe no cadastro.")
else:
    print("\nA chave 'cargo' não existe no cadastro.")

# 6. Percorrer o dicionário exibindo chaves e valores
print("\nCadastro completo:")

for chave, valor in funcionario.items():
    print(f"{chave}: {valor}")


#5. Sistema de estoque

# Lista de dicionários contendo os produtos
estoque = [
    {
        "nome": "Notebook",
        "categoria": "Informática",
        "preco": 3500.00,
        "quantidade": 8
    },
    {
        "nome": "Mouse",
        "categoria": "Periféricos",
        "preco": 80.00,
        "quantidade": 25
    },
    {
        "nome": "Teclado",
        "categoria": "Periféricos",
        "preco": 150.00,
        "quantidade": 7
    },
    {
        "nome": "Monitor",
        "categoria": "Informática",
        "preco": 1200.00,
        "quantidade": 12
    },
    {
        "nome": "Headset",
        "categoria": "Periféricos",
        "preco": 250.00,
        "quantidade": 5
    }
]

# 1 e 2. Exibir todos os produtos
print("=== PRODUTOS DO ESTOQUE ===")

for produto in estoque:
    print(
        f"Nome: {produto['nome']} | "
        f"Preço: R$ {produto['preco']:.2f} | "
        f"Quantidade: {produto['quantidade']}"
    )

# 3. Calcular a quantidade total de itens
quantidade_total = 0

for produto in estoque:
    quantidade_total += produto["quantidade"]

print("\nQuantidade total de itens:", quantidade_total)

# 4. Calcular o valor total do estoque
valor_total = 0

for produto in estoque:
    valor_total += produto["preco"] * produto["quantidade"]

print(f"Valor total do estoque: R$ {valor_total:.2f}")

# 5. Identificar produtos com menos de 10 unidades
print("\nProdutos com menos de 10 unidades:")

for produto in estoque:
    if produto["quantidade"] < 10:
        print(
            f"{produto['nome']} - "
            f"{produto['quantidade']} unidades"
        )

# 6. Verificar se determinado produto está cadastrado
produto_procurado = "Mouse"
encontrado = False

for produto in estoque:
    if produto["nome"].lower() == produto_procurado.lower():
        encontrado = True
        break

if encontrado:
    print(f"\nO produto '{produto_procurado}' está cadastrado.")
else:
    print(f"\nO produto '{produto_procurado}' não está cadastrado.")

# 7. Alterar a quantidade de um produto
for produto in estoque:
    if produto["nome"] == "Mouse":
        produto["quantidade"] = 30

print("\nQuantidade do Mouse alterada.")

# 8. Adicionar um novo produto
novo_produto = {
    "nome": "Webcam",
    "categoria": "Periféricos",
    "preco": 300.00,
    "quantidade": 10
}

estoque.append(novo_produto)

print("Novo produto adicionado.")

# 9. Relatório final
print("\n=== RELATÓRIO FINAL DO ESTOQUE ===")

for produto in estoque:
    print(f"Nome: {produto['nome']}")
    print(f"Categoria: {produto['categoria']}")
    print(f"Preço: R$ {produto['preco']:.2f}")
    print(f"Quantidade: {produto['quantidade']}")
    print("-" * 30)












