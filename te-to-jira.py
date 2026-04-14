import requests
from requests.auth import HTTPBasicAuth

TE_API_TOKEN = "SEU_TE_TOKEN"
JIRA_URL = "https://suaempresa.atlassian.net/rest/api/2/issue"
JIRA_USER = "seu_email@empresa.com"
JIRA_TOKEN = "SEU_JIRA_API_TOKEN"

def create_jira_bug(test_name, rule_name):
    payload = {
        "fields": {
            "project": {"key": "ITOP"}, # Chave do Projeto no Jira
            "summary": f"[ThousandEyes] Degradação em: {test_name}",
            "description": f"Alerta ativo detectado.\nRegra: {rule_name}\nPor favor, investigar logs da aplicação.",
            "issuetype": {"name": "Bug"}
        }
    }
    
    auth = HTTPBasicAuth(JIRA_USER, JIRA_TOKEN)
    res = requests.post(JIRA_URL, json=payload, auth=auth)
    
    if res.status_code == 201:
        print(f"Bug criado no Jira: {res.json().get('key')}")

# Lógica simplificada: você chamaria a API do TE e passaria os dados para a função acima.
if __name__ == "__main__":
    create_jira_bug("Portal do Cliente", "Tempo de Resposta > 2000ms")