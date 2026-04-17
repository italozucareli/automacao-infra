import requests

TE_TOKEN = "SEU_TOKEN"
HEADERS = {"Authorization": f"Bearer {TE_TOKEN}", "Content-Type": "application/json"}
WEBHOOK_ID = "SEU_WEBHOOK_INTEGRATION_ID"

def apply_webhook_to_all_rules():
    url_rules = "https://api.thousandeyes.com/v7/alerts/rules"
    rules = requests.get(url_rules, headers=HEADERS).json().get('alertRules', [])
    
    for rule in rules:
        rule_id = rule['ruleId']
        integrations = rule.get('integrationIds', [])
        
        if WEBHOOK_ID not in integrations:
            integrations.append(WEBHOOK_ID)
            
            # Atualiza a regra via POST
            update_url = f"{url_rules}/{rule_id}"
            payload = {"integrationIds": integrations}
            requests.post(update_url, headers=HEADERS, json=payload)
            print(f"Webhook associado à regra: {rule['ruleName']}")

if __name__ == "__main__":
    apply_webhook_to_all_rules()