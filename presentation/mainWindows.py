from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QApplication, QLineEdit, QPushButton, QTableView, QHBoxLayout, QLabel
from PyQt6.QtGui import QStandardItemModel, QStandardItem
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from logic.producto import IndexProduct, CreateProduct, DropProduct, UpdateProduct

class App(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.mainWindow = MainWindow()
        self.mainWindow.show()
        
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestor de Inventario")
        self.setGeometry(100, 100, 600, 400)
        
        self.widget = QWidget()
        self.setCentralWidget(self.widget)
        
        self.Layout = QVBoxLayout(self.widget)
        
        # create a dataview table useing the modules from the logic
        self.table = QTableView()
        self.Layout.addWidget(self.table)
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(["ID", "Nombre", "Descripción", "Precio", "Cantidad"])
        for row in IndexProduct():
            self.model.appendRow([QStandardItem(str(cell)) for cell in row])
        self.table.setModel(self.model)
        self.Layout.addWidget(self.table)
        self.HLayout = QHBoxLayout()
        #create a input for the name, description, price and quantity of the product
        self.name = QLineEdit()
        self.name.setPlaceholderText("Nombre")
        self.VLayout.addWidget(self.LbName)
        self.VLayout.addWidget(self.name)
        self.description = QLineEdit()
        
        self.description.setPlaceholderText("Descripción")
        self.price = QLineEdit()
        self.price.setPlaceholderText("Precio")
        self.quantity = QLineEdit()
        self.quantity.setPlaceholderText("Cantidad")
        self.HLayout.addWidget(self.name)
        self.HLayout.addWidget(self.description)
        self.HLayout.addWidget(self.price)
        self.HLayout.addWidget(self.quantity)
        
        self.Layout.addLayout(self.HLayout)
        self.butonsData = QHBoxLayout()
        self.Save = QPushButton("Guardar")
        self.Find = QPushButton("Buscar")
        self.delete = QPushButton("Eliminar")
        self.Update = QPushButton("Actualizar")
        self.butonsData.addWidget(self.Save)
        self.butonsData.addWidget(self.Find)
        self.butonsData.addWidget(self.delete)
        self.butonsData.addWidget(self.Update)
        self.Layout.addLayout(self.butonsData)
    
    def saveData(self) -> None:
        """in this function we will save the data of the product using the logic module and the data from the inputs
        """
        CreateProduct(self.name.text(), self.description.text(), float(self.price.text()), int(self.quantity.text()))