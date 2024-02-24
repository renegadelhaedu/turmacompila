from flask import *
import dao

#isntancia o servidor flask
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/verificarlogin', methods=['POST'])
def verificar_login():
    user = request.form.get('emailusuario')
    senha = request.form.get('senhausuario')
    nome_user = user.split('@')[0]

    if dao.checarlogin(user, senha):
        return render_template('logado.html', email=nome_user)
    else:
        return render_template('errologin.html')


@app.route('/entraremcontato')
def mostrarpaginacontato():
    return render_template('contato.html')

@app.route('/inserircontato', methods=['POST'])
def inserircontato():
    nome = request.form.get('nome')
    email = request.form.get('email')
    texto = request.form.get('texto')

    if dao.inserir_contato(nome, email, texto):
        return render_template('index.html')
    else:
        #criar pagina de erro de contato
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True) #executa/roda/starta o servidor