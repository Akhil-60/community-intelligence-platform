import requests
import json
import os

TOPIC = "community detection"

url = f"https://api.openalex.org/works?search={TOPIC}&per-page=50"

response = requests.get(url)

print("Status Code:", response.status_code)

data = response.json()

os.makedirs("data", exist_ok=True)

with open("data/papers.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)

print("Papers saved successfully!")
print("Total papers fetched:", len(data.get("results", [])))