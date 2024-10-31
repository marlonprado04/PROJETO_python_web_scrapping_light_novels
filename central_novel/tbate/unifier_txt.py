import os

# Solicita o caminho da pasta
pasta = input("Digite o caminho da pasta: ").strip()  # Remove possíveis espaços em branco
nome_arquivo = input("Digite o nome do arquivo unificado: ")

# Converte para caminho absoluto para evitar problemas
caminho_absoluto = os.path.abspath(pasta)
print(f"Caminho absoluto da pasta: {caminho_absoluto}")

# Verifica se o caminho é válido
if not os.path.isdir(caminho_absoluto):
    print("Caminho inválido.")
else:
    # Lista e imprime todos os arquivos no diretório para depuração
    todos_arquivos = os.listdir(caminho_absoluto)
    print("Arquivos na pasta:", todos_arquivos)
    # Filtra os arquivos .txt na pasta e os ordena
    arquivos_txt = [arquivo for arquivo in todos_arquivos if arquivo.endswith(".txt")]
    print("Arquivos .txt encontrados:", arquivos_txt)  # Verificação extra para depuração
    arquivos_txt.sort()  # Ordena os arquivos

    # Verifica se há arquivos .txt na pasta
    if not arquivos_txt:
        print("Não foram encontrados arquivos .txt na pasta.")
    else:
        # Nome do arquivo de saída
        arquivo_saida = f"{nome_arquivo}.txt"

        # Abre o arquivo de saída em modo de escrita
        with open(arquivo_saida, "w", encoding="utf-8") as saida:
            for arquivo_txt in arquivos_txt:
                # Abre cada arquivo .txt da pasta em modo de leitura
                with open(os.path.join(caminho_absoluto, arquivo_txt), "r", encoding="utf-8", errors="ignore") as arquivo:
                    # Lê o conteúdo do arquivo e escreve no arquivo de saída
                    conteudo = arquivo.read()
                    saida.write(conteudo)
                # Adiciona uma quebra de linha entre os arquivos
                saida.write("\n")
        print(f"Arquivos unificados com sucesso em '{arquivo_saida}'.")
