from datetime import datetime
import json

# Função para carregar os usuários registrados de um arquivo JSON
def load_users():
    try:
        with open("users.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Função para salvar os usuários registrados em um arquivo JSON
def save_users(users):
    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)

# Função para salvar estatísticas do usuário
def save_statistics(username, course, score):
    stats = load_statistics()
    if username not in stats:
        stats[username] = {}
    stats[username][course] = score
    with open("statistics.json", "w") as file:
        json.dump(stats, file, indent=4)

# Função para carregar estatísticas do usuário
def load_statistics():
    try:
        with open("statistics.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Introdução à plataforma
def introduction():
    print("Bem-vindo à União Digital!")
    print("Nossa plataforma oferece cursos gratuitos para promover a inclusão digital e o aprendizado de novas habilidades.")
    print("Aqui, você encontrará cursos sobre programação, segurança digital, cibersegurança e muito mais.")
    print("Estamos comprometidos em ajudar você a crescer e se desenvolver no mundo digital.")
    print("Vamos começar!\n")

# Função para calcular a idade com base na data de nascimento
def calculate_age(birth_date):
    today = datetime.today()
    birth_date = datetime.strptime(birth_date, "%d/%m/%Y")
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

# Função para registrar um novo usuário
def register():
    print("\n=== Registro de Usuário ===")
    full_name = input("Digite seu nome completo: ")
    birth_date = input("Digite sua data de nascimento (DD/MM/AAAA): ")
    try:
        age = calculate_age(birth_date)
    except ValueError:
        print("Data de nascimento inválida! Use o formato DD/MM/AAAA.")
        return register()
    print("Escolha seu gênero:")
    print("1. Masculino")
    print("2. Feminino")
    print("3. Prefiro não informar")
    gender_choice = input("Digite o número correspondente ao seu gênero: ")
    gender = {
        "1": "Masculino",
        "2": "Feminino",
        "3": "Prefiro não informar"
    }.get(gender_choice, "Prefiro não informar")
    location = input("Digite sua localização (cidade, estado ou país): ")
    username = input("Digite seu nome de usuário: ")

    # Verificar se o nome de usuário já existe
    users = load_users()
    if username in users:
        print("Nome de usuário já existe! Tente novamente.")
        return

    # Solicitar senha
    password = input("Digite sua senha: ")

    # Salvar o usuário no arquivo JSON
    users[username] = {
        "full_name": full_name,
        "age": age,
        "birth_date": birth_date,
        "gender": gender,
        "location": location,
        "password": password
    }
    save_users(users)

    print("\n=== Informações Registradas ===")
    print(f"Nome completo: {full_name}")
    print(f"Idade: {age} anos")
    print(f"Data de nascimento: {birth_date}")
    print(f"Gênero: {gender}")
    print(f"Localização: {location}")
    print(f"Usuário '{username}' registrado com sucesso!")

# Função para realizar login
def login():
    print("\n=== Login ===")
    username = input("Digite seu nome de usuário: ")
    password = input("Digite sua senha: ")

    # Carregar os usuários registrados
    users = load_users()
    if username in users and users[username]["password"] == password:
        print(f"Bem-vindo de volta, {username}!")
        user_dashboard(username)
    else:
        print("Nome de usuário ou senha incorretos! Tente novamente.")

# Função para exibir o painel do usuário
def user_dashboard(username):
    print("\n=== Painel do Usuário ===")
    print(f"Bem-vindo ao seu painel, {username}!")
    stats = load_statistics().get(username, {})
    if stats:
        print("\nEstatísticas dos cursos concluídos:")
        for course, score in stats.items():
            print(f"- {course}: {score:.2f}% de acertos")
    else:
        print("Você ainda não concluiu nenhum curso.")

    print("\nO que você gostaria de fazer agora?")
    print("1. Fazer um quiz")
    print("2. Sair")
    choice = input("Escolha uma opção: ")
    if choice == "1":
        course = choose_course()
        access_course(course, username)
    elif choice == "2":
        print("Saindo do painel. Até logo!")
    else:
        print("Opção inválida! Retornando ao painel.")
        user_dashboard(username)

# Função para escolher um curso
def choose_course():
    print("\nEscolha o curso que você deseja fazer:")
    print("1. Pensamento Lógico Computacional")
    print("2. Segurança Digital e Cidadania Digital")
    print("3. Programação em Python")
    print("4. Fundamentos de Cibersegurança")
    
    choice = input("Digite o número do curso desejado: ")
    courses = {
        "1": "Pensamento Lógico Computacional",
        "2": "Segurança Digital e Cidadania Digital",
        "3": "Programação em Python",
        "4": "Fundamentos de Cibersegurança"
    }
    
    return courses.get(choice, None)

# Função para acessar o conteúdo do curso escolhido
def access_course(course, username):
    if not course:
        print("Curso inválido! Tente novamente.")
        return

    print(f"\n=== Acessando o conteúdo do curso: {course} ===")
    
    if course == "Fundamentos de Cibersegurança":
        print("A cibersegurança protege sistemas, dados e pessoas contra ameaças cibernéticas.")
        score = cyber_quiz()
    elif course == "Pensamento Lógico Computacional":
        print("O pensamento computacional ajuda a resolver problemas de forma eficiente.")
        score = logic_quiz()
    else:
        print(f"Bem-vindo ao curso de {course}!")
        print("Aqui você encontrará materiais, exercícios e muito mais para aprender e se desenvolver.")
        score = 0

    # Salvar estatísticas do curso
    save_statistics(username, course, score)

    # Oferecer opções após finalizar o curso
    while True:
        print("\nO que você gostaria de fazer agora?")
        print("1. Voltar ao menu principal")
        print("2. Acessar outro curso")
        choice = input("Escolha uma opção: ")
        if choice == "1":
            user_dashboard(username)  # Volta ao menu principal
            break
        elif choice == "2":
            course = choose_course()  # Permite escolher outro curso
            access_course(course, username)
            break
        else:
            print("Opção inválida! Tente novamente.")

# Função genérica para rodar quizzes
def run_quiz(questions):
    correct_answers = 0
    for q in questions:
        print(q["question"])
        for option in q["options"]:
            print(option)
        answer = input("Digite a letra da resposta correta: ").strip().upper()
        if answer == q["correct"]:
            print("Resposta correta!\n")
            correct_answers += 1
        else:
            print(f"Resposta errada! A resposta correta é: {q['correct']}\n")
    total_questions = len(questions)
    score = (correct_answers / total_questions) * 100
    print(f"Você acertou {correct_answers} de {total_questions} perguntas.")
    print(f"Sua pontuação: {score:.2f}%\n")
    return score

# Função para realizar o quiz de cibersegurança
def cyber_quiz():
    questions = [
        {
            "question": "1. Qual é o principal objetivo da cibersegurança?",
            "options": [
                "A) Apenas proteger ativos financeiros.",
                "B) Proteger sistemas, dispositivos, dados e pessoas contra ameaças cibernéticas.",
                "C) Criar vírus para testar vulnerabilidades.",
                "D) Impedir qualquer acesso à internet."
            ],
            "correct": "B"
        },
        {
            "question": "2. Quais são algumas das ameaças cibernéticas mencionadas?",
            "options": [
                "A) Ransomware, phishing e roubo de dados.",
                "B) Ataques físicos a computadores.",
                "C) Desastres naturais como terremotos.",
                "D) Falhas em componentes de hardware."
            ],
            "correct": "A"
        },
        {
            "question": "3. Como a cibersegurança ajuda na proteção digital?",
            "options": [
                "A) Criando barreiras físicas para impedir o acesso a dispositivos.",
                "B) Aplicando tecnologias, práticas e políticas para prevenir ou mitigar ataques cibernéticos.",
                "C) Garantindo que todos os usuários tenham acesso irrestrito a qualquer sistema.",
                "D) Eliminando a necessidade de senhas e autenticação."
            ],
            "correct": "B"
        }
    ]
    return run_quiz(questions)

# Função para realizar o quiz de pensamento lógico computacional
def logic_quiz():
    questions = [
        {
            "question": "1. O que é o pensamento computacional?",
            "options": [
                "A) Um conjunto de regras para programar computadores.",
                "B) Uma estratégia para resolver problemas de forma eficiente, criando soluções genéricas.",
                "C) Uma técnica exclusiva para engenheiros de software.",
                "D) Um método para aprender apenas matemática avançada."
            ],
            "correct": "B"
        },
        {
            "question": "2. Quando o pensamento computacional deveria ser desenvolvido?",
            "options": [
                "A) Apenas na fase adulta, quando se aprende programação.",
                "B) Apenas por profissionais de tecnologia.",
                "C) Desde a infância, assim como outras disciplinas.",
                "D) Somente em cursos de ciência da computação."
            ],
            "correct": "C"
        },
        {
            "question": "3. O pensamento computacional está obrigatoriamente ligado ao ensino da programação?",
            "options": [
                "A) Sim, pois só pode ser aprendido escrevendo códigos.",
                "B) Não, pois é uma habilidade que pode ser desenvolvida sem programação.",
                "C) Sim, pois todas as soluções computacionais precisam de código.",
                "D) Não, pois só é útil em jogos e inteligência artificial."
            ],
            "correct": "B"
        }
    ]
    return run_quiz(questions)

# Menu principal
def main():
    introduction()
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
    main()