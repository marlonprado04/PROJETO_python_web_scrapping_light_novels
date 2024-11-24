# Importando bibliotecas necessárias
from bs4 import BeautifulSoup
import requests
import re

# Função para substituir ponto por traço no nome
def substituir_ponto_por_traco(valor):
    return re.sub(r"\.(\d+)", r"-\1", str(valor))

# Criando variável para URL do site
url = "https://centralnovel.com/the-beginning-after-the-end-capitulo-"

# Função para limpar o nome do arquivo
def limpar_nome_arquivo(nome):
    return nome.replace("/", "_").replace("?", "").replace("\n", " ").replace(":", " -").strip()

# Função para verificar se o capítulo existe
def verificar_existencia_url(url_completa):
    try:
        resposta = requests.head(url_completa, allow_redirects=True)
        return resposta.status_code == 200  # Retorna True se a página existe
    except requests.exceptions.RequestException:
        return False  # Em caso de erro, considera que a página não existe

# Função principal para baixar capítulos
def baixar_capitulos(capitulo_inicial, capitulo_final, caminho):
    for capitulo in range(capitulo_inicial, capitulo_final + 1):
        # Verifica se o capítulo principal existe
        cap_inicial = f"{capitulo}"
        cap_inicial = substituir_ponto_por_traco(cap_inicial)
        url_completa = f"{url}{cap_inicial}"

        if verificar_existencia_url(url_completa):
            print(f"Tentando baixar: {cap_inicial}")

            try:
                # Fazendo scraping da página
                requisicao = requests.get(url_completa)
                requisicao.raise_for_status()
                html = requisicao.text
                soup = BeautifulSoup(html, "html.parser")

                # Encontrando título do capítulo
                titulo_capitulo_element = soup.find("h1", {"class": "entry-title"})
                if titulo_capitulo_element:
                    titulo_capitulo = titulo_capitulo_element.get_text()
                    titulo_nome_element = soup.find("div", {"class": "cat-series"})
                    if titulo_nome_element:
                        titulo_nome = limpar_nome_arquivo(titulo_nome_element.get_text())

                        numero_capitulo = str(capitulo).zfill(5)  # Formatação correta
                        capitulo_nome = limpar_nome_arquivo(f"Capítulo {numero_capitulo}")

                        # Salvando o conteúdo em arquivo
                        with open(
                            f"{caminho}{capitulo_nome} - {titulo_nome}.txt",
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

                        print(f"Baixado: {capitulo_nome} - {titulo_nome}")
                    else:
                        print(f"Nome do capítulo não encontrado: {url_completa}")
                else:
                    print(f"Título do capítulo não encontrado: {url_completa}")

            except requests.exceptions.HTTPError as err:
                print(f"Não localizado: {cap_inicial}, Erro: {err}")
        
        # Agora verificar os subcapítulos consecutivos
        subcapitulo = 2
        while True:  # Loop para verificar os subcapítulos consecutivos
            cap_inicial = f"{capitulo}-{subcapitulo}"
            cap_inicial = substituir_ponto_por_traco(cap_inicial)
            url_completa = f"{url}{cap_inicial}"

            if verificar_existencia_url(url_completa):
                print(f"Tentando baixar: {cap_inicial}")

                try:
                    # Fazendo scraping da página
                    requisicao = requests.get(url_completa)
                    requisicao.raise_for_status()
                    html = requisicao.text
                    soup = BeautifulSoup(html, "html.parser")

                    # Encontrando título do capítulo
                    titulo_capitulo_element = soup.find("h1", {"class": "entry-title"})
                    if titulo_capitulo_element:
                        titulo_capitulo = titulo_capitulo_element.get_text()
                        titulo_nome_element = soup.find("div", {"class": "cat-series"})
                        if titulo_nome_element:
                            titulo_nome = limpar_nome_arquivo(titulo_nome_element.get_text())

                            numero_capitulo = str(capitulo).zfill(5)
                            numero_subcapitulo = str(subcapitulo).zfill(2)  # Formatação correta
                            capitulo_nome = limpar_nome_arquivo(f"Capítulo {numero_capitulo}-{numero_subcapitulo}")

                            # Salvando o conteúdo em arquivo
                            with open(
                                f"{caminho}{capitulo_nome} - {titulo_nome}.txt",
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

                            print(f"Baixado: {capitulo_nome} - {titulo_nome}")
                        else:
                            print(f"Nome do capítulo não encontrado: {url_completa}")
                    else:
                        print(f"Título do capítulo não encontrado: {url_completa}")

                except requests.exceptions.HTTPError as err:
                    print(f"Não localizado: {cap_inicial}, Erro: {err}")
                
                # Avança para o próximo subcapítulo
                subcapitulo += 1
            else:
                print(f"Subcapítulo {cap_inicial} não encontrado, pulando...")
                break  # Se o subcapítulo não existir, sai do loop de subcapítulos para esse capítulo

# Exemplo de uso
capitulo_inicial = int(input("Desde qual capítulo deseja fazer download? "))
capitulo_final = int(input("Até qual capítulo deseja fazer download? "))
caminho = input("Digite o caminho onde deseja salvar os arquivos (ex: ./, /, ./capitulos/): ")

# Chamando a função para baixar os capítulos
baixar_capitulos(capitulo_inicial, capitulo_final, caminho)