import os

# Solicita o caminho da pasta
pasta = input("Digite o caminho da pasta: ")
nome_arquivo = input("Digite o nome do arquivo unificado: ")

# Verifica se o caminho é válido
if not os.path.isdir(pasta):
    print("Caminho inválido.")
else:
    # Lista os arquivos .txt na pasta
    arquivos_txt = [
        arquivo for arquivo in os.listdir(pasta) if arquivo.endswith(".txt")
    ]

    # Verifica se há arquivos .txt na pasta
    if not arquivos_txt:
        print("Não foram encontrados arquivos .txt na pasta.")
    else:
        # Nome do arquivo de saída
        arquivo_saida = f"{nome_arquivo}.txt"

        # Abre o arquivo de saída em modo de escrita
        with open(arquivo_saida, "w") as saida:
            for arquivo_txt in arquivos_txt:
                # Abre cada arquivo .txt da pasta em modo de leitura
                with open(os.path.join(pasta, arquivo_txt), "r") as arquivo:
                    # Lê o conteúdo do arquivo e escreve no arquivo de saída
                    conteudo = arquivo.read()
                    saida.write(conteudo)
                # Adiciona uma quebra de linha entre os arquivos
                saida.write("\n")

        print(f"Arquivos unificados com sucesso em '{arquivo_saida}'.")
