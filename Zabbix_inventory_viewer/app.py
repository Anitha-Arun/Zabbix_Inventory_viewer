from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

ZABBIX_URL = 'http://zabbix_url/zabbix/api_jsonrpc.php'
USERNAME = 'Admin'
PASSWORD = 'please give password'
TARGET_GROUPS = ["Manual", "Longhaul", "Automation", "Inventory", "DM Team"]

def get_auth_token():
    payload = {
        "jsonrpc": "2.0",
        "method": "user.login",
        "params": {"username": USERNAME, "password": PASSWORD},
        "id": 1
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(ZABBIX_URL, data=json.dumps(payload), headers=headers)
    return response.json().get("result", None)

def get_host_groups(auth_token):
    payload = {
        "jsonrpc": "2.0",
        "method": "hostgroup.get",
        "params": {"output": "extend"},
        "auth": auth_token,
        "id": 2
    }
    response = requests.post(ZABBIX_URL, json=payload)
    groups = response.json().get("result", [])
    return {g["name"]: g["groupid"] for g in groups if g["name"] in TARGET_GROUPS}

def get_hosts_by_group(auth_token, group_id):
    payload = {
        "jsonrpc": "2.0",
        "method": "host.get",
        "params": {
            "output": ["hostid", "host", "name"],
            "selectInventory": "extend",
            "selectGroups": ["name"],
            "groupids": group_id
        },
        "auth": auth_token,
        "id": 3
    }
    response = requests.post(ZABBIX_URL, json=payload)
    return response.json().get("result", [])

@app.route('/', methods=['GET'])
def index():
    auth_token = get_auth_token()
    if not auth_token:
        return "Zabbix Authentication Failed"

    groups = get_host_groups(auth_token)
    selected_group = request.args.get("group")
    hosts_data = []

    if selected_group and selected_group in groups:
        hosts = get_hosts_by_group(auth_token, groups[selected_group])
        for host in hosts:
            inv = {k: v for k, v in host.get("inventory", {}).items() if v}
            if inv:
                hosts_data.append({
                    "host": host["host"],
                    "name": host["name"],
                    "inventory": inv
                })

    return render_template("zabbix.html", groups=TARGET_GROUPS, selected_group=selected_group, hosts=hosts_data)
if __name__ == '__main__':
    app.run(debug=True)