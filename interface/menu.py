from lib.task import Task
from system.manager import TaskManager


def exibir_menu():
    print("\n====== Gerenciador de Tarefas ======")
    print("[1] Adicionar tarefa")
    print("[2] Listar tarefas")
    print("[3] Concluir tarefa")
    print("[4] Editar tarefa")
    print("[5] Remover tarefa")
    print("[6] Filtrar tarefas")
    print("[0] Sair")
    print("====================================")


def capturar_dados_tarefa():
    titulo = input('\nTítulo da tarefa: ')
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
                gerenciador.limpar_tela()
                print('\n📋  Tarefas cadastradas:')
                gerenciador.listar_tarefa()
            elif escolha == '3':
                gerenciador.limpar_tela()
                print('\n📋  Tarefas cadastradas:')
                if not gerenciador.tarefas:
                    print('\n⚠️  Nenhuma tarefa cadastrada.')
                    gerenciador.limpar_tela_e_pause()
                else:
                    gerenciador.listar_tarefa()
                    try:
                        indice = int(
                            input('\nDigite o número da tarefa para concluir: ')) - 1
                        gerenciador.concluir_tarefa(indice)
                    except (ValueError, TypeError):
                        print('\n⚠️  Entra iválida.')
                        gerenciador.limpar_tela()
            elif escolha == '4':
                gerenciador.limpar_tela()
                print('\n📋  Tarefas cadastradas:')
                if not gerenciador.tarefas:
                    print('\n⚠️  Nenhuma tarefa cadastrada.')
                    gerenciador.limpar_tela_e_pause()
                else:
                    gerenciador.listar_tarefa()
                    try:
                        indice = int(
                            input('\nDigite o número da tarefa para editar: ')) - 1
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
                            gerenciador.limpar_tela_e_pause()
                    except (ValueError, TypeError):
                        print('\n⚠️  Entrada iválida.')
                        gerenciador.limpar_tela_e_pause()
            elif escolha == '5':
                gerenciador.limpar_tela()
                print('\n📋  Tarefas cadastradas:')
                if not gerenciador.tarefas:
                    print('\n⚠️  Nenhuma tarefa cadastrada.')
                    gerenciador.limpar_tela_e_pause()
                else:
                    gerenciador.listar_tarefa()
                    try:
                        indice = int(
                            input('\nDigite o número da tarefa para remover: ')) - 1
                        if 0 <= indice < len(gerenciador.tarefas):
                            gerenciador.remover_tarefa(indice)
                        else:
                            ('\n⚠️  Entrada iválida.')
                            gerenciador.limpar_tela_e_pause()
                    except (ValueError, TypeError):
                        print('\n⚠️  Entrada iválida.')
                        gerenciador.limpar_tela_e_pause()
            elif escolha == '6':
                gerenciador.limpar_tela()
                print("\n[1] Tarefas pendentes")
                print("[2] Tarefas concluídas")
                print("[3] Filtrar por prioridade")
                filtro = input("Escolha uma opção de filtro: ")

                if filtro == '1':
                    gerenciador.limpar_tela()
                    print('\n📋  Tarefas pendentes:')
                    gerenciador.filtrar_pendentes()
                elif filtro == '2':
                    gerenciador.limpar_tela()
                    print('\n📋  Tarefas concluídas:')
                    gerenciador.filtrar_concluidas()
                elif filtro == '3':
                    gerenciador.limpar_tela()
                    gerenciador.filtrar_prioridade()
                else:
                    print('\n⚠️  Opção iválida, tente novamente.')
                    gerenciador.limpar_tela_e_pause()
            elif escolha == '0':
                print('\n👋 Saindo do programa...')
                gerenciador.limpar_tela_e_pause()
                break
            else:
                print('\n⚠️  Opção iválida, tente novamente.')
                gerenciador.limpar_tela_e_pause()
        except (ValueError, TypeError):
            print('\n⚠️  Entrada iválida.')
            gerenciador.limpar_tela_e_pause()
        except KeyboardInterrupt:
            print('\n⚠️  Usuário interrompeu o programa.')
            print('👋 Saindo do programa...')
            gerenciador.limpar_tela_e_pause()
            break
