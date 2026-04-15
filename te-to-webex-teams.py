import requests

TE_API_TOKEN = "SEU_TOKEN"
# Crie um Webhook no Webex App Hub para a sua sala de NOC
WEBEX_WEBHOOK_URL = "https://webexapis.com/v1/webhooks/incoming/SUA_CHAVE_AQUI"

def send_webex_alert():
    te_url = "https://api.thousandeyes.com/v7/alerts?state=ACTIVE"
    te_headers = {"Authorization": f"Bearer {TE_API_TOKEN}"}
    alerts = requests.get(te_url, headers=te_headers).json().get('alerts', [])
    
    for alert in alerts:
        # Formata a mensagem usando Markdown nativo do Webex
        markdown_text = f"**🚨 Alerta ThousandEyes Ativo**\n" \
                        f"- **Teste:** {alert.get('testName')}\n" \
                        f"- **Regra Violada:** {alert.get('ruleName')}\n" \
                        f"- **Severidade:** Alta\n" \
                        f"*[Verifique o painel para mais detalhes]*"
                        
        payload = {"markdown": markdown_text}
        
        requests.post(WEBEX_WEBHOOK_URL, json=payload)
        print(f"Notificação Webex enviada para o teste {alert.get('testName')}")

if __name__ == "__main__":
    send_webex_alert()