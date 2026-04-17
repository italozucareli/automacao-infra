import requests

TE_API_TOKEN = "SEU_TOKEN"
HEADERS = {"Authorization": f"Bearer {TE_API_TOKEN}", "Content-Type": "application/json"}
TEST_ID = "55555"

def update_test_target(new_ip_or_url):
    url = f"https://api.thousandeyes.com/v7/tests/http-server/{TEST_ID}"
    payload = {"url": new_ip_or_url}
    
    res = requests.post(url, headers=HEADERS, json=payload) # POST e usado para update no TE
    if res.status_code == 200:
        print(f"Destino do teste atualizado para: {new_ip_or_url}")
    else:
        print("Falha ao atualizar alvo.")

if __name__ == "__main__":
    update_test_target("https://backup-site.minhaempresa.com")