# Validador de E-mail

def validar_email(email):
    # Verifica se contém "@" e não está no início ou fim, e se não há espaços
    if "@" in email and not email.startswith("@") and not email.endswith("@") and " " not in email:
        return "E-mail válido"
    else:
        return "E-mail inválido"

# Entrada do usuário
email_digitado = input("Digite um e-mail para validar: ")

# Validação e saída
resultado = validar_email(email_digitado)
print(resultado)