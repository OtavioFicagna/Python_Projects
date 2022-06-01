import requests
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

def converter(rcb_Real, rcb_Dolar):
    valorReal = float(rcb_Real)
    valorDolar = float(rcb_Dolar)
    #Pega a cotação atual do Dolar
    cotacao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
    cotacao_dic = cotacao.json()
    valorCotacao = float(cotacao_dic['USDBRL']['bid'])
    #Converte
        
        
    #Abre a janela com os valores
    msg = QMessageBox()
    msg.setWindowTitle("Resultado")
    msg.setText(f'''
    Cotação atual do Dólar: US${valor_Cotacao} ''')
    msg.exec()
rcb_Real = 10
rcb_Dolar = 10
converter(rcb_Real, rcb_Dolar)