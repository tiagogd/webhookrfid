from flask import Flask, request, render_template
from flask_socketio import SocketIO
import json
from datetime import datetime

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
    
    try:
        with open("leituras.txt", "a", encoding="utf-8") as f:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            # Salva no formato: [DATA] ID_ANTENA: JSON_DATA
            linha = f"[{timestamp}] {id_antena}: {json.dumps(dados, ensure_ascii=False)}\n"
            f.write(linha)
    except Exception as e:
        print(f"Erro ao salvar arquivo: {e}")

    # Verifica se os dados são uma lista
    if isinstance(dados, list):
        for item in dados:
            # --- CONVERSÃO DE DATA ---
            data_br = item.get('reading_created_at', '')
            try:
                # 1. Lê o formato original (Ano-Mês-Dia Hora:Min:Seg)
                dt_obj = datetime.strptime(data_br, '%Y-%m-%d %H:%M:%S')
                # 2. Converte para Brasileiro (Dia/Mês/Ano Hora:Min:Seg)
                data_br = dt_obj.strftime('%d/%m/%Y %H:%M:%S')
            except ValueError:
                pass # Se der erro, mantém a data original sem formatar
            
            # Filtra apenas os campos que você quer
            leitura_filtrada = {
                'epc': item.get('reading_epc_hex', 'N/A'),
                'leitor': item.get('reading_reader_name', 'Desconhecido'),
                'origem': id_antena,
                'data': data_br
            }
            # Emite o evento 'nova_leitura' para o navegador
            socketio.emit('nova_leitura', leitura_filtrada)
            print(f"Enviado para tela: {leitura_filtrada['epc']}")
            
    return 'Leitura recebida com sucesso', 200

if __name__ == '__main__':
    # Use socketio.run para suportar WebSockets
    socketio.run(app, host='0.0.0.0', port=5000, allow_unsafe_werkzeug=True)