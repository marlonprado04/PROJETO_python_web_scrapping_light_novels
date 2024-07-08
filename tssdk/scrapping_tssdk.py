# Links e informações necessárias:

# Site raiz de onde será feita a extração: https://sites.google.com/view/tssdklscanptbr/

# Estrutura do site para cada volume: https://sites.google.com/view/tssdklscanptbr/volume-1

# Classes de cada tag utilizadas para o scrapping:

# Imagens: `<img class="CENy8b">`<br>
# Títulos: h2 <br>
# Parágrafos de texto: p.CDt4Ke zfr3Q <br>
# Div do capítulo completo (até próxima imagem): jXK9ad-SmKAyb


# Importando bibliotecas necessarias
from bs4 import BeautifulSoup
import requests

# Criando url e parseando ela com o BeautifulSoup
url_completa = "https://sites.google.com/view/tssdklscanptbr/volume-1"
page = requests.get(url_completa)
soup = BeautifulSoup(page.content, "html.parser")


# Criando loop para acessar cada section individualmente
for section in soup.findAll("section"):  
    
    # Criando laço para extrair titulos
    for titulo in section.findAll("h2"):
        titulo = titulo.get_text())   
        print(titulo)
    
    # Criando laço para extrair paragrafos
    for paragrafo in section.findAll("p"):
        paragrafo = paragrafo.get_text()
        print(paragrafo)
        
    # Criando arquivo teste.txt e adicionando titulo e paragrafo
    with open("./teste.txt", "a") as arquivo:
        arquivo.write(f"{titulo}\n")
        arquivo.write(f"{paragrafo}\n")

    