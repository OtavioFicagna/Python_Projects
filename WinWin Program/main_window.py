from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

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
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(70, 50, 192, 111))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.recebeOdd1_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.recebeOdd1_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 3px;")
        self.recebeOdd1_2.setObjectName("recebeOdd1_2")
        self.gridLayout.addWidget(self.recebeOdd1_2, 1, 1, 1, 1)
        self.recebeOdd1 = QtWidgets.QLineEdit(self.layoutWidget)
        self.recebeOdd1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 3px;")
        self.recebeOdd1.setObjectName("recebeOdd1")
        self.gridLayout.addWidget(self.recebeOdd1, 0, 1, 1, 1)
        self.recebeOdd1_3 = QtWidgets.QLineEdit(self.layoutWidget)
        self.recebeOdd1_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 3px;")
        self.recebeOdd1_3.setObjectName("recebeOdd1_3")
        self.gridLayout.addWidget(self.recebeOdd1_3, 2, 1, 1, 1)
        self.aposta2_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.aposta2_2.setFont(font)
        self.aposta2_2.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"border-radius: 1px;")
        self.aposta2_2.setAlignment(QtCore.Qt.AlignCenter)
        self.aposta2_2.setObjectName("aposta2_2")
        self.gridLayout.addWidget(self.aposta2_2, 2, 0, 1, 1)
        self.aposta2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.aposta2.setFont(font)
        self.aposta2.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"border-radius: 1px;")
        self.aposta2.setAlignment(QtCore.Qt.AlignCenter)
        self.aposta2.setObjectName("aposta2")
        self.gridLayout.addWidget(self.aposta2, 1, 0, 1, 1)
        self.aposta1 = QtWidgets.QLabel(self.layoutWidget)
        self.aposta1.setMinimumSize(QtCore.QSize(51, 20))
        self.aposta1.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.aposta1.setFont(font)
        self.aposta1.setStyleSheet("background-color: rgb(0, 85, 255);\n"
"border-radius: 1px;")
        self.aposta1.setAlignment(QtCore.Qt.AlignCenter)
        self.aposta1.setObjectName("aposta1")
        self.gridLayout.addWidget(self.aposta1, 0, 0, 1, 1)
        self.calcula = QtWidgets.QPushButton(self.layoutWidget)
        self.calcula.setStyleSheet("background-color: rgb(209, 209, 209);\n"
"")
        self.calcula.setObjectName("calcula")
        self.gridLayout.addWidget(self.calcula, 3, 0, 1, 2)
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(250, 190, 71, 23))
        self.exit.setStyleSheet("background-color: rgb(209, 209, 209);\n"
"border-radius: 3px;")
        self.exit.setObjectName("exit")
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
        self.calcula.clicked.connect(self.calculo)
    
    def calculo(self):
        odd1 = float(self.recebeOdd1.text())
        odd2 = float(self.recebeOdd1_2.text())
        aposta = float(self.recebeOdd1_3.text())
        L1 = []
        L2 = []
        L2.append(odd1)
        L2.append(odd2)
        L2.sort()
        porcentagem1 = L2[0]*(100/(odd1+odd2))
        porcentagem2 = L2[1]*(100/(odd1+odd2))
        L1.append(porcentagem1)
        L1.append(porcentagem2)
        aposta1 = aposta-(aposta*(porcentagem1/100))
        aposta2 = aposta-(aposta*(porcentagem2/100))
        lucro = ((aposta2*L2[1]-aposta)+(aposta1*L2[0]-aposta))/2
        porcentagemLucro = (lucro*100)/aposta
        msg = QMessageBox()
        msg.setWindowTitle("Resultado")
        msg.setText(f'''
        Odd {L2[1]}: Chance de vitória {porcentagem1:.2f}% | Valor a ser apostado R${aposta2:.2f}
        Odd {L2[0]}: Chance de vitória {porcentagem2:.2f}% | Valor a ser apostado R${aposta1:.2f}
        Lucro = R${lucro:.2f} | Porcentagem de Lucro = {porcentagemLucro:.2f}% ''')
        msg.exec()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculadora"))
        self.titulo.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">Digite as odds das apostas:</span></p></body></html>"))
        self.aposta2_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Valor:</span></p></body></html>"))
        self.aposta2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Odd 2:</span></p></body></html>"))
        self.aposta1.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Odd 1:</span></p></body></html>"))
        self.calcula.setText(_translate("MainWindow", "CALCULAR"))
        self.exit.setText(_translate("MainWindow", "SAIR"))
        self.action_Fechar.setText(_translate("MainWindow", "&Fechar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
