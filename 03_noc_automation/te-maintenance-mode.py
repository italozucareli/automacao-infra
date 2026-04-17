import requests
import argparse

# ==============================================================================
# Script Operacional: Pausa/Retoma Testes durante Janelas de Manutencao
# ==============================================================================

TE_API_TOKEN = "SEU_OAUTH_TOKEN"
HEADERS = {
    "Authorization": f"Bearer {TE_API_TOKEN}",
    "Content-Type": "application/json"
}
TEST_ID = "123456" # ID do teste que sofrera manutencao
URL_UPDATE = f"https://api.thousandeyes.com/v7/tests/{TEST_ID}"

def change_test_state(enabled: bool):
    payload = {"enabled": 1 if enabled else 0}
    
    try:
        response = requests.post(URL_UPDATE, headers=HEADERS, json=payload, timeout=10)
        response.raise_for_status()
        
        estado = "ATIVADO" if enabled else "PAUSADO"
        print(f"Sucesso: O teste {TEST_ID} foi {estado}.")
        
    except requests.exceptions.RequestException as e:
        print(f"Falha ao alterar o estado do teste: {e}")

if __name__ == "__main__":
    # Permite rodar no terminal passando o argumento --enable ou --disable
    parser = argparse.ArgumentParser(description="Coloca o teste em modo manutencao.")
    parser.add_argument("--action", choices=['enable', 'disable'], required=True)
    args = parser.parse_args()

    if args.action == 'enable':
        change_test_state(True)
    else:
        change_test_state(False)