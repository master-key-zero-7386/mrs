# ==========================================================
# test_lwa.py
# 目的:
# AWSキー無しでSP-APIが応答するか確認
# ==========================================================

import requests

# ▼ 自分の値を入れる
CLIENT_ID = "xxxxxxxxxxxxxxxx"
CLIENT_SECRET = "xxxxxxxxxxxxxxxx"
REFRESH_TOKEN = "Atzr|xxxxxxxxxxxxxxxx"


# ==========================================================
# LWA Access Token取得
# ==========================================================
TOKEN_URL = "https://api.amazon.com/auth/o2/token"

payload = {
    "grant_type": "refresh_token",
    "refresh_token": REFRESH_TOKEN,
    "client_id": CLIENT_ID,
    "client_secret": CLIENT_SECRET,
}

print("=== LWA TOKEN REQUEST ===")

res = requests.post(TOKEN_URL, data=payload)

print("STATUS:", res.status_code)
print(res.text)

if res.status_code != 200:
    raise SystemExit("LWA取得失敗")

access_token = res.json()["access_token"]

print("\nACCESS TOKEN OK\n")


# ==========================================================
# Sellers API
# ==========================================================
url = "https://sellingpartnerapi-fe.amazon.com/sellers/v1/marketplaceParticipations"

headers = {
    "x-amz-access-token": access_token,
    "accept": "application/json",
}

print("=== SP-API REQUEST ===")

res = requests.get(
    url,
    headers=headers,
    timeout=30
)

print("STATUS:", res.status_code)
print(res.text)