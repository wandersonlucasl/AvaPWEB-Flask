from flask import Flask, render_template, request, redirect

app = Flask(__name__, template_folder='templates')

bantimes = []

@app.route('/')
def home():
    return render_template('index.html', titulo_pagina="Página inicial")

@app.route('/listar')
def listar():
    return render_template('listar.html', times=bantimes, titulo_pagina="Times Cadastrados")

@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        nome = request.form['nome']
        cidade = request.form['cidade']
        estado = request.form['estado']
        novo_time = {"id": len(bantimes) + 1, "nome": nome, "cidade": cidade, "estado": estado}
        bantimes.append(novo_time)
        return redirect('/listar')
    return render_template('cadastrar.html', titulo_pagina="Cadastrar Time")

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    time = next((time for time in bantimes if time['id'] == id), None)
    if request.method == 'POST':
        if time:
            time['nome'] = request.form['nome']
            time['cidade'] = request.form['cidade']
            time['estado'] = request.form['estado']
            return redirect('/listar')
        else:
            return "Time não encontrado."
    return render_template('editar.html', time=time, titulo_pagina="Editar Time")

@app.route('/excluir/<int:id>', methods=['POST'])
def excluir(id):
    time = next((time for time in bantimes if time['id'] == id), None)
    if time:
        bantimes.remove(time)
        return redirect('/listar')
    else:
        return "Time não encontrado."
    
if __name__ == '__main__':
    app.run(debug=True)
