import requests

TE_API_TOKEN = "SEU_TOKEN"
HEADERS = {"Authorization": f"Bearer {TE_API_TOKEN}"}

def bulk_delete(file_path):
    with open(file_path, 'r') as file:
        test_ids = file.read().splitlines()

    for test_id in test_ids:
        if not test_id.strip(): continue
        
        url = f"https://api.thousandeyes.com/v7/tests/{test_id}"
        res = requests.delete(url, headers=HEADERS)
        
        if res.status_code == 204: # 204 No Content = Sucesso no DELETE
            print(f"Teste {test_id} excluido com sucesso.")
        else:
            print(f"Falha ao excluir teste {test_id}: {res.status_code}")

if __name__ == "__main__":
    # Crie um arquivo txt chamado 'testes_para_apagar.txt' com um ID por linha
    bulk_delete("testes_para_apagar.txt")