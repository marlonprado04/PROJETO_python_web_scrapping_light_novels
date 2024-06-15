document.getElementById('downloadForm').addEventListener('submit', function (e) {
    e.preventDefault();

    const url = document.getElementById('url').value;
    const startChapter = parseFloat(document.getElementById('startChapter').value);
    const endChapter = parseFloat(document.getElementById('endChapter').value);
    const output = document.getElementById('output');

    output.textContent = "Iniciando downloads...\n";

    let currentChapter = startChapter;

    const downloadChapter = async (chapter) => {
        let chapterUrl = url;
        if (String(chapter).includes('.5')) {
            chapterUrl += String(chapter).replace('.', '-');
        } else {
            chapterUrl += String(chapter).replace('.0', '');
        }

        try {
            console.log(`Fetching URL: ${chapterUrl}`);  // Log da URL que está sendo buscada

            const response = await fetch(chapterUrl);
            if (!response.ok) throw new Error('Capítulo não encontrado');

            const text = await response.text();
            const parser = new DOMParser();
            const doc = parser.parseFromString(text, 'text/html');

            const titleElement = doc.querySelector('h1.entry-title');
            const nameElement = doc.querySelector('div.cat-series');
            if (titleElement && nameElement) {
                const title = titleElement.textContent;
                const name = nameElement.textContent.replace(/\//g, '_').replace(/\?/g, '');

                const fileName = `${title.replace('Capítulo ', '').replace(/\s/g, '').padStart(3, '0')} - ${name}.txt`;
                const fileContent = [title, name, '', ...Array.from(doc.querySelectorAll('p')).map(p => p.textContent)].join('\n\n');

                const handle = await getDirectoryHandle();
                if (handle) {
                    const fileHandle = await handle.getFileHandle(fileName, { create: true });
                    const writable = await fileHandle.createWritable();
                    await writable.write(fileContent);
                    await writable.close();

                    output.textContent += `Capítulo ${chapter} baixado com sucesso.\n`;
                } else {
                    output.textContent += `Erro ao acessar o caminho: ${path}\n`;
                }
            } else {
                output.textContent += `Capítulo ${chapter} não encontrado no site.\n`;
            }
        } catch (error) {
            output.textContent += `Erro ao baixar capítulo ${chapter}: ${error.message}\n`;
        }
    };

    const downloadLoop = async () => {
        while (currentChapter <= endChapter) {
            await downloadChapter(currentChapter);
            currentChapter += 0.5;
        }
        output.textContent += 'Downloads concluídos.';
    };

    downloadLoop();
});

document.getElementById('selectFolderButton').addEventListener('click', async () => {
    try {
        const handle = await window.showDirectoryPicker();
        document.getElementById('path').value = handle.name;
        window.selectedDirectoryHandle = handle;
    } catch (err) {
        console.error('Erro ao selecionar a pasta:', err);
    }
});

async function getDirectoryHandle() {
    return window.selectedDirectoryHandle || null;
}
