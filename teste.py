from aluno import Aluno
from disciplina import Disciplina
from matricula import Matricula
from aluno_graduacao import AlunoGraduacao
from aluno_mestrado import AlunoMestrado
from aluno_doutorado import AlunoDoutorado
from ru import RU

aluno1 = AlunoGraduacao(1, "Elias", "28/03/2003", "Cadastrado")
aluno2 = AlunoMestrado(2, "Cacau", "28/03/2003", "Cadastrado")
aluno3 = AlunoDoutorado(3, "Luiz", "28/03/2003", "Cadastrado")

disciplina1 = Disciplina(1, "Linguagem de Programação", 60)
matricula = Matricula(2022, 2, aluno1, disciplina1)

matricula.aprova_matricula(aluno1)
matricula.imprime_matriculas()

ru = RU()

aluno1.recebe_bolsa()
ru.compra_ticket(aluno1, 401)
aluno1.historico()
aluno1.saldo()

print()

aluno2.recebe_bolsa()
ru.compra_ticket(aluno2, 10)
aluno2.historico()
aluno2.saldo()

print()

aluno3.recebe_bolsa()
ru.compra_ticket(aluno3, 10)
aluno3.historico()
aluno3.saldo()

print()

ru.total_tickets()
ru.valor_total()