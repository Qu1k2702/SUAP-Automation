import scraper

disciplinas = scraper.coletar_notas()

bio = disciplinas["BIO2"]

print(bio.media())