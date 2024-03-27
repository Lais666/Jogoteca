import os

# Define o caminho do banco de dados principal
DATABASE_PATH = 'mysql+mysqlconnector://root:12345678@localhost/jogoteca'

# Verifica se estamos no ambiente de teste
if os.environ.get('FLASK_ENV') == 'testing':
    # Se estivermos no ambiente de teste, usa um banco de dados de teste
    DATABASE_PATH = 'mysql+mysqlconnector://root:12345678@localhost/teste_db'

SECRET_KEY = 'alura'

# Define o URI do banco de dados com base no caminho definido acima
SQLALCHEMY_DATABASE_URI = DATABASE_PATH

UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'
