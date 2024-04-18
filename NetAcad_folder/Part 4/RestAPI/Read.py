import requests
import json
 
router_ip = '192.168.56.101'
username = 'cisco'
password = 'cisco123!'
 
interface_name = 'Loopback14'
 
url = f"https://{router_ip}/restconf/data/ietf-interfaces:interfaces/interface={interface_name}"
 
headers = {
    'Content-Type': 'application/yang-data+json',
    'Accept': 'application/yang-data+json',
}
 
response = requests.get(url, headers=headers, auth=(username, password), verify=False)
 
if response.status_code == 200:
    interface_config = response.json()
    print(json.dumps(interface_config, indent=4))
else:
    print(f"Failed to read loopback interface configuration. Status code: {response.status_code}")