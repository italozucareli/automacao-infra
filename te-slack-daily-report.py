import requests

SLACK_WEBHOOK = "https://hooks.slack.com/services/..."
TE_TOKEN = "SEU_TOKEN"

def send_daily_digest():
    # Busca testes de rede
    url = "https://api.thousandeyes.com/v7/tests"
    headers = {"Authorization": f"Bearer {TE_TOKEN}"}
    tests = requests.get(url, headers=headers).json().get('tests', [])

    report = "*📊 Resumo Diário ThousandEyes*\n"
    for t in tests[:5]: # Top 5 testes
        report += f"• *{t['testName']}*: Operacional\n"

    requests.post(SLACK_WEBHOOK, json={"text": report})

if __name__ == "__main__":
    send_daily_digest()