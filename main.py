from fastapi import FastAPI, Query
import requests


app = FastAPI()


@app.get('/api/restaurants/')
def get_restaurants(restaurant: str = Query(None)):
    '''
        Endpoint to see restaurant menus.
    '''

    url = (
        'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
        )
    response = requests.get(url, timeout=100)
    print(response.status_code)

    if response.status_code == 200:
        data_json = response.json()

        if restaurant is None:
            return {'Data': data_json}
        data_restaurant = []
        for item in data_json:
            if item['Company'] == restaurant:
                data_restaurant.append({
                    'item': item['Item'],
                    'price': item['price'],
                    'description': item['description']
                })
        return {'Restaurant': restaurant, 'Menu': data_restaurant}
    else:
        return {'Error': f'{response.status_code}'}
