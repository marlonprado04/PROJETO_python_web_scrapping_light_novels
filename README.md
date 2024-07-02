[![python](https://img.shields.io/badge/Python-3.10.2-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://www.gnu.org/licenses/mit)

# Web Scrapping da Light Novel "The Beginning After The End" (TBATE)

Este repositório contém os arquivos relacionados ao projeto de Web Scrapping da light novel The Beginning After The End (TBATE).

## Índice

- [Web Scrapping da Light Novel "The Beginning After The End" (TBATE)](#web-scrapping-da-light-novel-the-beginning-after-the-end-tbate)
  - [Índice](#índice)
  - [Sobre o Projeto](#sobre-o-projeto)
    - [Visão Geral](#visão-geral)
    - [Tecnologias Utilizadas](#tecnologias-utilizadas)
    - [Fontes de Dados](#fontes-de-dados)
    - [Estrutura de Capítulos e Volumes](#estrutura-de-capítulos-e-volumes)
  - [Próximas etapas do projeto](#próximas-etapas-do-projeto)
  - [Instruções de Execução](#instruções-de-execução)

## Sobre o Projeto

### Visão Geral

Este projeto, implementado em **Python**, visa realizar Web Scraping da light novel "The Beginning After The End".

Para executar o projeto basta rodar o arquivo `scrapping.py` que é executável em qualquer máquina com **Python 3** instalado.

### Tecnologias Utilizadas

As principais tecnologias utilizadas neste projeto são:

- **Python 3.10.2**
- **Beautiful Soup 4.12.2** para o parsing HTML
- **Requests 2.31.0** para fazer requisições web

### Fontes de Dados

Inicialmente, o site usado para o scrapping foi o [Reaper Scans](https://reaperscans.net/series/o-comeco-apos-o-fim-novel). No entanto, devido a alterações no layout, o [Central Novel](https://centralnovel.com/series/the-beginning-after-the-end/) foi escolhido pela sua estabilidade e melhor estruturação dos dados.

### Estrutura de Capítulos e Volumes

A estrutura dos capítulos e volumes da obra pode ser encontrada  [neste site](https://tbate.fandom.com/wiki/Volumes_and_Chapters) e no próprio site da [Central Novel](https://centralnovel.com/series/the-beginning-after-the-end/), que visa seguir a ordem original da obra.

Abaixo a lista de capítulos e volumes:

- Volume 1: 1 ao 21 (20 caps)
  - 14.5
- Volume 2: 22 ao 42 (20 caps)
- Volume 3: 43 ao 68 (25 caps)
- Volume 4: 69 ao 97 (28 caps)
- Volume 5: 98 ao 138 (30 caps)
- Volume 6: 139 ao 194 (55 caps)
- Volume 7: 195 ao 249 (54 caps)
  - 221.5, 223.5, 230.5, 233.5
- Volume 8: 250 ao 313 (63 caps)
- Volume 8.5 (extra): 1 ao 20 (20 caps)
- Volume 9: 314 ao 381 (67 caps)
  - 374.5
- Volume 10: 382 ao 429 (47 caps)
- Volume 11: 430 em 482 (52 caps)
- Volume 12: aguardando

## Próximas etapas do projeto

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

Alternativamente, você pode usar o Jupyter Notebook ou o Google Colab para copiar o código `.py` e executá-lo lá. 

No caso de dúvidas ou sugestão o repositório está livre para abertura de issues ou se preferir entre em contato comigo através do meu email: <marlonprado04@gmail.com>
