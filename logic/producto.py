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
    result = session.execute(text("SELECT * FROM Productos")).fetchall()
    return result