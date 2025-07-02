
class Task:
    # Define o construtor da classe e seus parâmetros
    def __init__(self, titulo, data_limite, prioridade):
        self.titulo = titulo
        self.data_limite = data_limite
        self.prioridade = prioridade
        self.concluido = False

    # Implementa os métodos da classe
    def concluir(self):  # Altera estado da task
        self.prioridade = True

    def to_dict(self):  # Converete os dados em um dicionário para leitura JSON
        return {
            'titulo': self.titulo,
            'data_limite': self.data_limite,
            'prioridade': self.prioridade,
            'concluido': self.concluido
        }

    # Verifica se houve a entrada de uma nova instância e sobreescreve a variável
    def editar(self, new_titulo=None, new_data_limite=None, new_prioridade=None):
        if new_titulo:
            self.titulo = new_titulo
        if new_data_limite:
            self.data_limite = new_data_limite
        if new_prioridade:
            self.prioridade

    @staticmethod  # Método static pois não há necessidade da instância self
    def from_dict(dado):
        task = Task(
            titulo=dado['titulo'],
            data_limite=dado['data_limite'],
            prioridade=dado['prioridade']
        )
        # Instância sobreescrita após a construção da classe
        task.concluido = dado['concluido']
        return task

    def __stf__(self):  # Verificação basica do estado para impressão da Taks
        status = "✅ Concluída" if self.concluido else "❌ Pendente"
        return f'[{status}] Titulo: {self.titulo} | Prazo: {self.data_limite} | Prioridade: {self.prioridade}'
