"""
Sistema de Cadastro de Alunos
Programa de terminal para cadastrar, listar, buscar e remover alunos,
além de calcular a média geral das notas.
"""


def ler_nome(mensagem):
    """Pede um nome e repete a pergunta até o usuário digitar algo."""
    while True:
        nome = input(mensagem).strip()
        if nome:
            return nome
        print("O nome não pode ficar vazio.")


def ler_idade():
    """Pede a idade e valida se é um número inteiro maior que 0."""
    while True:
        try:
            idade = int(input("Idade: "))
            if idade > 0:
                return idade
            print("A idade deve ser maior que 0.")
        except ValueError:
            print("Digite um número inteiro válido.")


def ler_nota():
    """Pede a nota e valida se é um número entre 0 e 10."""
    while True:
        try:
            nota = float(input("Nota (0 a 10): ").replace(",", "."))
            if 0 <= nota <= 10:
                return nota
            print("A nota deve estar entre 0 e 10.")
        except ValueError:
            print("Digite um número válido.")


def adicionar_aluno(alunos):
    """Cadastra um novo aluno (dicionário) na lista de alunos."""
    print("\n--- Adicionar aluno ---")
    nome = ler_nome("Nome: ")
    idade = ler_idade()
    nota = ler_nota()

    aluno = {"nome": nome, "idade": idade, "nota": nota}
    alunos.append(aluno)
    print(f"Aluno {nome} cadastrado com sucesso!")


def listar_alunos(alunos):
    """Mostra todos os alunos cadastrados."""
    print("\n--- Lista de alunos ---")
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    for aluno in alunos:
        print(f"Nome: {aluno['nome']} | Idade: {aluno['idade']} | Nota: {aluno['nota']:.1f}")


def buscar_aluno(alunos):
    """Busca um aluno pelo nome (ignorando maiúsculas e minúsculas)."""
    print("\n--- Buscar aluno ---")
    nome = ler_nome("Nome do aluno: ").lower()

    for aluno in alunos:
        if aluno["nome"].lower() == nome:
            print("Aluno encontrado!")
            print(f"Nome: {aluno['nome']} | Idade: {aluno['idade']} | Nota: {aluno['nota']:.1f}")
            return

    print("Erro: aluno não encontrado.")


def remover_aluno(alunos):
    """Remove um aluno da lista pelo nome."""
    print("\n--- Remover aluno ---")
    nome = ler_nome("Nome do aluno: ").lower()

    for aluno in alunos:
        if aluno["nome"].lower() == nome:
            alunos.remove(aluno)
            print(f"Aluno {aluno['nome']} removido com sucesso!")
            return

    print("Aviso: aluno não encontrado.")


def media_geral(alunos):
    """Calcula e mostra a média de todas as notas."""
    print("\n--- Média geral ---")
    if not alunos:
        print("Não há alunos cadastrados para calcular a média.")
        return

    total = sum(aluno["nota"] for aluno in alunos)
    media = total / len(alunos)
    print(f"Média geral das notas: {media:.2f}")


def exibir_menu():
    """Mostra as opções do menu."""
    print("\n===== CADASTRO DE ALUNOS =====")
    print("1. Adicionar aluno")
    print("2. Listar todos os alunos")
    print("3. Buscar aluno pelo nome")
    print("4. Remover aluno")
    print("5. Mostrar média geral das notas")
    print("6. Sair")


def main():
    """Loop principal: mantém o programa rodando até o usuário sair."""
    alunos = []

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            adicionar_aluno(alunos)
        elif opcao == "2":
            listar_alunos(alunos)
        elif opcao == "3":
            buscar_aluno(alunos)
        elif opcao == "4":
            remover_aluno(alunos)
        elif opcao == "5":
            media_geral(alunos)
        elif opcao == "6":
            print("Encerrando o programa. Até logo!")
            break
        else:
            print("Opção inválida. Escolha um número de 1 a 6.")


if __name__ == "__main__":
    main()
