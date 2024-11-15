from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

class Productos(DeclarativeBase):
    __tablename__ = "productos"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String)
    precio: Mapped[float] = mapped_column(float)
    descripcion: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    cantidad: Mapped[int] = mapped_column(int)


    def __init__(self, nombre: str, precio: float, cantidad: int, descripcion:str):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.descripcion = descripcion

    def __repr__(self):
        return f"Productos({self.id}, {self.nombre}, {self.precio}, {self.cantidad}, {self.descripcion})"