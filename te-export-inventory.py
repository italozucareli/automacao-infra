import requests
import csv
from datetime import datetime

TE_API_TOKEN = "SEU_TOKEN"
HEADERS = {"Authorization": f"Bearer {TE_API_TOKEN}"}
URL = "https://api.thousandeyes.com/v7/tests"

def export_to_csv():
    res = requests.get(URL, headers=HEADERS)
    tests = res.json().get('tests', [])
    filename = f"te_inventory_{datetime.now().strftime('%Y%m%d')}.csv"
    
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["ID do Teste", "Nome do Teste", "Tipo", "Habilitado", "Intervalo (s)"])
        
        for t in tests:
            writer.writerow([t['testId'], t['testName'], t['type'], t['enabled'], t['interval']])
            
    print(f"Sucesso! {len(tests)} testes exportados para {filename}")

if __name__ == "__main__":
    export_to_csv()