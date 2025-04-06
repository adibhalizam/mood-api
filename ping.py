import requests

try:
    res = requests.get("https://mood-api-ns8u.onrender.com/")
    print("Ping success:", res.status_code)
except Exception as e:
    print("Ping failed:", e)
