# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'crear.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets



class MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(437, 315)
        self.Tabla = QtWidgets.QWidget(MainWindow)
        self.Tabla.setObjectName("Tabla")
        self.label = QtWidgets.QLabel(self.Tabla)
        self.label.setGeometry(QtCore.QRect(20, 10, 141, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.Tabla)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 111, 16))
        self.label_2.setObjectName("label_2")
        self.txtnbs = QtWidgets.QLineEdit(self.Tabla)
        self.txtnbs.setGeometry(QtCore.QRect(170, 10, 171, 21))
        self.txtnbs.setObjectName("txtnbs")
        self.txtnt = QtWidgets.QLineEdit(self.Tabla)
        self.txtnt.setGeometry(QtCore.QRect(170, 50, 171, 20))
        self.txtnt.setObjectName("txtnt")
        self.groupBox = QtWidgets.QGroupBox(self.Tabla)
        self.groupBox.setGeometry(QtCore.QRect(20, 90, 391, 181))
        self.groupBox.setObjectName("groupBox")
        self.txtnc = QtWidgets.QLineEdit(self.groupBox)
        self.txtnc.setGeometry(QtCore.QRect(10, 50, 141, 20))
        self.txtnc.setObjectName("txtnc")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 91, 16))
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(160, 50, 111, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(170, 20, 71, 16))
        self.label_4.setObjectName("label_4")
        self.boton1 = QtWidgets.QPushButton(self.groupBox)
        self.boton1.setGeometry(QtCore.QRect(290, 50, 75, 23))
        self.boton1.setObjectName("boton1")
        self.boton2 = QtWidgets.QPushButton(self.groupBox)
        self.boton2.setGeometry(QtCore.QRect(130, 120, 131, 23))
        self.boton2.setObjectName("boton2")
        MainWindow.setCentralWidget(self.Tabla)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 437, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Nombre de la base de datos"))
        self.label_2.setText(_translate("MainWindow", "Nombre de la tabla"))
        self.groupBox.setTitle(_translate("MainWindow", "Columna"))
        self.label_3.setText(_translate("MainWindow", "Nombre columna"))
        self.comboBox.setItemText(0, _translate("MainWindow", "INTEGER"))
        self.comboBox.setItemText(1, _translate("MainWindow", "TEXT"))
        self.comboBox.setItemText(2, _translate("MainWindow", "REAL"))
        self.label_4.setText(_translate("MainWindow", "Tipo de dato"))
        self.boton1.setText(_translate("MainWindow", "Agregar"))
        self.boton2.setText(_translate("MainWindow", "crear base de datos"))
