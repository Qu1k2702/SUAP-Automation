from playwright.sync_api import sync_playwright
import os
import media
from models import Disciplina, Aluno
from dotenv import load_dotenv

def coletar_notas(nome_aluno: str):
    
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
        load_dotenv()
       
        USUARIO = os.getenv("SUAP_USER")
        SENHA = os.getenv("SUAP_PASSWORD")

        user.fill(USUARIO)
        password.fill(SENHA)
        login_button.click()

        #Acessar boletim
        page.get_by_role("link", name="Ensino").click()
        page.get_by_role("link", name="Boletins").click()

        #Boletim
        page.wait_for_selector("#tabela_boletim tbody tr")
        
        boletim = page.locator("#tabela_boletim")

        linhas = boletim.locator("tbody tr")

        notas = {}

        aluno = Aluno(nome_aluno)

        for i in range(linhas.count()):
            linha = linhas.nth(i)
            colunas = linha.locator("td")

            codigo_materia = colunas.nth(2).text_content().strip()[14:18]
            indices = [9, 11, 13, 15]

            notas_materia = [
                media.converter_notas(colunas.nth(i).text_content()) for i in indices]

            disciplina = Disciplina(codigo_materia, notas_materia)

            notas[codigo_materia] = disciplina

            aluno.cadastrar_disciplina(codigo_materia)

    return {"Notas": notas, "Aluno": aluno}