import requests

TE_API_TOKEN = "SEU_TOKEN"
HEADERS = {"Authorization": f"Bearer {TE_API_TOKEN}", "Content-Type": "application/json"}
URL_TESTS = "https://api.thousandeyes.com/v7/tests"
URL_LABELS = "https://api.thousandeyes.com/v7/groups/tests"

def auto_tag_tests():
    # 1. Busca todos os testes
    tests = requests.get(URL_TESTS, headers=HEADERS).json().get('tests', [])
    
    finance_test_ids = []
    for t in tests:
        if "Banco" in t.get('testName', '') or "Pagamento" in t.get('testName', ''):
            finance_test_ids.append({"testId": t.get('testId')})
            
    if finance_test_ids:
        # 2. Associa esses testes a um Grupo/Label Especifico (Exemplo: Grupo ID 101)
        # Nota: O ID do grupo precisa existir previamente no portal
        LABEL_ID = "101" 
        payload = {"tests": finance_test_ids}
        
        # O Endpoint usa POST com a string '/update' no final para alterar labels
        res = requests.post(f"{URL_LABELS}/{LABEL_ID}/update", headers=HEADERS, json=payload)
        
        if res.status_code == 200:
            print(f"Sucesso! Label aplicada a {len(finance_test_ids)} testes financeiros.")
        else:
            print("Falha ao aplicar labels.")

if __name__ == "__main__":
    auto_tag_tests()