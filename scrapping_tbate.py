# Importando bibliotecas necessárias
from bs4 import BeautifulSoup
import requests

# Criadno URL do site
url = "https://centralnovel.com/the-beginning-after-the-end-capitulo-"

# Criando variáveis para receber range de capítulos para download
capitulo_inicial = int(input("Desde qual capítulo deseja fazer download?"))
capitulo_final = int(input("Até qual capítulo deseja fazer download?"))

# Criando laço de repetição
while capitulo_inicial <= capitulo_final:
    # Passando url completa com o número do cap
    url_completa = url + str(capitulo_inicial)

    # Passando a URL para uma requisição do requests
    requisicao = requests.get(url_completa)

    # Passando o HTML da requisição para uma variável
    html = requisicao.text

    # Parseando o HTML da requisição
    soup = BeautifulSoup(html, "html.parser")

    # Passando o título com número do capítulo para uma variável
    titulo_numero = soup.find("h1", {"class": "entry-title"}).get_text()

    # Passando o nome do capitulo para uma variavel
    titulo_nome = soup.find("div", {"class": "cat-series"}).get_text()
    # Subtituindo / no nome do capítulo para não dar conflito de diretório
    titulo_nome = titulo_nome.replace("/", "_")

    # Criando variável para recortar apenas o capítulo
    indice = titulo_numero.find("Capítulo")

    # Realizando operação para recortar titulo no formato "Capítulo x"
    if indice != -1:
        capitulo = titulo_numero[indice:]
        capitulo = capitulo.replace("/", "_")
    else:
        capitulo = f"#####ERRO##### {titulo_numero}"
        capitulo = capitulo.replace("/", "_")

    # Criando arquivo com número do capítulo e nome
    with open(f"./capitulos/{capitulo} - {titulo_nome}.txt", "w") as arquivo:
        arquivo.write(titulo_numero)
        arquivo.write("\n")
        arquivo.write(titulo_nome)
        arquivo.write("\n\n")

    # Criando loop para armazenar cada parágrafo dentro do arquivo criado
    for paragrafo in soup.find_all("p"):
        with open(f"./capitulos/{capitulo} - {titulo_nome}.txt", "a") as arquivo:
            arquivo.write(paragrafo.get_text())
            arquivo.write("\n\n")

    # Incrementando capitulo
    capitulo_inicial += 1
