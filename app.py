import json
import requests


url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
response = requests.get(url, timeout=100)

if response.status_code == 200:
    data_json = response.json()
    data_restaurant = {}

    for item in data_json:
        name_restaurant = item['Company']
        if name_restaurant not in data_restaurant:
            data_restaurant[name_restaurant] = []

        data_restaurant[name_restaurant].append({
            'item': item['Item'],
            'price': item['price'],
            'description': item['description']
        })

else:
    print(f'The error was{response.status_code}')

for name_restaurant, data in data_restaurant.items():
    name_archive = f'{name_restaurant}.json'

    with open(name_archive, 'w', encoding='utf-8') as archive:
        json.dump(data, archive, indent=4)
