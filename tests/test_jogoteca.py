import sys
import os
import pytest
from flask_testing import TestCase

# Configura a variável de ambiente para o ambiente de teste
os.environ['FLASK_ENV'] = 'testing'

# Adiciona o diretório raiz do projeto ao caminho de busca do Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from jogoteca import app, db  # Importa o aplicativo Flask existente, mas não inicializa uma nova instância do SQLAlchemy
from models import Jogos

class TestJogoteca(TestCase):

    # Método para criar o aplicativo Flask para os testes
    def create_app(self):
        print("Criando o aplicativo Flask para os testes")
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:12345678@localhost/teste_db'
        return app

    # Método executado antes de cada teste
    def setUp(self):
        print("Configurando o ambiente de teste")
        with app.app_context():
            db.create_all()

    # Método executado após cada teste
    # def tearDown(self):
    #    print("Limpando o ambiente de teste")
    #    with app.app_context():
    #        db.session.remove()
    #    with app.app_context():
    #        db.drop_all()

    # Teste para verificar se um jogo pode ser criado
    def test_criar_jogo(self):
        print("Executando o teste para criar um jogo")
        with self.app.test_client() as client:
            # Simula uma requisição POST para a rota /criar com dados do formulário
            response = client.post('/criar', data={
                'nome': 'Super Mario',
                'categoria': 'Plataforma',
                'console': 'Nintendo Switch'
            }, follow_redirects=True)

            # Verifica se a resposta HTTP é 200 OK
            assert response.status_code == 200, f"A resposta HTTP foi {response.status_code}, esperava-se 200."

            # Verifica se o jogo foi criado no banco de dados
            jogo_criado = Jogos.query.filter_by(nome='Super Mario').first()
            assert jogo_criado is not None
