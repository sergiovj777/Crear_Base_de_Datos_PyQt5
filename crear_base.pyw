import sys
from patsy import dmatrices
from PyQt5 import uic, QtWidgets
import sys
from PyQt5.QtCore import pyqtSlot 
from PyQt5.QtWidgets import QDialog, QMainWindow,QPushButton, QFrame, QApplication, QMessageBox
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
import sqlite3
import base64
import time
import datetime
import re
from sqlite3 import Error


from PyQt5.QtWidgets import  QApplication, QDialog, QMessageBox
from PyQt5.QtWidgets import QDialog, QMainWindow,QPushButton, QFrame, QApplication, QMessageBox
from PyQt5.uic import loadUi
import sqlite3
from sqlite3 import Error
from collections import namedtuple
import re



columna = namedtuple('Columna',['nombre','tipo'])
qtCreatorFile = "crear.ui" #Aquí va el nombre de tu archivo

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        columna = namedtuple('Columna',['nombre','tipo'])

        self.columna = []
        patron = '[a-zA-Z]+'
        self.regex = re.compile(patron)
        self.mensajes = QMessageBox(self)
        
        #Aquí van los botones
        self.boton1.clicked.connect(self.agregar_columna)
        self.boton2.clicked.connect(self.crear_base)

        self.show()
        


    def agregar_columna(self):
    	nombre_columna = self.txtnc.text().strip()
    	if self.regex.match(nombre_columna) is not None:

    		tipo_dato = str(self.comboBox.currentText())
    		self.columna.append(columna(nombre_columna, tipo_dato))
    		self.txtnc.setText('')
           

    	else:
    		self.mensajes.setWindowTitle('Mensaje')
    		self.mensajes.setText('Debe escribir un nombre de columna valido(caracteres alfabeticos)')
    		self.mensajes.exec_()
            

    def crear_base(self):
    	base_datos = self.txtnbs.text().strip()
    	tabla = self.txtnt.text().strip()
    	if self.regex.match(base_datos) is not None:
    		if self.regex.match(tabla) is not None:
    			if len(self.columna) > 0:
    				sql = f'CREATE TABLE IF NOT EXISTS {tabla} ('
    				plantilla_campos = '{} {}'
    				campos = []

    				for c in self.columna:
    					 campos.append(plantilla_campos.format(c.nombre, c.tipo))
    				lista_campos = ', '.join(campos)
    				sql += lista_campos + ')'
    				try:
    					conexion = sqlite3.connect(base_datos + '.db')
    					cur = conexion.cursor()
    					cur.execute(sql)
    					self.mensajes.setWindowTitle('Mensaje')
    					self.mensajes.setIcon(QMessageBox.Information)
    					self.mensajes.setText('Se ha creado la base de datos')
    					self.mensajes.exec_()
    				except Error as e:
    					self.mensajes.setWindowTitle('Mensaje')
    					self.mensajes.setIcon(QMessageBox.Warning)
    					self.mensajes.setText('Error')
    					self.mensajes.exec_()
    				finally:
    					conexion.close()
    			else:
    				self.mensajes.setWindowTitle('Mensaje')
    				self.mensajes.setIcon(QMessageBox.Warning)
    				self.mensajes.setText('Debe agrgar minimo una columna')
    				self.mensajes.exec_() 
    		else:
    			self.mensajes.setWindowTitle('Mensaje')
    			self.mensajes.setIcon(QMessageBox.Warning)
    			self.mensajes.setText('Debe escribir un nombre valido (caracteres alfabeticos)')
    			self.mensajes.exec_()
        

    	else:
    		self.mensajes.setWindowTitle('Mensaje')
    		self.mensajes.setIcon(QMessageBox.Warning)
    		self.mensajes.setText('Debe escribir un nombre valido (caracteres alfabeticos)')
    		self.mensajes.exec_()

   

    	


if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
