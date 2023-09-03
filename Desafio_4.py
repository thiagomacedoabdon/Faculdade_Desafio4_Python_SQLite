# Professor, fiz um pouco diferente. Eu primeiro criei o banco de dados, depois coloquei as opções dentro de funções
# função para add novo aluno e add professor
# função para excluir aluno e professor 
# função para consulta no banco de alunos e professores
# E por último (não foi pedido, mas quis incrementar mais o desafio) 
# fiz um laço de repetição while para criar a interação com o usuário e fazer a gestão do banco pelo terminal do VS Code também.

import sqlite3

def criar_banco():
    conexao = sqlite3.connect("cadastro_academia.db")
    cursor = conexao.cursor()

    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS alunos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    idade INTEGER)
    """)

    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS professores (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL)
    """)

    conexao.commit()
    conexao.close()

# add aluno 
def adicionar_aluno(nome, idade):
    conexao = sqlite3.connect("cadastro_academia.db")
    cursor = conexao.cursor()

    cursor.execute("INSERT INTO alunos (nome, idade) VALUES (?, ?)", (nome, idade))

    conexao.commit()
    conexao.close()

# add professor
def adicionar_professor(nome):
    conexao = sqlite3.connect("cadastro_academia.db")
    cursor = conexao.cursor()

    cursor.execute("INSERT INTO professores (nome) VALUES (?)", (nome,))

    conexao.commit()
    conexao.close()

# excluir aluno 
def excluir_aluno(id):
    conexao = sqlite3.connect("cadastro_academia.db")
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM alunos WHERE id=?", (id,))

    conexao.commit()
    conexao.close()

# excluir professor
def excluir_professor(id):
    conexao = sqlite3.connect("cadastro_academia.db")
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM professores WHERE id=?", (id,))

    conexao.commit()
    conexao.close()

# alunos
def listar_alunos():
    conexao = sqlite3.connect("cadastro_academia.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM alunos")
    alunos = cursor.fetchall()

    conexao.close()

    return alunos

# aluno menor
def consultar_alunos_menor_de_idade():
    conexao = sqlite3.connect("cadastro_academia.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM alunos WHERE idade < 18")
    alunos_menor_de_idade = cursor.fetchall()

    conexao.close()

    return alunos_menor_de_idade

# professores
def listar_professores():
    conexao = sqlite3.connect("cadastro_academia.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM professores")
    professores = cursor.fetchall()

    conexao.close()

    return professores

criar_banco()

while True: 
    print("\nMenu:")
    print("""
    1. Adicionar Aluno
    2. Adicionar Professor
    3. Excluir Aluno
    4. Excluir Professor
    5. Listar Alunos
    6. Listar Professores
    7. Consultar aluno menor de idade
    0. Sair
    """)

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do aluno: ")
        idade = int(input("Idade do aluno: "))
        adicionar_aluno(nome, idade)
        print("Aluno adicionado com sucesso!")

    elif opcao == "2":
        nome = input("Nome do professor: ")
        adicionar_professor(nome)
        print("Professor adicionado com sucesso!")

    elif opcao == "3":
        id = int(input("ID do aluno a ser excluído: "))
        excluir_aluno(id)
        print("Aluno excluído com sucesso!")

    elif opcao == "4":
        id = int(input("ID do professor a ser excluído: "))
        excluir_professor(id)
        print("Professor excluído com sucesso!")

    elif opcao == "5":
        alunos = listar_alunos()
        print("\nLista de Alunos:")
        for aluno in alunos:
            print(f"ID: {aluno[0]}, Nome: {aluno[1]}, Idade: {aluno[2]}")

    elif opcao == "6":
        professores = listar_professores()
        print("\nLista de Professores:")
        for professor in professores:
            print(f"ID: {professor[0]}, Nome: {professor[1]}")

    elif opcao == "7":
        alunos_menor_de_idade = consultar_alunos_menor_de_idade()
        print("\nAlunos menores de idade:")
        for aluno in alunos_menor_de_idade:
            print(f"ID: {aluno[0]}, Nome: {aluno[1]}, Idade: {aluno[2]}")

    elif opcao == "0":
        print("Obrigado pela sua visita!")
        break

    else:
        print("Opção inválida. Tente novamente.")

