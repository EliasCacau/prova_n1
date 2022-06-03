class Matricula:
    _matriculas = []
    def __init__(self, ano, semestre, aluno, disciplina):
        self._ano = ano
        self._semestre = semestre
        self._aluno = aluno
        self._disciplina = disciplina

    def aprova_matricula(self, aluno):
        aluno.status = "Matriculado"
        Matricula._matriculas.append(f"Aluno {aluno.nome} devidamente matriculado na disciplina {self._disciplina}| Ano: {self._ano} | Semestre: {self._semestre}")
        return aluno.status

    def imprime_matriculas(cls):
        for m in Matricula._matriculas:
            print(m)