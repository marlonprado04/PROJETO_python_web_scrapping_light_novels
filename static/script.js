function downloadCapitulos(event) {
    event.preventDefault();
    
    const url = document.getElementById('url').value;
    const capituloInicial = document.getElementById('capituloInicial').value;
    const capituloFinal = document.getElementById('capituloFinal').value;
    const caminho = document.getElementById('caminho').value; // Coleta o caminho do input
    const output = document.getElementById('output');
    
    output.innerHTML = "<li>Iniciando download...</li>";
    
    fetch('/download', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            url: url,
            capituloInicial: capituloInicial,
            capituloFinal: capituloFinal,
            caminho: caminho // Adiciona o caminho no corpo da requisição
        })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`Erro na resposta do servidor: ${response.statusText}`);
        }
        return response.json();
    })
    .then(data => {
        output.innerHTML = ''; // Limpa a saída
        data.resultados.forEach(log => {
            const li = document.createElement('li');
            li.textContent = log;
            output.appendChild(li);
        });
    })
    .catch(error => {
        output.innerHTML = `<li>Erro: ${error.message}</li>`;
    });
}
