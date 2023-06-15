import requests

# URL da API
url = 'http://localhost:8080/api/receive-data'

# Dados a serem enviados
dados = {
    'dataMovimento': '2023-06-15',
    'unidade': 'Unidade A',
    'tipo': 'Tipo X',
    'categoria': 'Categoria Y',
    'origem': 'Origem Z',
    'destino': 'Destino W',
    'observacao': 'Observação adicional',
    'valorReais': 100.0,
    'status': 'Ativo'
}

# Enviar a requisição POST para a API
response = requests.post(url, json=dados)

# Verificar o código de status da resposta
if response.status_code == 200:
    print('Dados enviados com sucesso para a API!')
else:
    print('Erro ao enviar os dados para a API:', response.text)
