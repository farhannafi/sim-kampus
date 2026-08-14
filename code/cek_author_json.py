import requests
import json

SERPAPI_API_KEY = "1eb991a416303d0888fee987b55b42ca60ea7fd6d75f1ee0132782515a461d36"
AUTHOR_ID = "3ZEzr0EAAAAJ"  # ID Handry Rochmad Dwi Happy

params = {
    "engine": "google_scholar_author",
    "author_id": AUTHOR_ID,
    "hl": "id",
    "api_key": SERPAPI_API_KEY,
}

res = requests.get("https://serpapi.com/search", params=params)
data = res.json()

# simpan ke file agar mudah dibaca
with open("hasil_raw_handry.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("✅ cek_author_json' berhasil dibuat, silakan buka untuk cek struktur JSON-nya.")
