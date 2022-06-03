class Disciplina:
    def __init__(self, codigo, nome, ch):
        self._codigo = codigo
        self._nome = nome
        self._ch = ch

    def __str__(self):
        return self._nome