# Projeto Light Novel Downloader

Este repositório contém três versões do projeto para baixar e organizar capítulos de light novels:

- **electron-version**: Aplicativo desktop (Electron + Node.js)
- **web-version**: Aplicação web (Flask/Python)
- **local-version**: Scripts locais para automação e unificação de capítulos

---

## electron-version (App Desktop)

Aplicativo desktop multiplataforma para baixar capítulos de novels diretamente do site Central Novel, com interface moderna e recursos de download em lote.

### Principais recursos
- Download de capítulos em lote (com barra de progresso)
- Geração automática de arquivos .zip com capítulos .txt
- Interface amigável (Electron)
- Unificação dos capítulos (em breve)

### Como rodar
1. Instale o Node.js (https://nodejs.org)
2. Instale as dependências:
   ```sh
   npm install
   ```
3. Rode o app:
   ```sh
   npm start
   ```
4. Para gerar o instalador (.exe):
   ```sh
   npm run build
   ```

---

## web-version (App Web)

Aplicação web simples para baixar capítulos via navegador, feita em Python (Flask).

### Principais recursos
- Download de capítulos em lote
- Geração de .zip com capítulos .txt
- Interface web simples

### Como rodar
1. Instale Python 3.10+
2. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```
3. Rode o app:
   ```sh
   python app.py
   ```
4. Acesse via navegador: http://localhost:5000

---

## local-version (Scripts Locais)

Scripts para automação, unificação e manipulação de capítulos baixados.

### Principais scripts
- `scrapping.py`: Baixa capítulos diretamente para o disco
- `unifier_txt_to_txt.py`: Une vários arquivos .txt em um só
- `unifier_txt_to_epub.py`: Converte capítulos .txt em um arquivo .epub

### Como usar
1. Instale Python 3.10+
2. Execute os scripts conforme desejado:
   ```sh
   python scrapping.py
   python unifier_txt_to_txt.py
   python unifier_txt_to_epub.py
   ```

---

## Estrutura do repositório

```
PROJETO_python_web_scrapping_light_novels/
├── electron-version/   # App desktop (Node.js/Electron)
├── web-version/        # App web (Flask/Python)
├── local-version/      # Scripts locais (Python)
└── README.md           # Documentação principal
```

---

## Licença
MIT

---

> Para dúvidas, sugestões ou contribuições, abra uma issue ou envie um e-mail para marlonprado04@gmail.com
