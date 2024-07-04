// Adiciona um listener de evento ao formulário para lidar com o envio do formulário
document.getElementById('downloadForm').addEventListener('submit', function (e) {
    e.preventDefault(); // Evita o envio padrão do formulário

    const url = document.getElementById('url').value; // Obtém a URL da novel
    const startChapter = parseFloat(document.getElementById('startChapter').value); // Obtém o capítulo inicial
    const endChapter = parseFloat(document.getElementById('endChapter').value); // Obtém o capítulo final
    const output = document.getElementById('output'); // Obtém o elemento para saída de mensagens

    output.textContent = "Iniciando downloads...\n"; // Exibe uma mensagem de início

    let currentChapter = startChapter; // Inicializa o capítulo atual com o capítulo inicial

    // Função assíncrona para fazer o download de um capítulo
    const downloadChapter = async (chapter) => {
        let chapterUrl = url; // Inicializa a URL do capítulo
        if (String(chapter).includes('.5')) {
            chapterUrl += String(chapter).replace('.', '-'); // Ajusta a URL para capítulos intermediários
        } else {
            chapterUrl += String(chapter).replace('.0', ''); // Ajusta a URL para capítulos inteiros
        }

        try {
            console.log(`Fetching URL: ${chapterUrl}`); // Log da URL que está sendo buscada

            const response = await fetch(chapterUrl); // Faz a requisição para a URL do capítulo
            if (!response.ok) throw new Error('Capítulo não encontrado'); // Lança um erro se a resposta não for bem-sucedida

            const text = await response.text(); // Obtém o texto da resposta
            const parser = new DOMParser(); // Cria um novo DOMParser
            const doc = parser.parseFromString(text, 'text/html'); // Parsea o HTML da resposta

            const titleElement = doc.querySelector('h1.entry-title'); // Seleciona o título do capítulo
            const nameElement = doc.querySelector('div.cat-series'); // Seleciona o nome da série
            if (titleElement && nameElement) {
                const title = titleElement.textContent; // Obtém o texto do título
                const name = nameElement.textContent.replace(/\//g, '_').replace(/\?/g, ''); // Substitui caracteres inválidos no nome

                const fileName = `${title.replace('Capítulo ', '').replace(/\s/g, '').padStart(3, '0')} - ${name}.txt`; // Cria o nome do arquivo
                const fileContent = [title, name, '', ...Array.from(doc.querySelectorAll('p')).map(p => p.textContent)].join('\n\n'); // Cria o conteúdo do arquivo

                // Cria um Blob com o conteúdo do arquivo e simula um download
                const blob = new Blob([fileContent], { type: 'text/plain' });
                const link = document.createElement('a');
                link.href = URL.createObjectURL(blob);
                link.download = fileName;
                document.body.appendChild(link);
                link.click();
                document.body.removeChild(link);

                output.textContent += `Capítulo ${chapter} baixado com sucesso.\n`; // Exibe uma mensagem de sucesso
            } else {
                output.textContent += `Capítulo ${chapter} não encontrado no site.\n`; // Exibe uma mensagem se o capítulo não for encontrado no site
            }
        } catch (error) {
            output.textContent += `Erro ao baixar capítulo ${chapter}: ${error.message}\n`; // Exibe uma mensagem de erro se ocorrer um erro na requisição
        }
    };

    // Função assíncrona para iterar sobre os capítulos e fazer o download de cada um
    const downloadLoop = async () => {
        while (currentChapter <= endChapter) {
            await downloadChapter(currentChapter); // Faz o download do capítulo atual
            currentChapter += 0.5; // Incrementa o capítulo em 0.5
        }
        output.textContent += "Downloads concluídos.\n"; // Exibe uma mensagem ao concluir todos os downloads
    };

    downloadLoop(); // Inicia o loop de download
});
