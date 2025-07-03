from lib.task import Task
from time import sleep
import json
import os


class TaskManager:
    def __init__(self, caminho_arquivo='data/tasks.json'):
        self.caminho_arquivo = caminho_arquivo
        self.tarefas = []
        self.carregar()

    def adicionar_taefa(self, task):
        self.tarefas.append(task)
        self.salvar()
        self.limpar_tela()
        print('\n✅ Tarefa cadastrada com sucesso!')
        self.limpar_tela_e_pause()

    def remover_tarefa(self, indice):
        if 0 <= indice < len(self.tarefas):
            removida = self.tarefas.pop(indice)
            self.salvar()
            self.limpar_tela()
            print(f'\n✅ Tarefa [{removida.titulo}] removida com sucesso!')
            self.limpar_tela_e_pause()
        else:
            print('\n⚠️  Índice iválido.')
            self.limpar_tela_e_pause()

    def listar_tarefa(self):
        if not self.tarefas:
            print('\n⚠️  Nenhuma tarefa cadastrada.')
            self.limpar_tela_e_pause()
            return
        print('')
        for i, tarefa in enumerate(self.tarefas, 1):
            print(f'{i} - {tarefa}')

    def filtrar_pendentes(self):
        if not self.tarefas:
            print('\n⚠️  Nenhuma tarefa cadastrada.')
            self.limpar_tela_e_pause()
            return
        print('')
        pendentes = [tarefa for tarefa in self.tarefas if not tarefa.concluido]
        for i, tarefa in enumerate(pendentes, 1):
            print(f'{i} - {tarefa}')

    def filtrar_concluidas(self):
        if not self.tarefas:
            print('\n⚠️  Nenhuma tarefa cadastrada.')
            self.limpar_tela_e_pause()
            return
        print('')
        concluidas = [tarefa for tarefa in self.tarefas if tarefa.concluido]
        if not concluidas:
            print('⚠️  Nenhuma tarefa concluída.')
            self.limpar_tela_e_pause()
            return
        for i, tarefa in enumerate(concluidas, 1):
            print(f'{i} - {tarefa}')

    def filtrar_prioridade(self):
        if not self.tarefas:
            print('\n⚠️  Nenhuma tarefa cadastrada.')
            self.limpar_tela_e_pause()
            return
        print('')
        try:
            prioridade_input = int(input("Digite a prioridade (1-5): "))
            if 0 <= prioridade_input <= 5:
                filtro_prioridade = [
                    tarefa for tarefa in self.tarefas if tarefa.prioridade == prioridade_input]
                self.limpar_tela()
                print(
                    f'\n📋  Tarefas filtradas por prioridade nível ({prioridade_input}):')
                print('')
                for i, tarefa in enumerate(filtro_prioridade, 1):
                    print(f'{i} - {tarefa}')
            else:
                print('\n⚠️  Valor de prioridade iválida.')
                return
        except (TypeError, ValueError):
            print('\n⚠️  Entrada iválida.')

    def editar_tarefa(self, indice, titulo=None, data_limite=None, prioridade=None):
        if 0 <= indice < len(self.tarefas):
            self.tarefas[indice].editar(titulo, data_limite, prioridade)
            self.salvar()
            self.limpar_tela()
            print('\n✅ Tarefa atualizada com sucesso!')
            self.limpar_tela_e_pause()
        else:
            print('\n⚠️  Índice iválido.')
            self.limpar_tela_e_pause()

    def concluir_tarefa(self, indice):
        if 0 <= indice < len(self.tarefas):
            self.tarefas[indice].concluir()
            self.salvar()
            self.limpar_tela()
            print('\n✅ Tarefa marcada como concluída.')
            self.limpar_tela_e_pause()
        else:
            print('\n⚠️  Índice iválido.')
            self.limpar_tela_e_pause()

    def salvar(self):
        with open(self.caminho_arquivo, 'w', encoding='utf-8') as arquivo:
            json.dump([task.to_dict() for task in self.tarefas],
                      arquivo, indent=4, ensure_ascii=False)

    def carregar(self):
        if os.path.exists(self.caminho_arquivo):
            try:
                with open(self.caminho_arquivo, 'r', encoding='utf-8') as arquivo:
                    dados = json.load(arquivo)
                    self.tarefas = [Task.from_dict(d) for d in dados]
            except (json.JSONDecodeError, UnicodeDecodeError):
                print('\n⚠️  Erro ao carregar arquivo. Inexistente ou corrompido.')
                self.tarefas = []
                self.salvar()
                self.limpar_tela_e_pause()
        else:
            self.tarefas = []

    def limpar_tela(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def limpar_tela_e_pause(self):
        sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
