import boto3
import requests
import os

def lambda_handler(event, context):
    te_token = os.environ['TE_TOKEN']
    test_id = os.environ['TEST_ID']
    
    headers = {"Authorization": f"Bearer {te_token}"}
    url = f"https://api.thousandeyes.com/v7/net/metrics/{test_id}"
    
    res = requests.get(url, headers=headers).json()
    cloudwatch = boto3.client('cloudwatch')

    for result in res.get('results', []):
        cloudwatch.put_metric_data(
            Namespace='ThousandEyes/Network',
            MetricData=[{
                'MetricName': 'AvgLatency',
                'Dimensions': [{'Name': 'Agent', 'Value': result['agent']['agentName']}],
                'Value': result['avgLatency'],
                'Unit': 'Milliseconds'
            }]
        )
    return {"status": "Metrics sent to CloudWatch"}