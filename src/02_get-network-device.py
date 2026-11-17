import json
import requests
from config import BASE_URL, NRO_TICKET
api_url = f"{BASE_URL}/network-device"

headers = {"X-Auth-Token": NRO_TICKET}

resp = requests.get(api_url, headers=headers)

print("Request status: ", resp.status_code)

response_json = resp.json()
print()
print()
print (response_json)
print()
print()
networkDevices = response_json["response"]

for networkDevice in networkDevices:
    if networkDevice.get('hostname', None):
        print(networkDevice["hostname"], "\t", networkDevice["platformId"], "\t", networkDevice["managementIpAddress"])
