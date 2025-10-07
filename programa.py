import sys

class Paciente:
    def __init__(self, nome, idade, prioridade):
        self.nome = nome
        self.idade = idade
        self.prioridade = prioridade
        self.proximo = None
        self.anterior = None

    def __str__(self):
        tipo = "(P)" if self.prioridade == 'P' else "(N)"
        return f"[ {self.nome} {tipo} ]"

class filaAtendimento:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def mostrarMemoria(self, antes, depois):
        print(f"Memória antes: {antes} bytes | depois: {depois} bytes | diferença: {depois - antes} bytes")

    def adicionarPaciente(self, nome, idade, prioridade):
        antes = sys.getsizeof(self)
        novo = Paciente(nome, idade, prioridade)
        if self.inicio is None:
            self.inicio = self.fim = novo
        elif prioridade == 'P':
            atual = self.inicio
            while atual.proximo and atual.proximo.prioridade == 'P':
                atual = atual.proximo
            novo.proximo = atual.proximo
            novo.anterior = atual
            if atual.proximo:
                atual.proximo.anterior = novo
            else:
                self.fim = novo
            atual.proximo = novo
        else:
            self.fim.proximo = novo
            novo.anterior = self.fim
            self.fim = novo
        depois = sys.getsizeof(self)
        print(f"Paciente {nome} adicionado.")
        self.mostrarMemoria(antes, depois)

    def removerPaciente(self):
        if self.inicio is None:
            print("Fila vazia.")
            return
        antes = sys.getsizeof(self)
        removido = self.inicio
        self.inicio = removido.proximo
        if self.inicio:
            self.inicio.anterior = None
        else:
            self.fim = None
        depois = sys.getsizeof(self)
        print(f"Paciente {removido.nome} foi atendido e removido.")
        self.mostrarMemoria(antes, depois)

    def alterarPaciente(self, nome, novo_nome=None, nova_idade=None, nova_prioridade=None):
        atual = self.inicio
        while atual:
            if atual.nome == nome:
                antes = sys.getsizeof(self)
                if novo_nome:
                    atual.nome = novo_nome
                if nova_idade:
                    atual.idade = nova_idade
                if nova_prioridade:
                    atual.prioridade = nova_prioridade
                depois = sys.getsizeof(self)
                print(f"Dados do paciente {nome} foram alterados.")
                self.mostrarMemoria(antes, depois)
                return
            atual = atual.proximo
        print(f"Paciente {nome} não encontrado.")

    def mostrarFila(self):
        atual = self.inicio
        representacao = ""
        while atual:
            representacao += str(atual)
            if atual.proximo:
                representacao += " --> "
            atual = atual.proximo
        print("Fila:", representacao if representacao else "vazia")

    def mostrarInvertida(self):
        atual = self.fim
        representacao = ""
        while atual:
            representacao += str(atual)
            if atual.anterior:
                representacao += " --> "
            atual = atual.anterior
        print("Fila invertida:", representacao if representacao else "vazia")


fila = filaAtendimento()
pacientes_exemplo = [
    ("Gabriel", 30, "P"),
    ("Heitor", 25, "N"),
    ("Eduardo", 40, "P"),
    ("Ygor", 20, "N"),
    ("Igor", 50, "P"),
    ("Felipe", 33, "N"),
    ("Carlos", 60, "P"),
    ("Clara", 28, "N"),
    ("Rafaela", 45, "P"),
    ("Luiza", 18, "N"),
]

for nome, idade, prioridade in pacientes_exemplo:
    fila.adicionarPaciente(nome, idade, prioridade)

fila.mostrarFila()
fila.removerPaciente()
fila.mostrarFila()
fila.alterarPaciente("Heitor", nova_idade=26, nova_prioridade="P")
fila.mostrarInvertida()
