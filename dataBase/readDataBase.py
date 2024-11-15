import os
import dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base, Session

Base = declarative_base()

def readDataBase() -> Session:
    dotenv.load_dotenv()
    user = os.getenv("user")
    password = os.getenv("password")
    host = os.getenv("host")
    port = os.getenv("port")
    dbname = os.getenv("DBName")
    
    # Cambia la cadena de conexión para PostgreSQL
    engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}')

    # Crear todas las tablas en el motor. Esto es equivalente a las sentencias "Create Table" en SQL.
    Base.metadata.create_all(engine)

    # Crear un objeto sessionmaker
    Session = sessionmaker(bind=engine)

    # Crear una sesión
    session = Session()

    return session
