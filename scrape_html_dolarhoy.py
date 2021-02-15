import requests
from bs4 import BeautifulSoup
import pprint # solo para presentar la info del dictionary resultado en el terminal

# resDolarHoy = requests.get('https://www.dolarhoy.com/')
resDolarOficial = requests.get('https://www.dolarhoy.com/cotizaciondolaroficial')
resDolarBlue = requests.get('https://www.dolarhoy.com/cotizaciondolarblue')

# soupDolarHoy = BeautifulSoup(resDolarHoy.text, 'html.parser')
soupDolarOficial = BeautifulSoup(resDolarOficial.text, 'html.parser')
soupDolarBlue = BeautifulSoup(resDolarBlue.text, 'html.parser')
message = ''

# print('***** Dolar Oficial *****')
# for info in soupDolarOficial.select('.pull-left'):
#     print(info.text)
# print('***** Dolar Blue *****')
# for info in soupDolarBlue.select('.pull-left'):
#     print(info.text)

# soupDolarOficial.find_all(attrs={"class": "topic"})
# soupDolarOficial.find_all(attrs={"class": "value"})



message = f"{message} Dolar Oficial:"
oficialCompraTitulo = soupDolarOficial.find_all(attrs={"class": "topic"})[0]
oficialCompraValor = soupDolarOficial.find_all(attrs={"class": "value"})[0]
message = f"{message}\n-----------------------\n{oficialCompraTitulo}\n{oficialCompraValor}\n"
oficialCompraTitulo = soupDolarOficial.find_all(attrs={"class": "topic"})[1]
oficialCompraValor = soupDolarOficial.find_all(attrs={"class": "value"})[1]
message = f"{message}\n-----------------------\n{oficialCompraTitulo}\n{oficialCompraValor}\n"

# for info in soupDolarOficial.select('.pull-left'):
#     message = message + ' | ' + info.text
    
message = f'{message}\nDolar Blue'
blueCompraTitulo = soupDolarBlue.find_all(attrs={"class": "topic"})[0]
blueCompraValor = soupDolarBlue.find_all(attrs={"class": "value"})[0]
message = f"{message}\n-----------------------\n{blueCompraTitulo}\n{blueCompraValor}\n"
blueCompraTitulo = soupDolarBlue.find_all(attrs={"class": "topic"})[1]
blueCompraValor = soupDolarBlue.find_all(attrs={"class": "value"})[1]
message = f"{message}\n-----------------------\n{blueCompraTitulo}\n{blueCompraValor}\n"
    # for info in soupDolarBlue.select('.pull-left'):
    #     message = message + ' | ' + info.text

def getDolarCurrentQuote():
    return message