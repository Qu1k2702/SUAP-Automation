from playwright.sync_api import sync_playwright
import time

notas = {}

def converter_notas(nota: str):
    if nota == "-":
        return "_"
    
    return float(nota.replace(",","."))

def validar_nota(nota):
    if nota == "_":
        return False
    
    return True
    
def calcular_media_materia(materia: str):
    notas_por_bimestre = []
    nota_total = 0

    for i in notas[materia]:
        if validar_nota(i):
            notas_por_bimestre.append(i)
            nota_total += i

    media = round(nota_total / len(notas_por_bimestre), 2)

    return f"Materia: {materia} \n Bimestres concluidos: {len(notas_por_bimestre)} \n  Media: {media}"

with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=True)
    #Abrir navegador
    page = browser.new_page()

    #Navegar para uma pagina
    page.goto("https://suap.ifsp.edu.br/accounts/login/?next=/")

    #Encontrar elementos
    user = page.get_by_role("textbox", name="Usuário:")
    password = page.get_by_role("textbox", name="Senha:")
    login_button = page.get_by_role("button", name="Acessar")

    #Login
    user.fill('VP3025501')
    password.fill('Thales-123')
    login_button.click()

    #Acessar boletim
    page.get_by_role("link", name="Ensino").click()
    page.get_by_role("link", name="Boletins").click()

    #Boletim
    page.wait_for_selector("#tabela_boletim tbody tr")
    
    boletim = page.locator("#tabela_boletim")

    linhas = boletim.locator("tbody tr")


    for i in range(linhas.count()):
        linha = linhas.nth(i)

        disciplina = linha.locator("td").nth(2).text_content().strip()[14:18]
        nota_n1 = converter_notas(linha.locator("td").nth(9).text_content().strip())
        nota_n2 = converter_notas(linha.locator("td").nth(11).text_content().strip())
        nota_n3 = converter_notas(linha.locator("td").nth(13).text_content().strip())
        nota_n4 = converter_notas(linha.locator("td").nth(15).text_content().strip())

        #print(f"{disciplina}: Bim1: {nota_n1} | Bim2: {nota_n2} | Bim3: {nota_n3} | Bim4: {nota_n4}")
        notas[disciplina] = [nota_n1, nota_n2, nota_n3, nota_n4]

    browser.close()
    
print(calcular_media_materia("BIO2"))
print("="*30)
print(calcular_media_materia("MAT3"))