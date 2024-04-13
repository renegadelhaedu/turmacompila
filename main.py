from flask import *
import dao
import data_analise as da

#isntancia o servidor flask
app = Flask(__name__)
app.secret_key = '1'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/logout')
def logout():
    #removeu do servidor
    session.pop('idusuario', None)

    res = make_response("Cookie Removido")
    res.set_cookie('idusuario', '', max_age=0)

    return render_template('home.html')


@app.route('/inscricao')
def inscricao():
    return render_template('inscricao.html')

@app.route('/cadastrarusuario', methods=['POST'])
def cadastrar_usuario():

    nome = request.form.get('nomeusuario')
    idade = request.form.get('idadeusuario')
    email = request.form.get('emailusuario')
    senha = request.form.get('senhausuario')

    if dao.cadastrarusuario(nome, idade, email, senha):
        return render_template('home.html', msg='Usuário inserido com sucesso')
    else:
        return render_template('home.html', msg='Usuário já existe')


@app.route('/verificarlogin', methods=['POST', 'GET'])
def verificar_login():

    if request.method == 'GET' and session.get('idusuario') != None:
        figura = da.processar_dados(da.importar_dados())
        return render_template('logado.html', email=session.get('idusuario'), fig=figura)
    elif request.method == 'POST':
        user = request.form.get('emailusuario')
        senha = request.form.get('senhausuario')

        if dao.checarlogin(user, senha):
            session['idusuario'] = user
            figura = da.processar_dados(da.importar_dados())
            return render_template('logado.html', email=user, fig=figura)
        else:
            return render_template('errologin.html')
    else:
        return render_template('errologin.html')


@app.route('/entraremcontato')
def mostrarpaginacontato():
    if session.get('idusuario') != None:
        return render_template('contato.html', email=session['idusuario'])
    else:
        return render_template('home.html')

@app.route('/inserircontato', methods=['POST','GET'])
def inserircontato():

    if request.method == 'POST':
        nome = request.form.get('nome')  # POST
        email = request.form.get('email')
        texto = request.form.get('texto')
        cep = request.form.get('cep')
    else:
        nome = request.args.get('nome')  # GET
        email = request.args.get('email')
        texto = request.args.get('texto')
        cep = request.args.get('cep')

    cep = cep.replace('-','')
    if dao.registrar_contato(nome, email, texto, cep, session['idusuario']):
        return render_template('logado.html')
    else:
        #criar pagina de erro de contato
        return render_template('contato.html', msg='cep invalido')

@app.route('/listarmensagens')
def listar_msg():
    if session.get('idusuario') != None:
        respostas = dao.listar_msgs_user(session['idusuario'])
        return render_template('exibirlistamsgs.html', lista=respostas, email=session['idusuario'] )
    else:
        return render_template('home.html')


@app.route('/interessecz')
def mostrar_interessecz():
    figura = da.processar_dados(da.importar_dados())

    return render_template('mostrarinteresse.html', fig=figura)


if __name__ == '__main__':
    app.run(debug=True) #executa/roda/starta o servidor