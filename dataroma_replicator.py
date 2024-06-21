# @sulfuroid 
# Script to suck https://www.dataroma.com/m/managers.php and isolate assets per line
# Can be used to replicate into your own portfolio

import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
import csv

# URL de la page contenant les données des gestionnaires de portefeuille
url = 'https://www.dataroma.com/m/managers.php'

# En-têtes HTTP pour simuler un navigateur web
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

# Récupérer le contenu de la page
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# Trouver le tableau contenant les données des gestionnaires de portefeuille
table = soup.find('table', {'id': 'grid'})

if table is None:
    raise ValueError("Table with id 'grid' not found on the page.")

# Extraire les en-têtes du tableau
headers = ["Portfolio Manager - Firm", "Portfolio value", "No. of stocks"] + [f"Top {i+1} holding" for i in range(10)]

# Extraire les données du tableau
rows = []
for row in table.find_all('tr')[1:]:
    cols = row.find_all('td')
    if len(cols) > 2:  # Pour s'assurer qu'il y a des colonnes à extraire
        manager_firm = cols[0].text.strip()
        portfolio_value = cols[1].text.strip()
        num_stocks = cols[2].text.strip()
        top_holdings = [holding.text.strip() for holding in cols[3:13]]
        rows.append([manager_firm, portfolio_value, num_stocks] + top_holdings)

# Afficher les données avec tabulate
print(tabulate(rows, headers=headers, tablefmt='grid'))

# Sauvegarder les données dans un fichier CSV
with open('portfolio_managers.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(headers)
    writer.writerows(rows)
