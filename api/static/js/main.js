async function buscarCep(cep) {
    try {
        const response = await fetch('http://localhost:8000/cep', {
            method: 'post',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({'cep': cep})
        });

        const data = await response.json();
        return {
            status: data.status,
            message: data.message,
            type: data.type,
            data: data.data
        };
    } catch (error) {
        return {
            status: 500,
            message: 'Erro ao acessar a API',
            type: 'error',
            error: error.message
        };
    }
}

document.getElementById('searchCep').addEventListener('click', async () => {
    const cep = document.getElementById('cep').value;
    const response = document.getElementById('result');

    const dados = await buscarCep(cep);
    response.textContent = JSON.stringify(dados, null, 2);
});
