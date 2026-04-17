import requests
import json
import sys

# =========================================================
# Script para Zabbix LLD (Discovery) de Testes ThousandEyes
# Em vez de cadastrar manualmente cada teste no Zabbix, este script faz o LLD. 
# Ele varre sua conta do ThousandEyes e entrega um JSON formatado para que o Zabbix crie automaticamente um "Item" e uma "Trigger" para cada teste ativo.
# Aplicação: Automação completa de monitoramento. Se você criar um novo teste no portal ThousandEyes, ele aparece no Zabbix automaticamente.
# =========================================================

TE_API_TOKEN = "SEU_OAUTH_TOKEN"
HEADERS = {"Authorization": f"Bearer {TE_API_TOKEN}"}
URL = "https://api.thousandeyes.com/v7/tests"

def discover_tests():
    try:
        response = requests.get(URL, headers=HEADERS, timeout=10)
        response.raise_for_status()
        tests = response.json().get('tests', [])

        lld_data = []
        for test in tests:
            # Filtra apenas testes ativos e de rede/http
            if test.get('enabled') == 1:
                lld_data.append({
                    "{#TE_TEST_ID}": str(test.get('testId')),
                    "{#TE_TEST_NAME}": test.get('testName'),
                    "{#TE_TEST_TYPE}": test.get('type')
                })

        # Formato exigido pelo Zabbix LLD
        print(json.dumps({"data": lld_data}))

    except Exception as e:
        print(json.dumps({"error": str(e)}))

if __name__ == "__main__":
    discover_tests()