from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import requests


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(330, 260)
        MainWindow.setMinimumSize(QtCore.QSize(330, 260))
        MainWindow.setMaximumSize(QtCore.QSize(330, 260))
        MainWindow.setFocusPolicy(QtCore.Qt.ClickFocus)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(31, 31, 31);")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.titulo = QtWidgets.QLabel(self.centralwidget)
        self.titulo.setGeometry(QtCore.QRect(10, 10, 311, 31))
        self.titulo.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.titulo.setFont(font)
        self.titulo.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.titulo.setAutoFillBackground(False)
        self.titulo.setStyleSheet("background-color: rgb(19, 19, 19);\n"
"border-radius: 2px;")
        self.titulo.setTextFormat(QtCore.Qt.RichText)
        self.titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.titulo.setWordWrap(False)
        self.titulo.setObjectName("titulo")
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(250, 190, 71, 23))
        self.exit.setStyleSheet("background-color: rgb(209, 209, 209);\n"
"border-radius: 3px;")
        self.exit.setObjectName("exit")
        self.btn_converte = QtWidgets.QPushButton(self.centralwidget)
        self.btn_converte.setGeometry(QtCore.QRect(90, 160, 141, 23))
        self.btn_converte.setStyleSheet("background-color: rgb(209, 209, 209);\n"
"")
        self.btn_converte.setObjectName("btn_converte")
        self.aposta1 = QtWidgets.QLabel(self.centralwidget)
        self.aposta1.setGeometry(QtCore.QRect(50, 50, 121, 21))
        self.aposta1.setMinimumSize(QtCore.QSize(51, 20))
        self.aposta1.setMaximumSize(QtCore.QSize(16777215, 150000))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.aposta1.setFont(font)
        self.aposta1.setStyleSheet("background-color: rgb(0, 85, 255);\n"
"border-radius: 3px;")
        self.aposta1.setAlignment(QtCore.Qt.AlignCenter)
        self.aposta1.setObjectName("aposta1")
        self.rcb_Dolar = QtWidgets.QLineEdit(self.centralwidget)
        self.rcb_Dolar.setGeometry(QtCore.QRect(180, 50, 111, 21))
        self.rcb_Dolar.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 3px;")
        self.rcb_Dolar.setObjectName("rcb_Dolar")
        self.titulo_2 = QtWidgets.QLabel(self.centralwidget)
        self.titulo_2.setGeometry(QtCore.QRect(10, 80, 311, 31))
        self.titulo_2.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.titulo_2.setFont(font)
        self.titulo_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.titulo_2.setAutoFillBackground(False)
        self.titulo_2.setStyleSheet("background-color: rgb(19, 19, 19);\n"
"border-radius: 2px;")
        self.titulo_2.setTextFormat(QtCore.Qt.RichText)
        self.titulo_2.setAlignment(QtCore.Qt.AlignCenter)
        self.titulo_2.setWordWrap(False)
        self.titulo_2.setObjectName("titulo_2")
        self.aposta1_2 = QtWidgets.QLabel(self.centralwidget)
        self.aposta1_2.setGeometry(QtCore.QRect(50, 120, 121, 21))
        self.aposta1_2.setMinimumSize(QtCore.QSize(51, 20))
        self.aposta1_2.setMaximumSize(QtCore.QSize(16777215, 150000))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.aposta1_2.setFont(font)
        self.aposta1_2.setStyleSheet("background-color: rgb(0, 85, 255);\n"
"border-radius: 3px;")
        self.aposta1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.aposta1_2.setObjectName("aposta1_2")
        self.rcb_Real = QtWidgets.QLineEdit(self.centralwidget)
        self.rcb_Real.setGeometry(QtCore.QRect(180, 120, 111, 21))
        self.rcb_Real.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 3px;")
        self.rcb_Real.setObjectName("rcb_Real")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 330, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_Fechar = QtWidgets.QAction(MainWindow)
        self.action_Fechar.setObjectName("action_Fechar")

        self.retranslateUi(MainWindow)
        self.exit.clicked.connect(MainWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.btn_converte.clicked.connect(self.converter)
        
    def converter(self):
        try:
            if self.rcb_Real.text() == "":
                valorReal = 0
            else:
                valorReal = float(self.rcb_Real.text())
            if self.rcb_Dolar.text() == "":
                valorDolar = 0
            else:
                valorDolar = float(self.rcb_Dolar.text())
            #Pega a cotação atual do Dolar
            cotacao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
            cotacao_dic = cotacao.json()
            valorCotacao = float(cotacao_dic['USDBRL']['bid'])
            #Converte
            converteReal = valorDolar*valorCotacao
            converteDolar = valorReal/valorCotacao
            #Abre a janela informando os valores
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Resultado")
            msg.setText(f'COTAÇÃO ATUAL DO DÓLAR: USD${valorCotacao}')
            msg.setInformativeText(f'''
            Conversão:
            USD${valorDolar:.2f} = R${converteReal:.2f} reais.
            R${valorReal:.2f} = USD${converteDolar:.2f} dólares.''')
            msg.exec()
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Resultado")
            msg.setText(f'ERRO')
            msg.setInformativeText(f'''INFORME OS VALORES CORRETAMENTE E TENTE NOVAMENTE''')
            msg.exec()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Conversor De Moeda"))
        self.titulo.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Dólar para Real:</span></p></body></html>"))
        self.exit.setText(_translate("MainWindow", "SAIR"))
        self.btn_converte.setText(_translate("MainWindow", "CONVERTER"))
        self.aposta1.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Valor em US$:</span></p></body></html>"))
        self.titulo_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Real para Dólar:</span></p></body></html>"))
        self.aposta1_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Valor em R$:</span></p></body></html>"))
        self.action_Fechar.setText(_translate("MainWindow", "&Fechar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
