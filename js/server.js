import express from 'express';
import fetch from 'node-fetch';  // Usando import para o node-fetch
import fs from 'fs-extra';       // Usando import para fs-extra
import { parse } from 'node-html-parser';  // Usando import para node-html-parser
import path from 'path';  // Para manipular caminhos de arquivos
import { fileURLToPath } from 'url';  // Para converter URL para caminho de arquivo

const app = express();
const port = 3000;

// Obter o diretório atual do arquivo usando `import.meta.url`
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Middleware para permitir parsing de JSON no corpo da requisição
app.use(express.json());
app.use(express.static(__dirname)); // Serve arquivos estáticos da pasta atual

// Função para fazer o download de cada capítulo
const downloadCapitulo = async (urlBase, numeroCapitulo, caminho) => {
  const capStr = numeroCapitulo.toString().includes(".5")
    ? numeroCapitulo.toString().replace(".5", "-")
    : numeroCapitulo.toString().replace(".0", "");

  const urlCompleta = `${urlBase}${capStr}`;
  const status = [];

  try {
    const response = await fetch(urlCompleta);
    if (!response.ok) throw new Error(`Erro HTTP: ${response.status}`);

    const html = await response.text();
    const root = parse(html);

    const tituloCapituloElement = root.querySelector("h1.entry-title");
    if (!tituloCapituloElement) {
      status.push(`Título do capítulo não encontrado: ${urlCompleta}`);
      return status;
    }

    const tituloCapitulo = tituloCapituloElement.text;
    const tituloNomeElement = root.querySelector("div.cat-series");
    if (!tituloNomeElement) {
      status.push(`Nome do capítulo não encontrado: ${urlCompleta}`);
      return status;
    }

    const tituloNome = tituloNomeElement.text
      .replace("/", "_")
      .replace("?", "");
    const indice = tituloCapitulo.indexOf("Capítulo");

    if (indice !== -1) {
      const numeroCapitulo = tituloCapitulo
        .slice(indice)
        .replace("Capítulo", "")
        .trim();
      const capituloNome = `Capítulo ${numeroCapitulo.padStart(3, "0")}`;

      const contentHtml = root.querySelector("div.epcontent.entry-content");
      if (contentHtml) {
        const content = Array.from(contentHtml.querySelectorAll("p"))
          .map((p) => p.text)
          .join("\n\n");

        // Cria o caminho completo do arquivo
        const caminhoCompleto = `${caminho}/${capituloNome} - ${tituloNome}.txt`;

        // Cria o arquivo com o conteúdo do capítulo
        await fs.outputFile(
          caminhoCompleto,
          `${tituloCapitulo}\n${tituloNome}\n\n${content}`
        );
        status.push(`Baixado: ${capituloNome} - ${tituloNome}`);
      }
    } else {
      status.push(`#####ERRO##### ${tituloCapitulo}`);
    }
  } catch (error) {
    status.push(`Não localizado: ${capStr}, Erro: ${error.message}`);
  }

  return status;
};

// Endpoint para processar os downloads
app.post("/baixar-capitulos", async (req, res) => {
  const { urlBase, capituloInicial, capituloFinal, caminho } = req.body;
  let capAtual = capituloInicial;
  const status = [];

  while (capAtual <= capituloFinal) {
    const chapterStatus = await downloadCapitulo(urlBase, capAtual, caminho);
    status.push(...chapterStatus);
    capAtual += 1;
  }

  res.json({ status });
});

// Inicia o servidor
app.listen(port, () => {
  console.log(`Servidor rodando na porta ${port}`);
});
