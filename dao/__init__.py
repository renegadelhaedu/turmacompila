

def checarlogin(users:list, usuario, senha):
    for user in users:
        if user['email'] == usuario and user['senha'] == senha:
            return True
    return False

def cadastrarusuario(users:list, nome, idade, email, senha):
    novousuario = {'nome':nome, 'idade':idade, 'email':email, 'senha': senha}
    if not usuarioexiste(users, email):
        users.append(novousuario)
        return True #deu certo inserir o novo usuario no banco
    else:
        return False #deu ruim pq ja tinha um user com este email

def usuarioexiste(users:list, email):
    for user in users:
        if user['email'] == email:
            return True  # já existe um usuario com este login
    return False # nao existe ninguem com este login


def registrar_contato(nome, email, comentario):
    print('ok')
    return True