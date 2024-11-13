from flask import Flask, request, jsonify, render_template
from bs4 import BeautifulSoup
import requests
import os

app = Flask(__name__)

# Função para limpar o nome do arquivo (remover caracteres inválidos)
def limpar_nome_arquivo(nome):
    return nome.replace("/", "_").replace("?", "").replace("\n", " ").replace(":", " -").strip()

@app.route('/download', methods=['POST'])
def download_capitulos():
    data = request.json
    url_base = data.get("url")
    capitulo_inicial = int(data.get("capituloInicial"))
    capitulo_final = int(data.get("capituloFinal"))
    caminho = data.get("caminho", "./")

    if not os.path.exists(caminho):
        os.makedirs(caminho)

    capitulos_baixados = []

    # Laço para baixar capítulos no intervalo especificado
    while capitulo_inicial <= capitulo_final:
        cap_inicial = (
            str(capitulo_inicial).replace(".5", "-")
            if ".5" in str(capitulo_inicial)
            else str(capitulo_inicial).replace(".0", "")
        )
        url_completa = f"{url_base}{cap_inicial}"
        print(f"Tentando baixar: {cap_inicial}")

        try:
            requisicao = requests.get(url_completa)
            requisicao.raise_for_status()
            html = requisicao.text
            soup = BeautifulSoup(html, "html.parser")

            titulo_capitulo_element = soup.find("h1", {"class": "entry-title"})
            if titulo_capitulo_element:
                titulo_capitulo = titulo_capitulo_element.get_text()
                titulo_nome_element = soup.find("div", {"class": "cat-series"})
                if titulo_nome_element:
                    titulo_nome = limpar_nome_arquivo(titulo_nome_element.get_text())

                    indice = titulo_capitulo.find("Capítulo")
                    if indice != -1:
                        capitulo = titulo_capitulo[indice:].replace("/", "_")
                        numero_capitulo = capitulo.replace("Capítulo", "").strip()
                        capitulo = limpar_nome_arquivo(f"Capítulo {numero_capitulo.zfill(5)}")

                        # Salva o capítulo no arquivo
                        with open(f"{caminho}{capitulo} - {titulo_nome}.txt", "w", encoding="utf-8") as arquivo:
                            arquivo.write(titulo_capitulo + "\n" + titulo_nome + "\n\n")
                            content_html = soup.find("div", {"class": "epcontent entry-content"})
                            for paragrafo in content_html.find_all("p"):
                                arquivo.write(paragrafo.get_text() + "\n\n")

                        capitulos_baixados.append(f"{capitulo} - {titulo_nome}")
                        print(f"Baixado: {capitulo} - {titulo_nome}")
                    else:
                        print(f"#####ERRO##### {titulo_capitulo}")
                else:
                    print(f"Nome do capítulo não encontrado: {url_completa}")
            else:
                print(f"Título do capítulo não encontrado: {url_completa}")
        except requests.exceptions.HTTPError as err:
            print(f"Não localizado: {cap_inicial}, Erro: {err}")

        capitulo_inicial += 1

    return jsonify({"status": "success", "capitulos": capitulos_baixados})

@app.route('/')
def index():
    return render_template('index.html')

# Para o Vercel identificar o ponto de entrada
app = app

# Mantém a possibilidade de executar localmente
if __name__ == "__main__":
    app.run(debug=True)
