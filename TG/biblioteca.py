from datetime import datetime, timedelta


# =========================
# DADOS DO SISTEMA
# =========================

livros = {
    1: {
        "titulo": "Anatomia Humana",
        "autor": "J. D. Smith",
        "categoria": "Enfermagem",
        "disponivel": True
    },
    2: {
        "titulo": "Farmacologia Básica",
        "autor": "Katzung",
        "categoria": "Farmácia",
        "disponivel": True
    },
    3: {
        "titulo": "Python para Iniciantes",
        "autor": "Autor Exemplo",
        "categoria": "Tecnologia",
        "disponivel": True
    }
}

alunos = {
    1: {
        "nome": "João",
        "matricula": "2026001",
        "regular": True
    },
    2: {
        "nome": "Maria",
        "matricula": "2026002",
        "regular": True
    }
}

emprestimos = []

# Valor da multa por dia de atraso
MULTA_POR_DIA = 2.00


# =========================
# FUNÇÕES AUXILIARES
# =========================

def encontrar_aluno(matricula):
    for aluno_id, aluno in alunos.items():
        if aluno["matricula"] == matricula:
            return aluno_id, aluno

    return None, None


def encontrar_emprestimo(matricula, livro_id):
    for emprestimo in emprestimos:
        if (
            emprestimo["matricula"] == matricula
            and emprestimo["livro_id"] == livro_id
            and emprestimo["devolvido"] is False
        ):
            return emprestimo

    return None


def calcular_multa(data_devolucao, data_limite):
    atraso = (data_devolucao - data_limite).days

    if atraso > 0:
        return atraso * MULTA_POR_DIA

    return 0.0


# =========================
# LIVROS
# =========================

def listar_livros():
    print("\n===== LIVROS DA BIBLIOTECA =====")

    for livro_id, livro in livros.items():

        if livro["disponivel"]:
            status = "Disponível"
        else:
            status = "Emprestado"

        print(f"""
ID: {livro_id}
Título: {livro['titulo']}
Autor: {livro['autor']}
Categoria: {livro['categoria']}
Status: {status}
-----------------------------
""")


def cadastrar_livro():
    print("\n===== CADASTRO DE LIVRO =====")

    titulo = input("Título: ")
    autor = input("Autor: ")
    categoria = input("Categoria: ")

    novo_id = max(livros.keys()) + 1

    livros[novo_id] = {
        "titulo": titulo,
        "autor": autor,
        "categoria": categoria,
        "disponivel": True
    }

    print("\nLivro cadastrado com sucesso!")


# =========================
# ALUNOS
# =========================

def cadastrar_aluno():
    print("\n===== CADASTRO DE ALUNO =====")

    nome = input("Nome: ")
    matricula = input("Matrícula: ")

    novo_id = max(alunos.keys()) + 1

    alunos[novo_id] = {
        "nome": nome,
        "matricula": matricula,
        "regular": True
    }

    print("\nAluno cadastrado com sucesso!")


# =========================
# EMPRÉSTIMO
# =========================

def realizar_emprestimo():

    print("\n===== EMPRÉSTIMO =====")

    matricula = input("Digite a matrícula do aluno: ")

    aluno_id, aluno = encontrar_aluno(matricula)

    # Verificação da matrícula
    if aluno is None:
        print("\nAluno não encontrado.")
        return

    if not aluno["regular"]:
        print("\nAluno não está regular.")
        return

    listar_livros()

    try:
        livro_id = int(input("Digite o ID do livro: "))
    except ValueError:
        print("\nID inválido.")
        return

    if livro_id not in livros:
        print("\nLivro não encontrado.")
        return

    livro = livros[livro_id]

    # Verificação da disponibilidade
    if not livro["disponivel"]:
        print("\nEste livro já está emprestado.")
        return

    # Data do empréstimo
    hoje = datetime.now()
    data_limite = hoje + timedelta(days=7)

    emprestimo = {
        "matricula": matricula,
        "livro_id": livro_id,
        "data_emprestimo": hoje,
        "data_limite": data_limite,
        "renovacoes": 0,
        "devolvido": False
    }

    emprestimos.append(emprestimo)

    livro["disponivel"] = False

    print("\n===== EMPRÉSTIMO REALIZADO =====")
    print(f"Aluno: {aluno['nome']}")
    print(f"Livro: {livro['titulo']}")
    print(f"Data do empréstimo: {hoje.strftime('%d/%m/%Y')}")
    print(f"Data limite: {data_limite.strftime('%d/%m/%Y')}")


# =========================
# RENOVAÇÃO
# =========================

def renovar_livro():

    print("\n===== RENOVAÇÃO =====")

    matricula = input("Digite a matrícula: ")

    try:
        livro_id = int(input("Digite o ID do livro: "))
    except ValueError:
        print("\nID inválido.")
        return

    emprestimo = encontrar_emprestimo(matricula, livro_id)

    if emprestimo is None:
        print("\nEmpréstimo não encontrado.")
        return

    if emprestimo["renovacoes"] >= 3:
        print("\nO limite de 3 renovações foi atingido.")
        return

    # Acrescenta mais 7 dias
    emprestimo["data_limite"] += timedelta(days=7)
    emprestimo["renovacoes"] += 1

    print("\nLivro renovado com sucesso!")
    print(
        f"Nova data limite: "
        f"{emprestimo['data_limite'].strftime('%d/%m/%Y')}"
    )
    print(f"Renovações utilizadas: {emprestimo['renovacoes']}/3")


# =========================
# DEVOLUÇÃO
# =========================

def devolver_livro():

    print("\n===== DEVOLUÇÃO =====")

    matricula = input("Digite a matrícula: ")

    try:
        livro_id = int(input("Digite o ID do livro: "))
    except ValueError:
        print("\nID inválido.")
        return

    emprestimo = encontrar_emprestimo(matricula, livro_id)

    if emprestimo is None:
        print("\nEmpréstimo não encontrado.")
        return

    hoje = datetime.now()

    multa = calcular_multa(
        hoje,
        emprestimo["data_limite"]
    )

    livro = livros[livro_id]

    # Pergunta sobre o estado do livro
    print("\nInspeção do livro:")
    print("1 - Livro em boas condições")
    print("2 - Livro danificado")

    estado = input("Escolha: ")

    emprestimo["data_devolucao"] = hoje
    emprestimo["multa"] = multa
    emprestimo["devolvido"] = True

    livro["disponivel"] = True

    print("\n===== DEVOLUÇÃO CONCLUÍDA =====")
    print(f"Livro: {livro['titulo']}")

    if estado == "2":
        print("ATENÇÃO: o livro foi marcado como danificado.")
        print("O aluno poderá ser acionado para reposição.")

    if multa > 0:
        print(f"Multa por atraso: R$ {multa:.2f}")
    else:
        print("Nenhuma multa foi aplicada.")

    print("Livro retornou ao estoque.")


# =========================
# HISTÓRICO
# =========================

def mostrar_historico():

    print("\n===== HISTÓRICO DE EMPRÉSTIMOS =====")

    if not emprestimos:
        print("Nenhum empréstimo registrado.")
        return

    for emprestimo in emprestimos:

        livro = livros[emprestimo["livro_id"]]

        status = (
            "Devolvido"
            if emprestimo["devolvido"]
            else "Em andamento"
        )

        print(f"""
Aluno: {emprestimo['matricula']}
Livro: {livro['titulo']}
Empréstimo: {emprestimo['data_emprestimo'].strftime('%d/%m/%Y')}
Prazo: {emprestimo['data_limite'].strftime('%d/%m/%Y')}
Renovações: {emprestimo['renovacoes']}
Status: {status}
-----------------------------
""")


# =========================
# MENU PRINCIPAL
# =========================

def menu():

    while True:

        print("""
========================================
       BIBLIOTECA ESCOLA SÃO BERNARDO
========================================

1 - Listar livros
2 - Cadastrar livro
3 - Cadastrar aluno
4 - Realizar empréstimo
5 - Renovar empréstimo
6 - Devolver livro
7 - Ver histórico
0 - Sair

========================================
""")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_livros()

        elif opcao == "2":
            cadastrar_livro()

        elif opcao == "3":
            cadastrar_aluno()

        elif opcao == "4":
            realizar_emprestimo()

        elif opcao == "5":
            renovar_livro()

        elif opcao == "6":
            devolver_livro()

        elif opcao == "7":
            mostrar_historico()

        elif opcao == "0":
            print("\nSistema encerrado.")
            break

        else:
            print("\nOpção inválida.")


# =========================
# INÍCIO DO PROGRAMA
# =========================

if __name__ == "__main__":
    menu()
