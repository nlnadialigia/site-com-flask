from flask import Flask, render_template

app = Flask(__name__)

# criar a 1ª página do site
# route => qual link vai ficar na página - caminho que vem depois do dominio
# função => o que será exibido na página
# template => um para cada página


@app.route('/')
def homepage():
    return render_template('homepage.html')


@app.route('/contatos')
def contatos():
    return render_template('contatos.html')


@app.route('/usuarios/<nome_usuario>')
def usuarios(nome_usuario):
    return render_template('usuarios.html', nome_usuario=nome_usuario)

# colocar o site no ar
# roda tudo que está dentro do if somente quando for executado dentro do arquivo


if __name__ == '__main__':
    app.run(debug=True)


# servidor heroku
# configurar o arquivo Procfile
# instalar gunicorn
# criar o arquivo requirements.txt => pip freeze requirements.txt
# esse arquivo contém todas as libs do projeto

