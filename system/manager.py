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
        print('\n✅ Tarefa cadastrada com sucesso!')
        self.limpar_tela()

    def remover_tarefa(self, indice):
        if 0 <= indice < len(self.tarefas):
            removida = self.tarefas.pop(indice)
            self.salvar()
            print(f'\n✅ Tarefa [{removida.titulo}] removida com sucesso!')
            self.limpar_tela()
        else:
            print('\n⚠️  Índice iválido.')
            self.limpar_tela()

    def listar_tarefa(self):
        if not self.tarefas:
            print('\n⚠️  Nenhuma tarefa cadastrada.')
            self.limpar_tela()
            return
        print('')
        for i, tarefa in enumerate(self.tarefas, 1):
            print(f'{i} - {tarefa}')

    def editar_tarefa(self, indice, titulo=None, data_limite=None, prioridade=None):
        if 0 <= indice < len(self.tarefas):
            self.tarefas[indice].editar(titulo, data_limite, prioridade)
            self.salvar()
            print('\n✅ Tarefa atualizada com sucesso!')
            self.limpar_tela()
        else:
            print('\n⚠️  Índice iválido.')
            self.limpar_tela()

    def concluir_tarefa(self, indice):
        if 0 <= indice < len(self.tarefas):
            self.tarefas[indice].concluir()
            self.salvar()
            print('\n✅ Tarefa marcada como concluída.')
            self.limpar_tela()
        else:
            print('\n⚠️  Índice iválido.')
            self.limpar_tela()

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
                self.limpar_tela()
        else:
            self.tarefas = []

    def limpar_tela(self):
        sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
