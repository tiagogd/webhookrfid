# webhookrfid
Webhook para receber leituras das antenas RFID

=====================================================
SISTEMA DE MONITORAMENTO RFID - WEBHOOK LOCAL
=====================================================

1. ESTRUTURA DE PASTAS:
   /seu-projeto
   ├── app.py              (O código Python enviado anteriormente)
   └── /templates
       └── index.html      (O código HTML/JS enviado anteriormente)

2. REQUISITOS (INSTALAÇÃO):
   Abra o terminal na pasta do projeto e execute:
   > pip install flask flask-socketio

3. COMO EXECUTAR:
   1. No terminal, execute: python app.py
   2. O terminal dirá: "Running on http://0.0.0.0:5000"
   3. MANTENHA O TERMINAL ABERTO.

4. COMO VISUALIZAR:
   1. Abra seu navegador (Chrome, Edge ou Firefox).
   2. Acesse o endereço: http://localhost:5000
   3. Você verá a tabela vazia "Leituras em Tempo Real".

5. COMO TESTAR O RECEBIMENTO (Via Terminal):
   Para simular o leitor enviando dados, use este comando:
   > curl -X POST http://127.0.0.1:5000/webhook/TesteAntena -H "Content-Type: application/json" -d "[{\"reading_epc_hex\":\"ABC123\", \"reading_reader_name\":\"Leitor_Alpha\"}]"

6. COPIAR DADOS:
   - Clique no botão verde "Copiar para Excel" no topo da página.
   - Abra o Excel e pressione Ctrl+V.

OBS: Se o navegador for fechado, os dados da tela sumirão (não salvos em banco).
=====================================================
