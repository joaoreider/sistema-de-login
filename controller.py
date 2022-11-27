from model import Pessoa
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
# cripitografia dos dados
import hashlib 

def retorna_session():

    USUARIO = "root"
    SENHA = ""
    HOST = "localhost"
    BANCO = "cadastrosistema"
    PORT = "3306"

    conn = f"mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BANCO}"

    engine = create_engine(conn, echo=True)
    Session = sessionmaker(bind=engine)
    return Session()

class ControllerCadastro():
    @classmethod
    def verificar_dados(cls, nome, email, senha):
        if len(nome) > 50 or len(nome) < 2:
            return 2
        if len(email) > 200:
            return 3
        if len(senha)>100 or len(senha) < 7:
            return 4
        
        return 1
    
    @classmethod
    def cadastrar(cls, nome, email, senha):
        # conectando ao banco
        session = retorna_session()
        # filtro se existe o email cadastro
        usuario = session.query(Pessoa).filter(Pessoa.email == email).all()
        if len(usuario) > 0:
            return 5
        
        dados_verificados = cls.verificar_dados(nome, email, senha)
        # erro de verificacao
        if  dados_verificados != 1:
            return dados_verificados
        
        # tudo ocorreu como esperado
        try:
            # encode para passar a string como binário
            senha = hashlib.sha256(senha.encode()).hexdigest()
            p1 = Pessoa(nome = nome, email = email, senha = senha)
            session.add(p1)
            session.commit()
            return 1

        except:
            return 6

class ControllerLogin():
    @classmethod
    def login(cls, email, senha):
        session = retorna_session()
        senha = hashlib.sha256(senha.encode()).hexdigest()
        logado = session.query(Pessoa).filter(Pessoa.email==email).filter(Pessoa.senha == senha ).all()
        if len(logado) == 1:
            return {'logado':True, 'id':logado[0].id}
        else:
            return False

