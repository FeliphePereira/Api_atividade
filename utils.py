from models import Pessoas, Usuarios

def insere_pessoas():
    pessoa = Pessoas(nome = 'Felipe', idade = 29)
    print(pessoa)
    pessoa.save()

def consulta_pessoa():
    #pessoa = Pessoas.query.all()
    #print(pessoa)
    pessoa = Pessoas.query.filter_by(nome='Rafael').first()
    print(pessoa.idade)

def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome = 'Rafael').first()
    pessoa.idade = 21
    pessoa.save()

def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome = 'Felipe').first()
    pessoa.delete()

def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)

if __name__ == '__main__':
    #insere_pessoas()
    #altera_pessoa()
    #consulta_pessoa()
    #exclui_pessoa()