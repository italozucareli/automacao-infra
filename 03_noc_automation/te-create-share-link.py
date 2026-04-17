import requests
import json

TE_API_TOKEN = "SEU_TOKEN"
HEADERS = {"Authorization": f"Bearer {TE_API_TOKEN}", "Content-Type": "application/json"}
URL = "https://api.thousandeyes.com/v7/shares"

def create_isp_evidence(test_id):
    # Compartilha os dados das ultimas 4 horas
    payload = {
        "testId": test_id,
        "timeSpan": 14400 
    }
    res = requests.post(URL, headers=HEADERS, json=payload)
    if res.status_code == 201:
        share_link = res.json().get('shareUrl')
        print(f"Envie este link para o provedor analisar o problema: {share_link}")
    else:
        print("Erro ao gerar link de compartilhamento.")

if __name__ == "__main__":
    create_isp_evidence("112233")