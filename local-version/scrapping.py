# Importando bibliotecas necessárias
from bs4 import BeautifulSoup
import requests

# Criando variável para URL do site
#url = "https://centralnovel.com/the-beginning-after-the-end-capitulo-"

# URL para outra novel
# Pode ser alterado para qualquer novel do site desde que respeite a estrutura padrão
# url = "https://centralnovel.com/trash-of-the-counts-family-capitulo-"

url = "https://centralnovel.com/shadow-slave-capitulo-"

# Criando variáveis para receber range de capítulos para download
capitulo_inicial = float(input("Desde qual capítulo deseja fazer download? "))
capitulo_final = float(input("Até qual capítulo deseja fazer download? "))
caminho = input(
    "Digite o caminho onde deseja salvar os arquivos (ex: ./, /, ./capitulos/): "
)

def limpar_nome_arquivo(nome):
    # Substitui caracteres indesejados por um espaço ou nada
    return nome.replace("/", "_").replace("?", "").replace("\n", " ").replace(":", " -").strip()


# Criando laço de repetição para executar o código em loop
while capitulo_inicial <= capitulo_final:
        cap_inicial = (
            str(capitulo_inicial).replace(".5", "-")
            if ".5" in str(capitulo_inicial)
            else str(capitulo_inicial).replace(".0", "")
        )
        url_completa = f"{url}{cap_inicial}"
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


                        with open(
                            f"{caminho}{capitulo} - {titulo_nome}.txt",
                            "w",
                            encoding="utf-8",
                        ) as arquivo:
                            arquivo.write(
                                titulo_capitulo + "\n" + titulo_nome + "\n\n"
                            )
                            content_html = soup.find(
                                "div", {"class": "epcontent entry-content"}
                            )
                            for paragrafo in content_html.find_all("p"):
                                arquivo.write(paragrafo.get_text() + "\n\n")

                        print(f"Baixado: {capitulo} - {titulo_nome}")
                    else:
                        print(f"#####ERRO##### {titulo_capitulo}")
                else:
                    print(
                        f"Nome do capítulo não encontrado: {url_completa}"
                    )
            else:
                print(
                    f"Título do capítulo não encontrado: {url_completa}"
                )

        except requests.exceptions.HTTPError as err:
            print(f"Não localizado: {cap_inicial}, Erro: {err}")

        capitulo_inicial += 1
