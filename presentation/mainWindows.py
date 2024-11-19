from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QApplication, QLineEdit, QPushButton, QTableView, QHBoxLayout, QMessageBox
from PyQt6.QtGui import QStandardItemModel, QStandardItem
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from logic.producto import IndexProduct, CreateProduct, DropProduct, UpdateProduct, FindProduct

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
        self.loadData()
        self.Layout.addWidget(self.table)
        self.HLayout = QHBoxLayout()
        #create a input for the name, description, price and quantity of the product
        self.id = QLineEdit()
        self.id.setPlaceholderText("ID")
        self.name = QLineEdit()
        self.name.setPlaceholderText("Nombre")
        self.description = QLineEdit()
        self.description.setPlaceholderText("Descripción")
        self.price = QLineEdit()
        self.price.setPlaceholderText("Precio")
        self.quantity = QLineEdit()
        self.quantity.setPlaceholderText("Cantidad")
        self.HLayout.addWidget(self.id)
        self.HLayout.addWidget(self.name)
        self.HLayout.addWidget(self.description)
        self.HLayout.addWidget(self.price)
        self.HLayout.addWidget(self.quantity)     
        self.Layout.addLayout(self.HLayout)
        self.butonsData = QHBoxLayout()
        self.Save = QPushButton("Guardar")
        self.Save.clicked.connect(self.saveData)
        self.Find = QPushButton("Buscar")
        self.Find.clicked.connect(self.findProduct)
        self.delete = QPushButton("Eliminar")
        self.delete.clicked.connect(self.deleteData)
        self.Update = QPushButton("Actualizar")
        self.Update.clicked.connect(self.updateData)
        self.butonsData.addWidget(self.Save)
        self.butonsData.addWidget(self.Find)
        self.butonsData.addWidget(self.delete)
        self.butonsData.addWidget(self.Update)
        self.Layout.addLayout(self.butonsData)
    
    def loadData(self) -> None:
        self.model.clear()
        self.model.setHorizontalHeaderLabels(["ID", "Nombre", "Descripción", "Precio", "Cantidad"])
        for row in IndexProduct():
            self.model.appendRow([QStandardItem(str(cell)) for cell in row])
        self.table.setModel(self.model)
        

    def saveData(self) -> None:
        """in this function we will save the data of the product using the logic module and the data from the inputs
        """
        if self.name.text() == "" or self.description.text() == "" or self.price.text() == "" or self.quantity.text() == "":
            QMessageBox.critical(self, "Error", "Todos los campos deben estar llenos.")
            return
        CreateProduct(self.name.text(), self.description.text(), float(self.price.text()), int(self.quantity.text())) 
        self.loadData()
        #clear the inputs
        self.name.clear()
        self.description.clear()
        self.price.clear()
        self.quantity.clear()
        
    def deleteData(self) -> None:
        """in this function we will delete the data of the product using the logic module and the data from the inputs
        """
        if self.id.text() == "":
            QMessageBox.critical(self, "Error", "El campo ID debe estar lleno.")
            return
        DropProduct(int(self.id.text()))
        self.loadData()
        #clear the inputs
        self.id.clear()
        self.name.clear()
        self.description.clear()
        self.price.clear()
        self.quantity.clear()
    
    def updateData(self) -> None:
        """in this function we will update the data of the product using the logic module and the data from the inputs
        """
        if self.name.text() == "" or self.description.text() == "" or self.price.text() == "" or self.quantity.text() == "":
            QMessageBox.critical(self, "Error", "Todos los campos deben estar llenos.")
            return
        UpdateProduct(self.name.text(), self.description.text(), float(self.price.text()), int(self.quantity.text())) 
        self.loadData()
        #clear the inputs
        self.name.clear()
        self.description.clear()
        self.price.clear()
        self.quantity.clear()
    
    def findProduct(self) -> None:
        """in this function we will find the data of the product using the logic module and the data from the inputs
        """
        if self.name.text() == "":
            QMessageBox.critical(self, "Error", "El campo nombre debe estar lleno.")
            return
        for row in FindProduct(self.name.text()):
            self.model.appendRow([QStandardItem(str(cell)) for cell in row])
        self.table.setModel(self.model)
        #clear the inputs
        self.name.clear()
        self.description.clear()
        self.price.clear()
        self.quantity.clear()