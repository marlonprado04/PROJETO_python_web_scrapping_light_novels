import fetch from 'node-fetch';
import fs from 'fs-extra';
import { parse } from 'node-html-parser';
import path from 'path';
import cors from 'cors';

// Configurações de CORS para permitir requisições do seu domínio
const corsOptions = {
    origin: 'https://projetos.marlonprado.com.br',
    methods: ['POST']
};

// Função de middleware para lidar com o CORS em uma função serverless
function runMiddleware(req, res, fn) {
    return new Promise((resolve, reject) => {
        fn(req, res, (result) => {
            if (result instanceof Error) {
                return reject(result);
            }
            return resolve(result);
        });
    });
}

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

                const caminhoCompleto = path.join('/tmp', `${capituloNome} - ${tituloNome}.txt`);

                // Garante que o diretório exista e salva o arquivo temporariamente
                await fs.ensureDir(path.dirname(caminhoCompleto));
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

// Função handler para o endpoint serverless no Vercel
export default async function handler(req, res) {
    await runMiddleware(req, res, cors(corsOptions));

    if (req.method === "POST") {
        const { urlBase, capituloInicial, capituloFinal } = req.body;
        let capAtual = capituloInicial;
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
        res.end();

        // Limpeza dos arquivos temporários
        filePaths.forEach(filePath => fs.removeSync(filePath));
    } else {
        res.status(405).json({ message: 'Método não permitido' });
    }
}