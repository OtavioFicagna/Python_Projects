import requests

def converter(rcb_Dolar, rcb_Real):
    #Pega a cotação atual do Dolar
    cotacao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
    cotacao_dic = cotacao.json()
    valorCotacao = float(cotacao_dic['USDBRL']['bid'])
    
    #Converte
    valorReal = rcb_Dolar*valorCotacao
    valorDolar = rcb_Real/valorCotacao
    
    print(valorReal, valorDolar)

rcb_Dolar = 5
rcb_Real = 50
converter(rcb_Dolar, rcb_Real)
    