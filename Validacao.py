# Biblioteca para ocultar a senha - é preciso instalar antes do primeiro uso
import maskpass

# Validar a senha de acordo com os requisitos
def validar_senha(senha: str) -> None:
    # Analisa os erros encontrados na senha
    erros = []

    # A senha precisa ter no mínimo 8 caracteres
    if len(senha) < 8:
        erros.append("A senha deve ter no mínimo 8 caracteres")

    # A senha precisa ter no mínimo uma letra maiúscula
    if not any(char.isupper() for char in senha):
        erros.append("A senha deve conter pelo menos uma letra maiúscula")

    # Pelo menos um número
    if not any(char.isdigit() for char in senha):
        erros.append("A senha deve conter pelo menos um número")

    # Símbolos permitidos
    simbolos_permitidos = {"_", "#", "@"}

    if not any(char in simbolos_permitidos for char in senha):
        erros.append(
            "A senha deve conter pelo menos um dos símbolos: _, # ou @"
        )

    # Se houver erros, exibe a mensagem de erro
    if erros:
        mensagem_erro = "\n".join(f" . {erro}" for erro in erros)

        raise ValueError(
            f"Sua senha não atende aos requisitos de segurança:\n{mensagem_erro}"
        )

# Função principal
def main():
    print("=" * 45)
    print("SISTEMA DE CRIAÇÃO DE SENHA SEGURA")
    print("=" * 45)

    print("Requisitos para a senha:")
    print("1. Mínimo de 8 caracteres")
    print("2. Pelo menos 1 letra maiúscula")
    print("3. Pelo menos 1 número")
    print("4. Pelo menos 1 dos símbolos: _, # ou @")

    senha_cadastrada = ""

    # Loop para solicitar a senha até que seja válida
    while True:
        try:
            senha_input = input("\nDigite a sua senha: ")

            validar_senha(senha_input)

            senha_cadastrada = senha_input

            print("\nSenha criada e validada com sucesso!")
            break

        except ValueError as erro:
            print(f"\nErro: {erro}\n")
            print("Por favor, tente novamente.")

    # Pergunta se o usuário deseja ver a senha criada ( biblioteca maskpass sendo ativada )
    print("-" * 45)

    opcao = input(
        "Deseja ver a senha criada? (Sim ou Não): "
    ).strip().upper()

    if opcao == "SIM":
        print(f"\nSua senha é: {senha_cadastrada}")
    else:
        print("\nSenha mantida oculta por segurança.")

    print("\nObrigado por utilizar o sistema.")

# Executa a função principal
if __name__ == "__main__":
    main()