from aluno import Aluno


class AlunoDoutorado(Aluno):
    def __init__(self, matricula, nome, data_nascimento, status):
        super().__init__(matricula, nome, data_nascimento, status)
        self._ticket = 1.5

    def recebe_bolsa(self):
        self._bolsa = 2200
        self._historico.append(f"{self._nome} recebeu R$ {self._bolsa:.2f} da bolsa")



