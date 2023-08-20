# Web Scrapping da Light Novel "The Beginning After The End" (TBATE)

Este repositório contém os arquivos relacionados ao projeto de Web Scrapping da light novel "The Beginning After The End" (TBATE).

## Índice

- [Sobre o Projeto](#sobre-o-projeto)
  - [Visão Geral](#visão-geral)
  - [Tecnologias Utilizadas](#tecnologias-utilizadas)
  - [Fontes de Dados](#fontes-de-dados)
  - [Estrutura de Capítulos e Volumes](#estrutura-de-capítulos-e-volumes)
- [Próximas Etapas](#próximas-etapas)
- [Instruções de Execução](#instruções-de-execução)


## Sobre o Projeto

### Visão Geral

Este projeto, implementado em **Python**, visa realizar Web Scraping da light novel "The Beginning After The End". O código pode ser executado no **VSCode** com extensões para trabalhar com arquivos `.ipynb`, no **Google Colaboratory** ou no **Jupyter Notebook**. Também há uma versão alternativa em `.py` que é executável em qualquer máquina com **Python** instalado.

### Tecnologias Utilizadas

As principais tecnologias utilizadas neste projeto incluem:

- **Python 3.10.2**
- **Beautiful Soup 4.12.2** para o parsing HTML
- **Requests 2.31.0** para fazer requisições web

### Fontes de Dados

Inicialmente, o site usado para o scraping foi o [Reaper Scans](https://reaperscans.net/series/o-comeco-apos-o-fim-novel). No entanto, devido a alterações no layout, o [Central Novel](https://centralnovel.com/series/the-beginning-after-the-end/) foi escolhido pela sua estabilidade e melhor estruturação dos dados.

### Estrutura de Capítulos e Volumes

A estrutura dos capítulos e volumes da obra pode ser encontrada no [site](https://tbate.fandom.com/wiki/Volumes_and_Chapters) e no site [Central Novel](https://centralnovel.com/series/the-beginning-after-the-end/), seguindo a ordem original da obra.

- Volume 1: Capítulos 1 ao 21, Capítulo 14.5
- Volume 2: Capítulos 22 ao 42
- Volume 3: Capítulos 43 ao 68
- ...

## Próximas Etapas

- [x] Adicionar quebra de linha nos parágrafos
- [x] Adaptar nome dos arquivos para ordenação "009, 099, 999"
- [x] Criar arquivo alternativo no formato .py para facilitar edição e execução
- [x] Refatorar código para aceitar caminho de download informado pelo usuário
- [x] Refatorar código para baixar capítulos intermediários (ex: 14-5, 221-5)

## Instruções de Execução

Para executar o código, siga as instruções abaixo:

1. Garanta que você possui o Python 3 instalado e as bibliotecas `requests` e `BeautifulSoup` na versão adequada.
2. Execute o código Python e forneça as informações necessárias:
   - Capítulo inicial para download
   - Capítulo final para download
   - Caminho para salvar o arquivo (exemplo: `./` para diretório atual)
   
Alternativamente, você pode usar o Jupyter Notebook ou o Google Colab para importar o código `.ipynb` e executá-lo lá.

No caso de dúvidas ou sugestão o repositório está livre para abertura de issues ou se preferir entre em contato comigo através do meu email: marlonprado04@gmail.com