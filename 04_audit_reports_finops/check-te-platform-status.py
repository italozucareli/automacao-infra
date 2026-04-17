import requests

# API publica da pagina de status da ThousandEyes
STATUS_API = "https://status.thousandeyes.com/api/v2/status.json"

def check_platform_health():
    try:
        res = requests.get(STATUS_API)
        res.raise_for_status()
        data = res.json()
        
        status_geral = data.get('status', {}).get('description', 'Desconhecido')
        indicador = data.get('status', {}).get('indicator', 'none')
        
        if indicador == "none":
            print(f"✅ Plataforma ThousandEyes 100% Operacional. (Status: {status_geral})")
        else:
            print(f"⚠️ ATEÇÃO! A ThousandEyes está reportando instabilidade: {status_geral}")
            
    except Exception as e:
        print(f"Não foi possível checar o status da ThousandEyes: {e}")

if __name__ == "__main__":
    check_platform_health()