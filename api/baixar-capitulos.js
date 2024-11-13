import { parse } from 'node-html-parser';

async function downloadCapitulo(urlBase, numeroCapitulo) {
    const capStr = numeroCapitulo.toString().includes(".5")
        ? numeroCapitulo.toString().replace(".5", "-")
        : numeroCapitulo.toString().replace(".0", "");

    const urlCompleta = `${urlBase}${capStr}`;
    const status = [];
    let content = "";

    try {
        const fetch = (await import('node-fetch')).default;

        const response = await fetch(urlCompleta);
        if (!response.ok) throw new Error(`Erro HTTP: ${response.status}`);

        const html = await response.text();
        const root = parse(html);

        const tituloCapituloElement = root.querySelector("h1.entry-title");
        const tituloNomeElement = root.querySelector("div.cat-series");

        if (!tituloCapituloElement || !tituloNomeElement) {
            throw new Error("Título ou nome do capítulo não encontrado");
        }

        const tituloCapitulo = tituloCapituloElement.text;
        const tituloNome = tituloNomeElement.text.replace("/", "_").replace("?", "");
        const contentHtml = root.querySelector("div.epcontent.entry-content");

        if (contentHtml) {
            content = Array.from(contentHtml.querySelectorAll("p"))
                .map((p) => p.text)
                .join("\n\n");
        }

        status.push(`Baixado: ${tituloCapitulo} - ${tituloNome}`);
        return { status, content: `${tituloCapitulo}\n${tituloNome}\n\n${content}` };
    } catch (error) {
        console.error(`Erro ao baixar o capítulo ${numeroCapitulo}:`, error);
        status.push(`Não localizado: ${capStr}, Erro: ${error.message}`);
        return { status, content: null };
    }
}

export default async function handler(req, res) {
    // Verifica se a requisição é POST
    if (req.method === "POST") {
        const { urlBase, capituloInicial, capituloFinal } = req.body;
        let capAtual = capituloInicial;
        const status = [];
        const capitulos = [];

        // Baixa os capítulos
        while (capAtual <= capituloFinal) {
            const { status: chapterStatus, content } = await downloadCapitulo(urlBase, capAtual);
            status.push(...chapterStatus);
            if (content) {
                capitulos.push({ capitulo: capAtual, content });
            }
            capAtual++;
        }

        res.status(200).json({ status, capitulos });
    } else {
        // Responde com erro para outros métodos HTTP
        res.status(405).json({ message: 'Método não permitido' });
    }
}
