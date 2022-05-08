import requests
res = requests.post('http://127.0.0.1:5000', json={"mytext":"lalala"})
if res.ok:
    print(res.json())