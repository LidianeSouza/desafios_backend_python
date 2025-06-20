# Sistema de Atendimento Médico 

pacientes = []

n = int(input("Quantos pacientes serão cadastrados? "))

for i in range(n):
    entrada = input(f"Digite os dados do paciente {i+1} (nome, idade, status): ")
    nome, idade, status = entrada.split(", ")
    idade = int(idade)
    pacientes.append((nome, idade, status, i))  # o "i" representa a ordem de chegada

# Função de prioridade: menor valor = mais prioridade
def prioridade(paciente):
    nome, idade, status, ordem = paciente
    if status == "urgente":
        return (0, -idade)  # prioridade máxima, depois idade decrescente
    elif idade >= 60:
        return (1, -idade)  # prioridade intermediária
    else:
        return (2, ordem)   # por ordem de chegada

# Ordenar pacientes pela prioridade
ordenados = sorted(pacientes, key=prioridade)

# Exibir resultado
nomes_em_ordem = [p[0] for p in ordenados]
print("Ordem de Atendimento:", ", ".join(nomes_em_ordem))