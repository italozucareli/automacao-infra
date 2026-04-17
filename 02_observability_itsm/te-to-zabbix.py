import requests
import subprocess
import json

# ==============================================================================
# Script de Integracao: Envia Alertas do ThousandEyes para o Zabbix
# ==============================================================================

TE_API_TOKEN = "SEU_OAUTH_BEARER_TOKEN"
ZABBIX_SERVER = "10.0.0.100" # IP do seu servidor Zabbix
ZABBIX_HOST = "ThousandEyes_API" # Nome do Host cadastrado no Zabbix

HEADERS = {
    "Authorization": f"Bearer {TE_API_TOKEN}",
    "Content-Type": "application/json"
}
URL = "https://api.thousandeyes.com/v7/alerts?state=ACTIVE"

def send_to_zabbix(key, value):
    """Usa o binario zabbix_sender do SO para enviar a metrica"""
    cmd = [
        "zabbix_sender",
        "-z", ZABBIX_SERVER,
        "-s", ZABBIX_HOST,
        "-k", key,
        "-o", str(value)
    ]
    try:
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL)
    except subprocess.CalledProcessError as e:
        print(f"Erro ao enviar para o Zabbix: {e}")

def process_alerts():
    try:
        response = requests.get(URL, headers=HEADERS, timeout=10)
        response.raise_for_status()
        alerts = response.json().get('alerts', [])
        
        # Envia a contagem total de alertas ativos para uma trigger principal no Zabbix
        total_alerts = len(alerts)
        send_to_zabbix("te.alerts.total", total_alerts)
        
        print(f"Sucesso: {total_alerts} alertas reportados ao Zabbix.")
        
    except Exception as e:
        print(f"Falha na integracao: {e}")

if __name__ == "__main__":
    process_alerts()