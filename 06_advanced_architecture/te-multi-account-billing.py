import requests

TE_TOKEN = "SEU_TOKEN"
HEADERS = {"Authorization": f"Bearer {TE_TOKEN}"}
URL_ACCOUNTS = "https://api.thousandeyes.com/v7/account-groups"

def report_multi_account_billing():
    print("📊 Relatório de Consumo por Centro de Custo (Account Groups)\n")
    
    accounts = requests.get(URL_ACCOUNTS, headers=HEADERS).json().get('accountGroups', [])
    
    total_geral = 0
    for acc in accounts:
        aid = acc['aid']
        name = acc['accountGroupName']
        
        # Passa o parametro aid na URL para consultar o contexto daquela subconta
        url_usage = f"https://api.thousandeyes.com/v7/usage?aid={aid}"
        usage_data = requests.get(url_usage, headers=HEADERS).json().get('usage', {})
        
        used = usage_data.get('used', 0)
        total_geral += used
        
        print(f"🏢 Conta: {name.ljust(25)} | Consumo: {used} Units")
        
    print("-" * 50)
    print(f"💰 TOTAL GERAL DA FATURA: {total_geral} Units")

if __name__ == "__main__":
    report_multi_account_billing()