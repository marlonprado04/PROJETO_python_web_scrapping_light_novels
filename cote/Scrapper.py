from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

class Scrapper:
    def __init__(self, url="https://animecenterbr.com/youkoso-jitsuryoku-light-novel-pt-br", options=None):
        self.url = url
        if options is None:
            options = webdriver.ChromeOptions()
            options.add_argument('--ignore-certificate-errors')
            options.add_argument('--ignore-ssl-errors')
        self.driver = webdriver.Chrome(options=options)

    # Define função para aguardar renderização do body
    def render_body_content(self, seconds=10):
        
        # Inicia web driver a partir da URL
        self.driver.get(self.url)
        
        # Espera até que o body seja carregado na página
        wait = WebDriverWait(self.driver, seconds)
        try:
            wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        except Exception as e:
            print("TimeoutException:", e)

    # Define função para retornar uma lista de elementos de determinadas tags
    def list_elements_by_tag_name(self, tag):
        # Renderiza body
        self.render_body_content()

        # Encontra todas as tags procuradas na página
        tags = self.driver.find_elements(By.TAG_NAME, tag)

        # Cria variável para armazenar tags
        values = []

        # Armazena cada elemento na lista de valores
        for element in tags:
            values.append(element.get_attribute("outerHTML"))

        return values

    def list_elements_by_css_selector(self, selector):
        # Renderiza body
        self.render_body_content()

        # Encontra todos os elementos com o seletor CSS especificado na página
        elements = self.driver.find_elements(By.CSS_SELECTOR, selector)

        # Cria uma lista para armazenar os conteúdos HTML
        html_contents = []

        # Extrai o conteúdo HTML de cada elemento e armazena na lista
        for element in elements:
            html_contents.append(element.get_attribute("outerHTML"))

        # Retorna os conteúdos HTML concatenados em uma única string
        return '\n'.join(html_contents)

    # Define função para retornar uma lista de elementos de determinadas classes
    def list_elements_by_class(self, class_name):
        # Renderiza body
        self.render_body_content()

        # Encontra todos os elementos com a classe especificada na página
        elements = self.driver.find_elements(By.CSS_SELECTOR, f".{class_name}")

        # Cria variável para armazenar os elementos
        values = []

        # Armazena cada elemento na lista de valores
        for element in elements:
            values.append(element.get_attribute("outerHTML"))

        # Retorna a lista de valores concatenada em uma única string
        return '\n'.join(values)

    # Fecha o navegador
    def close_driver(self):
        self.driver.quit()