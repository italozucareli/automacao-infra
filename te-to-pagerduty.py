import requests
import json

# Configurações
TE_API_TOKEN = "SEU_TE_TOKEN"
PD_ROUTING_KEY = "SUA_INTEGRATION_KEY_PAGERDUTY"

def trigger_pd_incident():
    # 1. Busca alertas ativos no ThousandEyes
    te_url = "https://api.thousandeyes.com/v7/alerts?state=ACTIVE"
    te_headers = {"Authorization": f"Bearer {TE_API_TOKEN}"}
    alerts = requests.get(te_url, headers=te_headers).json().get('alerts', [])

    for alert in alerts:
        # 2. Envia para o PagerDuty Events API
        pd_url = "https://events.pagerduty.com/v2/enqueue"
        payload = {
            "routing_key": PD_ROUTING_KEY,
            "event_action": "trigger",
            "payload": {
                "summary": f"Falha de Rede: {alert.get('testName')}",
                "source": "ThousandEyes",
                "severity": "critical",
                "custom_details": {
                    "rule": alert.get('ruleName'),
                    "metrics": alert.get('metrics')
                }
            }
        }
        requests.post(pd_url, json=payload)

if __name__ == "__main__":
    trigger_pd_incident()