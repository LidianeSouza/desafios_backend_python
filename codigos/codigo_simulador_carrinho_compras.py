# Sistema de Carrinho de Compras

# Lista para guardar os produtos
carrinho = []

# Recebe o número de produtos
quantidade = int(input("Quantos produtos você quer adicionar? "))

# Loop para adicionar cada produto
for i in range(quantidade):
    entrada = input(f"Digite o nome e o preço do produto {i+1} (ex: Pão 3.50): ")
    nome, preco = entrada.split()
    preco = float(preco)
    carrinho.append((nome, preco))

# Exibe os produtos e calcula o total
total = 0
print("\nProdutos no carrinho:")
for nome, preco in carrinho:
    print(f"{nome}: R${preco:.2f}")
    total += preco

print(f"Total: R${total:.2f}")