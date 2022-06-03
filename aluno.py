from ru import RU

class Aluno(RU):
    def __init__(self, matricula, nome, data_nascimento, status):
        self._matricula = matricula
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._status = status
        self._bolsa = 0
        self._ticket = 0
        self._historico = []

    @property
    def matricula(self):
        return self._matricula

    @matricula.setter
    def matricula(self, valor):
        self._matricula = valor

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor

    @property
    def data_nascimento(self):
        return self._data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, valor):
        self._data_nascimento = valor

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, valor):
        self._status = valor

    @property
    def ticket(self):
        return self._ticket

    @property
    def bolsa(self):
        return self._bolsa

    @bolsa.setter
    def bolsa(self, valor):
        self._bolsa = valor

    def saldo(self):
        return print(f"Saldo do aluno {self._nome}: R$ {self._bolsa:.2f}")

    def historico(self):
        for h in self._historico:
            print(h)