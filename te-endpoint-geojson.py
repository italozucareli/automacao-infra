import requests
import json

TE_API_TOKEN = "SEU_TOKEN"
HEADERS = {"Authorization": f"Bearer {TE_API_TOKEN}"}
URL = "https://api.thousandeyes.com/v7/endpoint/agents"

def export_to_geojson():
    res = requests.get(URL, headers=HEADERS).json()
    agents = res.get('agents', [])
    
    features = []
    for agent in agents:
        location = agent.get('location', {})
        lat = location.get('latitude')
        lon = location.get('longitude')
        
        if lat and lon:
            features.append({
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [lon, lat] # GeoJSON usa Longitude, Latitude
                },
                "properties": {
                    "agentName": agent.get('agentName'),
                    "status": agent.get('state'),
                    "platform": agent.get('platform')
                }
            })
            
    geojson = {
        "type": "FeatureCollection",
        "features": features
    }
    
    with open("te_endpoints_map.json", "w") as f:
        json.dump(geojson, f, indent=2)
        
    print("Mapa GeoJSON atualizado: te_endpoints_map.json")

if __name__ == "__main__":
    export_to_geojson()