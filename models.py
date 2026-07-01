class Disciplina:
    def __init__(self, codigo, notas):
        self.__codigo = codigo
        self.__notas = notas

    def codigo(self):
        return self.__codigo

    def acessar_notas(self):
        return self.__notas

    def media(self):
        notas_validas = [nota for nota in self.__notas if nota is not None]

        return round(sum(notas_validas) / len(notas_validas), 2)
    
class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.__disciplinas = []

    def cadastrar_disciplina(self, disciplina):
        self.__disciplinas.append(disciplina)

    def listar_disciplinas(self):
        return self.__disciplinas