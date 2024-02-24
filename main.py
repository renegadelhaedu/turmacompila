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

@app.route('/inserircontato')
def mostrarpaginacontato():
    return render_template('contato.html')


if __name__ == '__main__':
    app.run(debug=True) #executa/roda/starta o servidor