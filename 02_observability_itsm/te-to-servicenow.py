import requests
import json

TE_API_TOKEN = "SEU_TE_TOKEN"
SNOW_INSTANCE = "dev12345.service-now.com"
SNOW_USER = "admin"
SNOW_PASS = "sua_senha"

def create_snow_incident():
    # Busca alertas no ThousandEyes
    te_url = "https://api.thousandeyes.com/v7/alerts?state=ACTIVE"
    te_headers = {"Authorization": f"Bearer {TE_API_TOKEN}"}
    
    alerts = requests.get(te_url, headers=te_headers).json().get('alerts', [])
    
    for alert in alerts:
        # Cria o payload para o ServiceNow
        snow_url = f"https://{SNOW_INSTANCE}/api/now/table/incident"
        payload = {
            "short_description": f"ThousandEyes: Falha no {alert.get('testName')}",
            "description": f"Regra Violada: {alert.get('ruleName')}\nInicio: {alert.get('startDate')}",
            "assignment_group": "Network Support", # Fila da equipe de redes
            "urgency": "2",
            "impact": "2"
        }
        
        # Envia via POST para o ServiceNow (Basic Auth)
        snow_res = requests.post(snow_url, auth=(SNOW_USER, SNOW_PASS), json=payload)
        if snow_res.status_code == 201:
            inc_number = snow_res.json().get('result', {}).get('number')
            print(f"Incidente {inc_number} criado no ServiceNow com sucesso.")

if __name__ == "__main__":
    create_snow_incident()