import requests

TE_API_TOKEN = "SEU_TOKEN"
HEADERS = {"Authorization": f"Bearer {TE_API_TOKEN}"}
URL = "https://api.thousandeyes.com/v7/usage"

def check_billing_quota():
    res = requests.get(URL, headers=HEADERS)
    data = res.json().get('usage', {})
    
    quota = data.get('quota', 1)
    used = data.get('used', 0)
    percent = (used / quota) * 100
    
    print(f"Consumo do Mes: {used} de {quota} Units ({percent:.1f}%)")
    if percent > 80:
        print("ALERTA CRÍTICO: Você consumiu mais de 80% da sua cota de monitoramento!")

if __name__ == "__main__":
    check_billing_quota()