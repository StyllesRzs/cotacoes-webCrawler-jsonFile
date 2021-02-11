import requests
from bs4 import BeautifulSoup as bs
import json


'''
--- DOLAR ---
'''

req = requests.get('https://www.remessaonline.com.br/cotacao/cotacao-dolar')
content = req.text

soup = bs(content, 'html.parser')


#buscando o dolar com a var soup
dolar = soup.find('div', {'class': 'style__Text-sc-15flwue-2 cSuXFv'}).text[0:4]
#substituindo a ',' para '.'
dolar = dolar.replace(',', '.')
#transformando o dolar em float, para pegar os centavos
dolar = float(dolar)
#arredondando os digitos para casas decimais
dolar = round(dolar, 2)
print('Dolar:', dolar)  

'''
---- EURO ---
'''
req = requests.get('https://www.remessaonline.com.br/cotacao/cotacao-euro')

content = req.text

soup = bs(content, 'html.parser')

euro = soup.find('div', {'class': 'style__Text-sc-15flwue-2 cSuXFv'}).text[0:4]
euro = euro.replace(',', '.')
euro = float(euro)
euro = round(euro, 2)

print('Euro:', euro)  

'''
--- LIBRA ESTERLINA---
'''

req = requests.get('https://www.remessaonline.com.br/cotacao/cotacao-libra-esterlina')

content = req.text
soup = bs(content, 'html.parser')

libraEsterlina = soup.find('div', {'class': 'style__Text-sc-15flwue-2 cSuXFv'}).text[0:4]

libraEsterlina = libraEsterlina.replace(',', '.')
libraEsterlina = float(libraEsterlina)
libraEsterlina = round(libraEsterlina, 2)

print('Libra Esterlina:',  libraEsterlina)

'''
--- DOLAR CANADENSE ---
'''

req = requests.get('https://www.remessaonline.com.br/cotacao/cotacao-dolar-canadense')
content = req.text
soup = bs(content, 'html.parser')

dolarCanadense = soup.find('div', {'class': 'style__Text-sc-15flwue-2 cSuXFv'}).text[0:4]
dolarCanadense = dolarCanadense.replace(',', '.')
dolarCanadense = float(dolarCanadense)
dolarCanadense = round(dolarCanadense, 2)

print('Dolar Canadense:', dolarCanadense)


dados = {
    'cotacaoDolar': dolar,
    'cotacaoEuro': euro,
    'cotacaoLibraEsterlina': libraEsterlina,
    'cotacaoDolarCanadense': dolarCanadense

}

with open('.\webCrawlers\cotacao.json', 'w') as json_file:
    json.dump(dados, json_file, indent=4)




