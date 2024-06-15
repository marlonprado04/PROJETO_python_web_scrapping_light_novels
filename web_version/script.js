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

                const handle = await getDirectoryHandle(); // Obtém o handle do diretório
                if (handle) {
                    const fileHandle = await handle.getFileHandle(fileName, { create: true }); // Cria o handle do arquivo
                    const writable = await fileHandle.createWritable(); // Cria um writable stream
                    await writable.write(fileContent); // Escreve o conteúdo no arquivo
                    await writable.close(); // Fecha o writable stream

                    output.textContent += `Capítulo ${chapter} baixado com sucesso.\n`; // Exibe uma mensagem de sucesso
                } else {
                    output.textContent += `Erro ao acessar o caminho: ${path}\n`; // Exibe uma mensagem de erro se não conseguir acessar o caminho
                }
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
            currentChapter += 0.5; // Incrementa o capítulo atual
        }
        output.textContent += 'Downloads concluídos.'; // Exibe uma mensagem quando todos os downloads forem concluídos
    };

    downloadLoop(); // Inicia o loop de download
});

// Adiciona um listener de evento ao botão "Selecionar Pasta" para permitir ao usuário selecionar uma pasta
document.getElementById('selectFolderButton').addEventListener('click', async () => {
    try {
        const handle = await window.showDirectoryPicker(); // Abre o seletor de diretório
        document.getElementById('path').value = handle.name; // Define o valor do campo de caminho com o nome do diretório
        window.selectedDirectoryHandle = handle; // Armazena o handle do diretório na janela global
    } catch (err) {
        console.error('Erro ao selecionar a pasta:', err); // Exibe uma mensagem de erro se ocorrer um erro ao selecionar a pasta
    }
});

// Função para obter o handle do diretório selecionado
async function getDirectoryHandle() {
    return window.selectedDirectoryHandle || null; // Retorna o handle do diretório ou null se não houver nenhum selecionado
}
