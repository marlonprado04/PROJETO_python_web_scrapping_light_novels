# Importando bibliotecas necessárias
from bs4 import BeautifulSoup
import requests

# Criadno URL do site
url = "https://centralnovel.com/the-beginning-after-the-end-capitulo-"

# Criando variáveis para receber range de capítulos para download
capitulo_inicial = int(input("Desde qual capítulo deseja fazer download?"))
capitulo_final = int(input("Até qual capítulo deseja fazer download?"))
caminho = input("Digite o caminho onde deseja salvar os arquivos (ex: ./, /, ./capitulos/): ")

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
    titulo_capitulo = soup.find("h1", {"class": "entry-title"}).get_text()

    # Passando o nome do capitulo para uma variavel
    titulo_nome = soup.find("div", {"class": "cat-series"}).get_text()
    # Subtituindo / no nome do capítulo para não dar conflito de diretório
    titulo_nome = titulo_nome.replace("/", "_")

    # Criando variável para recortar apenas o capítulo
    indice = titulo_capitulo.find("Capítulo")

    # Realizando operação para tratar o titulo "Capítulo x"
    if indice != -1:
        # Obtendo texto "Capítulo x"
        capitulo = titulo_capitulo[indice:]
        capitulo = capitulo.replace("/", "_")

        # Obtendo apenas o número do capítulo
        numero_capitulo = capitulo.split(" ")[1]

        # Formatando o número do capítulo com três dígitos
        capitulo = f"Capítulo {numero_capitulo.zfill(3)}"
    else:
        ## Armazenando mensagem de erro caso capítulo não tenha sido informado
        capitulo = f"#####ERRO##### {titulo_capitulo}"
        capitulo = capitulo.replace("/", "_")

    # Criando arquivo com número do capítulo e nome
    with open(f"{caminho}{capitulo} - {titulo_nome}.txt", "w") as arquivo:
        arquivo.write(titulo_capitulo)
        arquivo.write("\n")
        arquivo.write(titulo_nome)
        arquivo.write("\n\n")

    # Criando loop para armazenar cada parágrafo dentro do arquivo criado
    for paragrafo in soup.find_all("p"):
        with open(f"{caminho}{capitulo} - {titulo_nome}.txt", "a") as arquivo:
            arquivo.write(paragrafo.get_text())
            arquivo.write("\n\n")

    # Incrementando capitulo
    capitulo_inicial += 1