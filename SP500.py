# @Sulfuroid 2024
# This Python script gets the list of SP500 Symboles from wikipedia
# GPL 3
import requests
from bs4 import BeautifulSoup

# URL de la page Wikipedia contenant la liste des entreprises du S&P 500
url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

# Récupérer le contenu de la page
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Trouver le tableau contenant la liste des entreprises
table = soup.find('table', {'class': 'wikitable sortable'})

# Extraire les symboles boursiers
tickers = []
for row in table.find_all('tr')[1:]:
    ticker = row.find_all('td')[0].text.strip()
    tickers.append(ticker)

# Afficher la liste des symboles boursiers
print(tickers)
