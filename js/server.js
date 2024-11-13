import express from 'express';
import fetch from 'node-fetch';
import fs from 'fs-extra';
import { parse } from 'node-html-parser';
import path from 'path';
import { fileURLToPath } from 'url';
import cors from 'cors';

// Habilita acesso do domínio ao backend
app.use(cors({ origin: 'https://marlonprado.com.br'}));

// Define porta do express
const app = express();
const port = 3000;

// Obter o diretório atual do arquivo usando `import.meta.url`
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

app.use(express.json());
app.use(express.static(__dirname)); 

// Função para fazer o download de cada capítulo e salvar como arquivos de texto
const downloadCapitulo = async (urlBase, numeroCapitulo) => {
  const capStr = numeroCapitulo.toString().includes(".5")
    ? numeroCapitulo.toString().replace(".5", "-")
    : numeroCapitulo.toString().replace(".0", "");

  const urlCompleta = `${urlBase}${capStr}`;
  const status = [];
  const filePaths = [];

  try {
    const response = await fetch(urlCompleta);
    if (!response.ok) throw new Error(`Erro HTTP: ${response.status}`);

    const html = await response.text();
    const root = parse(html);

    const tituloCapituloElement = root.querySelector("h1.entry-title");
    if (!tituloCapituloElement) {
      status.push(`Título do capítulo não encontrado: ${urlCompleta}`);
      return { status, filePaths };
    }

    const tituloCapitulo = tituloCapituloElement.text;
    const tituloNomeElement = root.querySelector("div.cat-series");
    if (!tituloNomeElement) {
      status.push(`Nome do capítulo não encontrado: ${urlCompleta}`);
      return { status, filePaths };
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

        const caminhoCompleto = path.join(__dirname, req.body.caminho, `${capituloNome} - ${tituloNome}.txt`);

        const dirPath = path.dirname(caminhoCompleto);
        await fs.ensureDir(dirPath);  // Garante que o diretório exista
        await fs.outputFile(caminhoCompleto, `${tituloCapitulo}\n${tituloNome}\n\n${content}`);


        status.push(`Baixado: ${capituloNome} - ${tituloNome}`);
        filePaths.push(caminhoCompleto);
      }
    } else {
      status.push(`#####ERRO##### ${tituloCapitulo}`);
    }
  } catch (error) {
    console.error(`Erro ao baixar o capítulo ${numeroCapitulo}:`, error);
    status.push(`Não localizado: ${capStr}, Erro: ${error.message}`);
  }

  return { status, filePaths };
};

// Endpoint para processar os downloads
app.post("/baixar-capitulos", async (req, res) => {
  const { urlBase, capituloInicial, capituloFinal } = req.body;
  let capAtual = capituloInicial;
  const status = [];
  const filePaths = [];

  res.setHeader('Content-Type', 'text/plain');
  
  // Baixa cada capítulo e gera os arquivos de texto
  while (capAtual <= capituloFinal) {
    const { status: chapterStatus, filePaths: chapterFilePaths } = await downloadCapitulo(urlBase, capAtual);
    chapterStatus.forEach(s => res.write(s + '\n')); // Envia cada status progressivamente
    filePaths.push(...chapterFilePaths);
    capAtual++;
  }

  res.write('Todos os capítulos foram baixados com sucesso!\n');
  
  // Limpeza dos arquivos após o envio
  filePaths.forEach(filePath => fs.removeSync(filePath));
});

app.listen(port, () => {
  console.log(`Servidor rodando na porta ${port}`);
});
