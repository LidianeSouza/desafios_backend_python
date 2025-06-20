# Sistema de Descontos para Loja Online

# Entrada de dados
preco = float(input("Digite o preço do produto: "))
cupom = input("Digite o código do cupom: ")

# Verifica o cupom e aplica o desconto
if cupom == "DESCONTO10":
    preco_final = preco * 0.90
elif cupom == "DESCONTO20":
    preco_final = preco * 0.80
elif cupom == "SEM_DESCONTO":
    preco_final = preco
else:
    print("Cupom inválido. Nenhum desconto aplicado.")
    preco_final = preco

# Exibe o preço final com duas casas decimais
print(f"Preço final: {preco_final:.2f}")