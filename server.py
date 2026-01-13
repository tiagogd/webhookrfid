from flask import Flask, request, abort

app = Flask(__name__)

@app.route('/rfid/<id_antena>', methods=['POST'])
def webhook(id_antena):
    if request.method == 'POST':
        print(request.json)
        return "Leitura recebida"
    else:
        abort(400)

if __name__ == '__main__':
    app.run(debug=False)