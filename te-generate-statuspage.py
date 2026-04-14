import requests

TE_API_TOKEN = "SEU_TOKEN"
HEADERS = {"Authorization": f"Bearer {TE_API_TOKEN}"}
URL = "https://api.thousandeyes.com/v7/alerts?state=ACTIVE"

def generate_html():
    res = requests.get(URL, headers=HEADERS)
    alerts = res.json().get('alerts', [])
    
    cor_fundo = "#e74c3c" if alerts else "#2ecc71"
    status_texto = "Problemas Detectados" if alerts else "Todos os Sistemas Operacionais"
    
    html = f"""
    <html><head><title>Status da Rede</title></head>
    <body style="font-family: Arial; text-align: center; padding: 50px; background-color: {cor_fundo}; color: white;">
        <h1>Status: {status_texto}</h1>
        <p>Verificado pela plataforma ThousandEyes</p>
    </body></html>
    """
    
    with open("status.html", "w") as f:
        f.write(html)
    print("Pagina de status atualizada (status.html).")

if __name__ == "__main__":
    generate_html()