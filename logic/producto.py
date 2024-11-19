import sys
import os
from typing import Any, Sequence
from sqlalchemy import text
from sqlalchemy.engine.row import Row

# Añadir el directorio raíz del proyecto al PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dataBase.readDataBase import readDataBase

session = readDataBase()


def IndexProduct() -> Sequence[Row[Any]]:
    Query = text("SELECT * FROM productos")
    result = session.execute(Query).fetchall()
    return result

def DropProduct(id: int) -> None:
    Query = text(f"DELETE FROM productos WHERE id = {id}")
    session.execute(Query)
    session.commit()
    
def CreateProduct(name: str, description:str ,price: float, cantidad:int) -> None:
    Query = text(f"INSERT INTO productos (nombre, descripcion,precio, cantidad) VALUES ('{name}','{description}' ,{price}, {cantidad})")
    session.execute(Query)
    session.commit()

def UpdateProduct(id: int, name: str, descrition:str , price: float, cantidad:int) -> None:
    Query = text(f"UPDATE productos SET nombre = '{name}', descripcion = '{descrition}', precio = {price}, cantidad={cantidad} WHERE id = {id}")
    session.execute(Query)
    session.commit()

def FindProduct(name: str) -> Sequence[Row[Any]]:
    Query = text(f"SELECT * FROM productos WHERE nombre = '{name}'")
    result = session.execute(Query).fetchall()
    return result