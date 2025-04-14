from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Função para carregar as mensagens do arquivo JSON
def load_messages():
    try:
        with open('database.json', 'r') as file:
            messages = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        messages = []
    return messages

# Função para salvar as mensagens no arquivo JSON
def save_messages(messages):
    with open('database.json', 'w') as file:
        json.dump(messages, file, indent=4)

# Rota para a página principal
@app.route('/')
def index():
    messages = load_messages()
    return render_template('index.html', messages=messages)

# Rota para enviar mensagem
@app.route('/send_message', methods=['POST'])
def send_message():
    user = request.form['user']
    message = request.form['message']

    messages = load_messages()
    new_message = {'user': user, 'message': message}
    messages.append(new_message)
    save_messages(messages)

    return jsonify({'user': user, 'message': message})

if __name__ == '__main__':
    app.run(debug=True)
