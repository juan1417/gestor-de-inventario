from PyQt6.QtWidgets import QMainWindow, QStackedWidget, QVBoxLayout, QWidget, QApplication, QTableWidget, QTableWidgetItem, QPushButton, QTableView, QStackedLayout
from PyQt6.QtGui import QStandardItemModel, QStandardItem
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from logic.producto import IndexProduct

class App(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.mainWindow = MainWindow()
        self.mainWindow.show()
        
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestor de inventario")
        self.setGeometry(100, 100, 800, 600)
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)
        self.createDataTable()
        
        
    def createDataTable(self):
        self.table = QTableView()
        products = IndexProduct()
        
        # Crear un modelo estándar
        model = QStandardItemModel()
        
        # Añadir encabezados de columna
        model.setHorizontalHeaderLabels(['ID', 'Nombre', 'Descripcion','Precio', 'Cantidad'])  # Ajusta según tus columnas
        
        for product in products:
            items = [
                QStandardItem(str(product.id)),
                QStandardItem(product.nombre),
                QStandardItem(str(product.descripcion)),
                QStandardItem(str(product.precio)),
                QStandardItem(str(product.cantidad))
            ]
            model.appendRow(items)
        
        # Establecer el modelo en la tabla
        self.table.setModel(model)
        self.stack.addWidget(self.table)
    
    def insertData(self):
        pass