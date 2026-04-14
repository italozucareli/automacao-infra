import requests
import json
from datetime import datetime

# ==============================================================================
# Script de Backup das Configuracoes de Testes do ThousandEyes
# ==============================================================================

TE_API_TOKEN = "SEU_OAUTH_TOKEN"
HEADERS = {"Authorization": f"Bearer {TE_API_TOKEN}"}
URL = "https://api.thousandeyes.com/v7/tests"

def backup_tests():
    data_atual = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"te_backup_tests_{data_atual}.json"
    
    try:
        print("Iniciando download das configuracoes de testes...")
        response = requests.get(URL, headers=HEADERS, timeout=15)
        response.raise_for_status()
        
        testes = response.json()
        
        with open(filename, 'w') as f:
            json.dump(testes, f, indent=4)
            
        print(f"Backup concluido com sucesso! Salvo em: {filename}")
        
    except Exception as e:
        print(f"Erro ao realizar o backup: {e}")

if __name__ == "__main__":
    backup_tests()