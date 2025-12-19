from flask import Flask, request, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'segredo_local'
socketio = SocketIO(app)

# Rota para exibir a página HTML
@app.route('/')
def index():
    return render_template('index.html')

# Rota do Webhook
@app.route('/rfid/<id_antena>', methods=['POST'])
def webhook(id_antena):
    dados = request.json
    
    # Verifica se os dados são uma lista (como no seu exemplo)
    if isinstance(dados, list):
        for item in dados:
            # Filtra apenas os campos que você quer
            leitura_filtrada = {
                'epc': item.get('reading_epc_hex', 'N/A'),
                'leitor': item.get('reading_reader_name', 'Desconhecido'),
                'origem': id_antena
            }
            # Emite o evento 'nova_leitura' para o navegador
            socketio.emit('nova_leitura', leitura_filtrada)
            print(f"Enviado para tela: {leitura_filtrada['epc']}")
            
    return 'success', 200

if __name__ == '__main__':
    # Use socketio.run para suportar WebSockets
    socketio.run(app, host='0.0.0.0', port=5000, allow_unsafe_werkzeug=True)