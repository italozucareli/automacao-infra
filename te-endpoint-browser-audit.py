import requests

TE_TOKEN = "SEU_TOKEN"
HEADERS = {"Authorization": f"Bearer {TE_TOKEN}"}
URL = "https://api.thousandeyes.com/v7/endpoint/test-results/browser-sessions"

def audit_outdated_browsers():
    sessions = requests.get(URL, headers=HEADERS).json().get('browserSessions', [])
    
    print("🛡️ Auditoria de Segurança de Navegadores (Endpoints)")
    for session in sessions:
        agent = session.get('agentName')
        browser_info = session.get('browser', '') # Retorna ex: "Chrome 112"
        
        # Lógica simples: Se for versão antiga do Chrome (ex: abaixo de 115)
        if "Chrome" in browser_info:
            versao = int(browser_info.split()[1].split('.')[0])
            if versao < 115:
                print(f"⛔ VULNERÁVEL: Computador de {agent} usando {browser_info} (Atualização necessária)")

if __name__ == "__main__":
    audit_outdated_browsers()