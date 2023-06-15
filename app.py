from flask import Flask, request, jsonify
import os
import json

app = Flask(__name__)

# Diretório de destino para salvar os arquivos JSON recebidos
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/api/receive-data', methods=['POST'])
def receive_data():
    data = request.json
    # Processar os dados recebidos conforme necessário
    print("Dados recebidos:", data)

    # Salvar o arquivo JSON recebido em um diretório
    filename = 'received.json'
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    with open(filepath, 'w') as file:
        json.dump(data, file)

    return jsonify({'message': 'Dados recebidos com sucesso'})

if __name__ == '__main__':
    # Certifique-se de criar o diretório 'received_files' antes de iniciar o servidor
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(host='localhost', port=8080)


    
