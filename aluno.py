class Aluno:
    def __init__(self, matricula, nome, data_nascimento, status):
        self._matricula = matricula
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._status = status

    @property
    def matricula(self):
        return self._matricula

    @matricula.setter
    def matricula(self, valor):
        self._matricula = valor

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, valor):
        self._status = valor