import requests
from bs4 import BeautifulSoup

# URL de la page Wikipedia contenant la liste des entreprises du NASDAQ-100
url = 'https://en.wikipedia.org/wiki/NASDAQ-100'

# Récupérer le contenu de la page
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Trouver le tableau contenant la liste des entreprises
table = soup.find('table', {'class': 'wikitable sortable'})

# Extraire les symboles boursiers
tickers = []
for row in table.find_all('tr')[1:]:
    ticker = row.find_all('td')[1].text.strip()  # La colonne des tickers est la deuxième colonne dans ce tableau
    tickers.append(ticker)

# Afficher la liste des symboles boursiers
print(tickers)
