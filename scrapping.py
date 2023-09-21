# Importando bibliotecas necessárias
from bs4 import BeautifulSoup
import requests

# Criando variável para URL do site
#url = "https://centralnovel.com/the-beginning-after-the-end-capitulo-"

# URL para outra novel
# Pode ser alterado para qualquer novel do site desde que respeite a estrutura padrão
url = "https://centralnovel.com/trash-of-the-counts-family-capitulo-"

# Criando variáveis para receber range de capítulos para download
capitulo_inicial = float(input("Desde qual capítulo deseja fazer download?"))
capitulo_final = float(input("Até qual capítulo deseja fazer download?"))
caminho = input(
    "Digite o caminho onde deseja salvar os arquivos (ex: ./, /, ./capitulos/): "
)

# Criando laço de repetição para executar o código em loop
while capitulo_inicial <= capitulo_final:
    # Criando if para tratar URL de acordo com capítulo atual
    if ".5" in str(capitulo_inicial):
        # Substituindo . por - no caso de ser um capítulo intermediário
        cap_inicial = str(capitulo_inicial).replace(".", "-")
        # Passando URL completa
        url_completa = f"{url}{cap_inicial}"
        print(f"Capitulo:{cap_inicial}")

    else:
        # Removendo .0 no caso de não ser um capítulo intermediário
        cap_inicial = str(capitulo_inicial).replace(".0", "")
        # Passando URL completa
        url_completa = f"{url}{cap_inicial}"
        print(f"Capitulo:{cap_inicial}")


    # Criando tentativa com a URL passada
    try:
        # Passando a URL para uma requisição do requests
        requisicao = requests.get(url_completa)
        requisicao.raise_for_status()  # Verifica se ocorreu algum erro na requisição

        # Passando o HTML requisitado para uma variável
        html = requisicao.text

        # Parseando o HTML da requisição
        soup = BeautifulSoup(html, "html.parser")

        # Passando o título + número do capítulo para uma variável
        titulo_capitulo_element = soup.find("h1", {"class": "entry-title"})
        if titulo_capitulo_element:
            titulo_capitulo = titulo_capitulo_element.get_text()

            # Passando o nome do capítulo para uma variável
            titulo_nome_element = soup.find("div", {"class": "cat-series"})
            if titulo_nome_element:
                titulo_nome = titulo_nome_element.get_text()
                # Substituindo a / no nome do capítulo para não dar conflito de diretório
                titulo_nome = titulo_nome.replace("/", "_")
                
                # Substituindo o ? no nome do capítulo para não dar conflito no sistema de arquivos
                titulo_nome = titulo_nome.replace("?", "")

                # Criando variável para recortar apenas o capítulo
                indice = titulo_capitulo.find("Capítulo")

                # Realizando operação para tratar o título "Capítulo x"
                if indice != -1:
                    # Obtendo texto "Capítulo x"
                    capitulo = titulo_capitulo[indice:]
                    capitulo = capitulo.replace("/", "_")
                    
                    # Obtendo apenas o número do capítulo extraído do título
                    numero_capitulo = capitulo.replace("Capítulo", "").replace(" ", "").replace("\n", "")

                    # Formatando o número do capítulo com três dígitos
                    capitulo = f"Capítulo {numero_capitulo.zfill(3)}"
                else:
                    ## Armazenando mensagem de erro caso capítulo não tenha sido informado no site
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
                    with open(
                        f"{caminho}{capitulo} - {titulo_nome}.txt", "a"
                    ) as arquivo:
                        arquivo.write(paragrafo.get_text())
                        arquivo.write("\n\n")
            else:
                print(f"Nome do capítulo não encontrado: {url_completa}")
                # Ou pode apenas passar para o próximo capítulo, sem fazer nada
                pass

        else:
            print(f"Título do capítulo não encontrado: {url_completa}")
            # Ou pode apenas passar para o próximo capítulo, sem fazer nada
            pass

    # Tratando exceção no caso da URL não encontrada
    except requests.exceptions.HTTPError as err:
        # Caso ocorra um erro HTTP (por exemplo, 404), a URL não existe
        # Imprimindo mensagem informando que o capítulo não existe
        print(f"Capítulo não encontrado: {cap_inicial}")

        # Passando para o próximo incremento
        pass

    # Incrementando capitulo
    capitulo_inicial += 0.5
