# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!

import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog

compra = 0


#
# Window
#

class Ui_MainWindow(QDialog):

    


    def finish(self):
        global compra
        self.listWidget.clear()
        self.valorAtualizado.clear()
        df.to_excel('FATURAMENTO.xlsx',  sheet_name='Faturamento do dia')
        compra = 0
        
    def delete(self):
        global compra
        produtoExcluido = self.listWidget.currentItem().text()
        codigo, produto = produtoExcluido.split("     ", 1)
        quantidade, produto = produto.split("   ", 1)
        df.at[int(codigo), 'Quantidade'] = df.at[int(codigo), 'Quantidade'] - int(quantidade)
        df.at[int(codigo), 'Valor'] = df.at[int(codigo), 'Valor'] - df.at[int(codigo), 'Preço']*int(quantidade)
        compra = compra - df.at[int(codigo), 'Preço']*int(quantidade)
        self.valorAtualizado.setText(str(round(compra, 2)))

        

        self.listWidget.takeItem(self.listWidget.currentRow())
        
         

    def add(self):
        global compra
        codProduto = int(self.lineEdit_codigoProduto.text())
        qntProduto = int(self.lineEdit_quantidadeProduto.text())
        nomeProduto = df.at[codProduto, 'Produto']
        compra = compra + df.at[codProduto, 'Preço']*qntProduto
        df.at[codProduto, 'Quantidade'] = df.at[codProduto, 'Quantidade'] + qntProduto
        df.at[codProduto, 'Valor'] = df.at[codProduto, 'Preço'] * df.at[codProduto, 'Quantidade']
        self.listWidget.addItem(str(codProduto) + "     " + str(qntProduto) + "   " + str(nomeProduto))
        self.lineEdit_codigoProduto.clear()
        self.lineEdit_quantidadeProduto.clear()
        self.valorAtualizado.setText(str(round(compra, 2)))

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(925, 446)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_codigoProduto = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_codigoProduto.setGeometry(QtCore.QRect(90, 80, 150, 70))
        self.lineEdit_codigoProduto.setObjectName("lineEdit_codigoProduto")
        self.lineEdit_quantidadeProduto = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_quantidadeProduto.setGeometry(QtCore.QRect(280, 80, 150, 70))
        self.lineEdit_quantidadeProduto.setObjectName("lineEdit_quantidadeProduto")
        self.pushButton_OK = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_OK.setGeometry(QtCore.QRect(460, 90, 111, 41))
        self.pushButton_OK.setObjectName("pushButton_OK")
        self.pushButton_delete = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_delete.setGeometry(QtCore.QRect(500, 200, 150, 70))
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.pushButton_delete.setText("Delete")
        self.valor = QtWidgets.QLabel(self.centralwidget)
        self.valor.setGeometry(QtCore.QRect(650, 230, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.valor.setFont(font)
        self.valor.setObjectName("valor")
        self.valorAtualizado = QtWidgets.QLabel(self.centralwidget)
        self.valorAtualizado.setGeometry(QtCore.QRect(790, 250, 55, 16))
        self.valorAtualizado.setObjectName("valorAtualizado")
        self.pushButton_finalizarCompra = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_finalizarCompra.setGeometry(QtCore.QRect(670, 360, 191, 51))
        self.pushButton_finalizarCompra.setObjectName("pushButton_finalizarCompra")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(630, 20, 256, 192))
        self.listWidget.setObjectName("listWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        

        self.pushButton_OK.clicked.connect(self.add)
        self.pushButton_finalizarCompra.clicked.connect(self.finish)
        self.pushButton_delete.clicked.connect(self.delete)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit_codigoProduto.setPlaceholderText(_translate("MainWindow", "Código do produto"))
        self.lineEdit_quantidadeProduto.setPlaceholderText(_translate("MainWindow", "Quantidade"))
        self.pushButton_OK.setText(_translate("MainWindow", "OK"))
        self.valor.setText(_translate("MainWindow", "Valor "))
        self.valorAtualizado.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_finalizarCompra.setText(_translate("MainWindow", "Finalizar Compra"))

    
        


if __name__ == "__main__":
    import sys
    df = pd.read_excel('FATURAMENTO_vs2.xlsx')
    compra = 0
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
