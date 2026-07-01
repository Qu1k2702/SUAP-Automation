import scraper

notas_coletadas = scraper.coletar_notas()

aluno = notas_coletadas[1]
notas_por_materia = notas_coletadas[0]

bio = notas_por_materia["BIO2"]

print(aluno.listar_disciplinas())
print(bio.acessar_notas())