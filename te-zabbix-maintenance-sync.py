import requests

# Zabbix Config
ZBX_URL = "http://10.0.0.100/api_jsonrpc.php"
ZBX_TOKEN = "SEU_ZABBIX_API_TOKEN"

# ThousandEyes Config
TE_API_TOKEN = "SEU_TE_TOKEN"
TE_HEADERS = {"Authorization": f"Bearer {TE_API_TOKEN}", "Content-Type": "application/json"}

# Mapeamento estatico de ID do Host Zabbix para ID do Teste ThousandEyes
HOST_TO_TEST_MAP = {
    "10084": "112233", # Exemplo: HostID Zabbix -> TestID ThousandEyes
}

def sync_maintenance():
    # Consulta hosts em manutencao no Zabbix
    payload_zbx = {
        "jsonrpc": "2.0",
        "method": "host.get",
        "params": {
            "output": ["hostid", "maintenance_status"],
            "filter": {"maintenance_status": 1} # 1 = Em Manutencao
        },
        "auth": ZBX_TOKEN,
        "id": 1
    }
    
    hosts_in_maintenance = requests.post(ZBX_URL, json=payload_zbx).json().get('result', [])
    
    for host in hosts_in_maintenance:
        zbx_host_id = host['hostid']
        if zbx_host_id in HOST_TO_TEST_MAP:
            te_test_id = HOST_TO_TEST_MAP[zbx_host_id]
            
            # Desabilita o teste no ThousandEyes
            url_te = f"https://api.thousandeyes.com/v7/tests/http-server/{te_test_id}"
            requests.post(url_te, headers=TE_HEADERS, json={"enabled": 0})
            print(f"Teste {te_test_id} pausado no ThousandEyes (Host em manutencao no Zabbix)")

if __name__ == "__main__":
    sync_maintenance()