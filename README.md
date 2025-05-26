[![python](https://img.shields.io/badge/Python-3.10.2-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://www.gnu.org/licenses/mit)

# Projeto Light Novel Downloader

Este repositório contém múltiplas soluções para baixar, organizar e unificar capítulos de light novels, incluindo versões desktop, web e scripts locais.

## Índice
- [Projeto Light Novel Downloader](#projeto-light-novel-downloader)
  - [Índice](#índice)
  - [Visão Geral](#visão-geral)
  - [Estrutura do Projeto](#estrutura-do-projeto)
  - [electron-version (App Desktop)](#electron-version-app-desktop)
  - [web-version (App Web)](#web-version-app-web)
  - [local-version (Scripts Locais)](#local-version-scripts-locais)
  - [Licença](#licença)

---

## Visão Geral

Este projeto visa facilitar o download em lote, organização e unificação de capítulos de light novels, especialmente do site Central Novel. São oferecidas três abordagens:
- **electron-version**: Aplicativo desktop moderno, multiplataforma, com interface gráfica.
- **web-version**: Aplicação web simples, fácil de rodar em qualquer máquina com Python.
- **local-version**: Scripts para automação, unificação e manipulação de capítulos.

## Estrutura do Projeto

```
PROJETO_python_web_scrapping_light_novels/
├── electron-version/   # App desktop (Node.js/Electron)
├── web-version/        # App web (Flask/Python)
├── local-version/      # Scripts locais (Python)
├── README.md           # Este arquivo
├── README_PROJETO.md   # Documentação detalhada
└── ...
```

## electron-version (App Desktop)
- Baixe capítulos em lote com barra de progresso
- Gera arquivos .zip com capítulos .txt
- Interface amigável (Electron)
- Futuro: unificação de capítulos direto no app

**Como rodar:**
1. Instale Node.js
2. `npm install`
3. `npm start` para rodar, `npm run build` para gerar instalador

## web-version (App Web)
- Baixe capítulos em lote via navegador
- Gera .zip com capítulos .txt
- Interface web simples

**Como rodar:**
1. Instale Python 3.10+
2. `pip install -r requirements.txt`
3. `python app.py`

## local-version (Scripts Locais)
- Scripts para baixar, unificar e converter capítulos
- Exemplo: unir vários .txt em um só, ou converter para .epub

**Como rodar:**
1. Instale Python 3.10+
2. Execute os scripts desejados, ex: `python unifier_txt_to_txt.py`

## Licença
MIT

---

> Para dúvidas, sugestões ou contribuições, abra uma issue ou envie um e-mail para marlonprado04@gmail.com
