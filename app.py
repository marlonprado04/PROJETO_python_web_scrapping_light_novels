from flask import Flask, render_template, request, jsonify
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/download', methods=['POST'])
def download():
    try:
        data = request.get_json()
        url = data['url']
        capitulo_inicial = int(data['capituloInicial'])
        capitulo_final = int(data['capituloFinal'])
        caminho = './capitulos/'  # Definindo um caminho fixo para os arquivos, pode ser ajustado

        resultados = []

        while capitulo_inicial <= capitulo_final:
            cap_inicial = str(capitulo_inicial).replace(".5", "-") if ".5" in str(capitulo_inicial) else str(capitulo_inicial).replace(".0", "")
            url_completa = f"{url}{cap_inicial}"
            resultados.append(f"Tentando baixar: {cap_inicial}")

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
                        titulo_nome = titulo_nome_element.get_text().replace("/", "_").replace("?", "")
                        indice = titulo_capitulo.find("Capítulo")

                        if indice != -1:
                            capitulo = titulo_capitulo[indice:].replace("/", "_")
                            numero_capitulo = capitulo.replace("Capítulo", "").strip()
                            capitulo = f"Capítulo {numero_capitulo.zfill(3)}"

                            with open(f"{caminho}{capitulo} - {titulo_nome}.txt", "w", encoding="utf-8") as arquivo:
                                arquivo.write(titulo_capitulo + "\n" + titulo_nome + "\n\n")
                                content_html = soup.find("div", {"class": "epcontent entry-content"})
                                for paragrafo in content_html.find_all("p"):
                                    arquivo.write(paragrafo.get_text() + "\n\n")
                            
                            resultados.append(f"Baixado: {capitulo} - {titulo_nome}")
                        else:
                            resultados.append(f"#####ERRO##### {titulo_capitulo}")
                    else:
                        resultados.append(f"Nome do capítulo não encontrado: {url_completa}")
                else:
                    resultados.append(f"Título do capítulo não encontrado: {url_completa}")

            except requests.exceptions.HTTPError as err:
                resultados.append(f"Não localizado: {cap_inicial}, Erro: {err}")

            capitulo_inicial += 1

        return jsonify(resultados=resultados)

    except Exception as e:
        # Retorna uma resposta JSON de erro em caso de exceção
        return jsonify(resultados=[f"Erro no servidor: {e}"]), 500

if __name__ == '__main__':
    app.run(debug=True)
