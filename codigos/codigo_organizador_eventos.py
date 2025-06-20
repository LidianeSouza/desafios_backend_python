# Organizador de Eventos

# Cria o dicionário vazio para os temas
temas = {}

# Recebe o número de participantes
quantidade = int(input("Quantos participantes? "))

# Loop para registrar cada participante e seu tema
for i in range(quantidade):
    entrada = input(f"Digite o nome e o tema do participante {i+1} (ex: Ana, Música): ")
    nome, tema = entrada.split(", ")
    
    # Adiciona o nome na lista do tema correspondente
    if tema in temas:
        temas[tema].append(nome)
    else:
        temas[tema] = [nome]

# Mostra os participantes organizados por tema
print("\nParticipantes por tema:")
for tema, nomes in temas.items():
    print(f"{tema}: {', '.join(nomes)}")