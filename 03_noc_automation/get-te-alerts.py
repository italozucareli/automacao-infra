import requests
import json

# ==============================================================================
# Script de Consulta de Alertas Ativos - API ThousandEyes v7
# ==============================================================================

# Insira o seu token de API gerado no portal
API_TOKEN = "COLE_SEU_OAUTH_BEARER_TOKEN_AQUI"
HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

# URL da API v7 para buscar alertas ativos (estado = ACTIVE)
URL = "https://api.thousandeyes.com/v7/alerts?state=ACTIVE"

def get_active_alerts():
    print("Consultando alertas ativos no ThousandEyes...\n")
    try:
        response = requests.get(URL, headers=HEADERS, timeout=10)
        response.raise_for_status()  # Verifica se houve erro HTTP
        
        data = response.json()
        alerts = data.get('alerts', [])
        
        if not alerts:
            print("Nenhum alerta ativo no momento. A rede esta estavel.")
            return

        print(f"Foram encontrados {len(alerts)} alertas ativos:")
        print("-" * 50)
        
        for alert in alerts:
            test_name = alert.get('testName', 'Teste Desconhecido')
            rule_name = alert.get('ruleName', 'Regra Desconhecida')
            date_start = alert.get('startDate', 'Data Indisponível')
            
            print(f"[!] Teste Afetado: {test_name}")
            print(f"    Regra Violada: {rule_name}")
            print(f"    Inicio do Alerta: {date_start}")
            print("-" * 50)

    except requests.exceptions.RequestException as e:
        print(f"Erro ao conectar na API do ThousandEyes: {e}")

if __name__ == "__main__":
    get_active_alerts()