# Sistema de Reservas de Pousada

# Entrada dos quartos disponíveis
disponiveis = input("Digite os quartos disponíveis (separados por espaço): ").split()

# Entrada dos quartos solicitados
solicitados = input("Digite os quartos solicitados (separados por espaço): ").split()

# Listas para armazenar os resultados
confirmadas = []
recusadas = []

# Verifica cada solicitação
for quarto in solicitados:
    if quarto in disponiveis:
        confirmadas.append(quarto)
        disponiveis.remove(quarto)  # remove para não reservar duas vezes
    else:
        recusadas.append(quarto)

# Exibe os resultados
print("Reservas confirmadas:", " ".join(confirmadas))
print("Reservas recusadas:", " ".join(recusadas))
