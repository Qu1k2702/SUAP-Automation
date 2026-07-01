import scraper

notas_coletadas = scraper.coletar_notas("Thales")

aluno = notas_coletadas["Aluno"]
notas_por_materia = notas_coletadas["Notas"]

bio = notas_por_materia["ART2"]

print(aluno.listar_disciplinas())
print(bio.acessar_notas())
print(aluno.nome)