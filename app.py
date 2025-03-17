# Introdução à plataforma

# Função para exibir a introdução
def introduction():
    print("Bem-vindo à União Digital!")
    print("Nossa plataforma oferece cursos gratuitos para promover a inclusão digital e o aprendizado de novas habilidades.")
    print("Aqui, você encontrará cursos sobre programação, segurança digital, cibersegurança e muito mais.")
    print("Estamos comprometidos em ajudar você a crescer e se desenvolver no mundo digital.")
    print("Vamos começar!\n")

# Função para registrar um novo usuário
def register():
    print("\n=== Registro de Usuário ===")
    username = input("Digite seu nome de usuário: ")
    password = input("Digite sua senha: ")
    print(f"Usuário '{username}' registrado com sucesso!")

# Função para realizar login
def login():
    print("\n=== Login ===")
    username = input("Digite seu nome de usuário: ")
    password = input("Digite sua senha: ")
    print(f"Bem-vindo de volta, {username}!")
    course = choose_course()  # Chama a função para escolher um curso
    access_course(course)  # Chama a função para acessar o conteúdo do curso escolhido

# Função para escolher um curso
def choose_course():
    print("\nEscolha o curso que você deseja fazer:")
    print("1. Pensamento Lógico Computacional")
    print("2. Segurança Digital e Cidadania Digital")
    print("3. Programação em Python")
    print("4. Fundamentos de Cibersegurança")
    choice = input("Digite o número do curso desejado: ")
    if choice == "1":
        return "Pensamento Lógico Computacional"
    elif choice == "2":
        return "Segurança Digital e Cidadania Digital"
    elif choice == "3":
        return "Programação em Python"
    elif choice == "4":
        return "Fundamentos de Cibersegurança"
    else:
        print("Opção inválida! Tente novamente.")
        return choose_course()  # Rechama a função em caso de entrada inválida

# Função para acessar o conteúdo do curso escolhido
def access_course(course):
    print(f"\n=== Acessando o conteúdo do curso: {course} ===")
    print(f"Bem-vindo ao curso de {course}!")
    print("Aqui você encontrará materiais, exercícios e muito mais para aprender e se desenvolver.")
    print("Aproveite o curso!\n")
    input("Pressione Enter para voltar ao menu principal...")  # Aguarda o usuário pressionar Enter para retornar ao menu

# Menu principal
def main():
    introduction()  # Chama a introdução antes de exibir o menu
    while True:
        print("\n1. Registrar")
        print("2. Login")
        print("3. Sair")
        choice = input("Escolha uma opção: ")
        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()  # Chama a função principal quando o script é executado