
# CRIA AS INSTÂNCIAS DE NOVOS PERSONAGENS A SEREM EXIBIDOS
class Persona:
    def __init__(self, name: str, relation: int, work: str):
        self.name = name
        self.relation = relation
        self.work = work

    def say(self, string: str):
        print(string)


claudia = Persona('Cláudia', 10, 'Jornalista')

