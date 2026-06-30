class Disciplina:
    def __init__(self, codigo, notas):
        self.codigo = codigo
        self.notas = notas

    def media(self):
        notas_validas = [nota for nota in self.notas if nota is not None]

        return round(sum(notas_validas) / len(notas_validas), 2)