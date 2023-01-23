import requests

OPENTDB_ENDPOINT = "https://opentdb.com/api.php"

params = {
    "amount": 10,
    "type": "boolean",
    "category": 18
}

response = requests.get(url=OPENTDB_ENDPOINT, params=params)
response.raise_for_status()
question_data = response.json()["results"]
