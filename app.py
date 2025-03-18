# Função para acessar o conteúdo do curso escolhido

print("Debug: Início do programa")

def access_course(course):
    print(f"\n=== Acessando o conteúdo do curso: {course} ===")
    if course == "Fundamentos de Cibersegurança":
        print("A cibersegurança refere-se a quaisquer tecnologias, práticas e políticas que atuem na prevenção de ataques cibernéticos ou na mitigação do seu impacto.")
        print("A cibersegurança tem como objetivo proteger sistemas de computador, aplicações, dispositivos, dados, ativos financeiros e pessoas contra ransomwares e outros malwares, golpes de phishing, roubo de dados e outras ameaças cibernéticas.")
        print("\nAgora, responda às perguntas abaixo para testar seus conhecimentos:\n")
        
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
                    "question": "2. Quais são algumas das ameaças cibernéticas mencionadas no trecho?",
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

            # Calcula a porcentagem de acertos
            total_questions = len(questions)
            score = (correct_answers / total_questions) * 100
            print(f"Você acertou {correct_answers} de {total_questions} perguntas.")
            print(f"Sua pontuação: {score:.2f}%\n")

            # Opção de refazer o quiz
            if correct_answers < total_questions:
                retry = input("Você gostaria de tentar novamente? (S/N): ").strip().upper()
                if retry == "S":
                    cyber_quiz()

        # Inicia o quiz de cibersegurança
        cyber_quiz()

    elif course == "Pensamento Lógico Computacional":
        print("O pensamento computacional é uma estratégia que permite resolver problemas, de forma eficiente, criando soluções genéricas para problemas variados, pertencentes a uma mesma classe.")
        print("Como habilidade humana, o pensamento computacional deveria ser desenvolvido desde a infância, assim como as demais disciplinas, não precisando, necessariamente, estar associado ao ensino da programação de computadores.")
        print("\nAgora, responda às perguntas abaixo para testar seus conhecimentos:\n")
        
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

            # Calcula a porcentagem de acertos
            total_questions = len(questions)
            score = (correct_answers / total_questions) * 100
            print(f"Você acertou {correct_answers} de {total_questions} perguntas.")
            print(f"Sua pontuação: {score:.2f}%\n")

            # Opção de refazer o quiz
            if correct_answers < total_questions:
                retry = input("Você gostaria de tentar novamente? (S/N): ").strip().upper()
                if retry == "S":
                    logic_quiz()

        # Inicia o quiz de pensamento lógico computacional
        logic_quiz()

    else:
        print(f"Bem-vindo ao curso de {course}!")
        print("Aqui você encontrará materiais, exercícios e muito mais para aprender e se desenvolver.")
    print("Aproveite o curso!\n")
    input("Pressione Enter para voltar ao menu principal...")  # Aguarda o usuário pressionar Enter para retornar ao menu