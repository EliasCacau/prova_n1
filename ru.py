class RU:
    _total_tickets = 0
    _valor_total = 0

    @classmethod
    def total_tickets(cls):
        return print(RU._total_tickets)

    @classmethod
    def valor_total(cls):
        return print(RU._valor_total)

    def compra_ticket(self, aluno, qnt):
        soma = aluno.ticket * qnt
        if aluno.bolsa >= soma:
            aluno.bolsa -= soma
            RU._total_tickets += qnt
            RU._valor_total += soma
            aluno._historico.append(f"{aluno.nome} comprou {qnt} tickets")
        else:
            aluno._historico.append(f"{aluno.nome} Saldo insuficiente")

