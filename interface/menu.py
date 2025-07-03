from lib.task import Task
from system.manager import TaskManager


def exibir_menu():
    print("\n====== Gerenciador de Tarefas ======")
    print("[1] Adicionar tarefa")
    print("[2] Listar tarefas")
    print("[3] Concluir tarefa")
    print("[4] Editar tarefa")
    print("[5] Remover tarefa")
    print("[0] Sair")
    print("====================================")


def capturar_dados_tarefa():
    titulo = input('Título da tarefa: ')
    data = input('Data limite (dd/mm/aaaa): ')
    prioridade = int(input('Prioridade (1-5): '))
    return Task(titulo, data, prioridade)


def menu():
    gerenciador = TaskManager()

    while True:
        exibir_menu()
        try:
            escolha = input('Escolha uma opção: ')
            if escolha == '1':
                nova_tarefa = capturar_dados_tarefa()
                gerenciador.adicionar_taefa(nova_tarefa)
            elif escolha == '2':
                gerenciador.listar_tarefa()
            elif escolha == '3':
                if not gerenciador.tarefas:
                    print('\n⚠️  Nenhuma tarefa cadastrada.')
                else:
                    gerenciador.listar_tarefa()
                    try:
                        indice = int(
                            input('Digite o número da tarefa para concluir: ')) - 1
                        gerenciador.concluir_tarefa(indice)
                    except (ValueError, TypeError):
                        print('\n⚠️  Entra iválida.')
            elif escolha == '4':
                if not gerenciador.tarefas:
                    print('\n⚠️  Nenhuma tarefa cadastrada.')
                else:
                    gerenciador.listar_tarefa()
                    try:
                        indice = int(
                            input('Digite o número da tarefa para editar: ')) - 1
                        if 0 <= indice <= len(gerenciador.tarefas):
                            titulo = input(
                                'Novo título (ou Enter para manter): ').strip() or None
                            data = input(
                                'Nova data (ou Enter para manter): ').strip() or None
                            prioridade_input = input(
                                'Nova prioridade (ou Enter para manter): ').strip() or None
                            prioridade = int(
                                prioridade_input) if prioridade_input else None
                            gerenciador.editar_tarefa(
                                indice, titulo, data, prioridade)
                        else:
                            print('\n⚠️  Entrada iválida.')
                    except (ValueError, TypeError):
                        print('\n⚠️  Entrada iválida.')
            elif escolha == '5':
                if not gerenciador.tarefas:
                    print('\n⚠️  Nenhuma tarefa cadastrada.')
                else:
                    gerenciador.listar_tarefa()
                    try:
                        indice = int(
                            input('Digite o número da tarefa para remover: ')) - 1
                        if 0 < indice < len(gerenciador.tarefas):
                            gerenciador.remover_tarefa(indice)
                        else:
                            ('\n⚠️  Entrada iválida.')
                    except (ValueError, TypeError):
                        print('\n⚠️  Entrada iválida.')
            elif escolha == '0':
                print('\n👋 Saindo do programa...')
                break
            else:
                print('\n⚠️  Opção iválida, tente novamente.')
        except (ValueError, TypeError):
            print('\n⚠️  Entrada iválida.')
