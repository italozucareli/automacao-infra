import requests
import json

# ==============================================================================
# Script ChatOps: Envia Alertas Ativos para o Microsoft Teams
# ==============================================================================

TE_API_TOKEN = "SEU_OAUTH_TOKEN"
TE_HEADERS = {"Authorization": f"Bearer {TE_API_TOKEN}"}
TE_URL = "https://api.thousandeyes.com/v7/alerts?state=ACTIVE"

# Webhook gerado no canal do MS Teams (Incoming Webhook)
TEAMS_WEBHOOK_URL = "https://sua-empresa.webhook.office.com/webhookb2/..."

def send_to_teams(alert_name, test_name, date_start):
    payload = {
        "@type": "MessageCard",
        "@context": "http://schema.org/extensions",
        "themeColor": "E81123",
        "summary": "Incidente de Rede - ThousandEyes",
        "sections": [{
            "activityTitle": "🚨 Novo Alerta no ThousandEyes",
            "facts": [
                {"name": "Regra Violada:", "value": alert_name},
                {"name": "Teste Afetado:", "value": test_name},
                {"name": "Início do Evento:", "value": date_start}
            ],
            "markdown": True
        }]
    }
    requests.post(TEAMS_WEBHOOK_URL, json=payload)

def check_and_notify():
    try:
        res = requests.get(TE_URL, headers=TE_HEADERS)
        res.raise_for_status()
        alerts = res.json().get('alerts', [])
        
        for alert in alerts:
            send_to_teams(alert.get('ruleName'), alert.get('testName'), alert.get('startDate'))
            print(f"Notificacao enviada ao Teams para o teste: {alert.get('testName')}")
            
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    check_and_notify()