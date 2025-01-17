import requests
import json

api_url = 'http://api.open-notify.org/astros.json'

response = requests.get(api_url)

if response.status_code == 200:
    data = response.json()

    with open('astros.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print('Дані успішно записані в JSON файл!')
else:
    print('Не вдалося отримати дані з API.')