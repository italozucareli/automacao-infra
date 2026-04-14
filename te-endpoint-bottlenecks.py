import requests

TE_API_TOKEN = "SEU_TOKEN"
HEADERS = {"Authorization": f"Bearer {TE_API_TOKEN}"}
URL = "https://api.thousandeyes.com/v7/endpoint/system/metrics"

def check_device_health():
    res = requests.get(URL, headers=HEADERS)
    data = res.json().get('systemMetrics', [])
    
    print("--- Auditoria de Saude dos Computadores ---")
    for device in data:
        cpu = device.get('cpuLoad', 0)
        if cpu > 85:
            nome = device.get('agentName', 'Desconhecido')
            print(f"⚠️ Atenção: PC de {nome} esta com gargalo (CPU: {cpu}%)")

if __name__ == "__main__":
    check_device_health()