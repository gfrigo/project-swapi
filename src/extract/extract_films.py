#pylint: disable=all
import pandas as pd
import requests

def extract_to_save_films_data():
    url='https://swapi.dev/api/films/'

    response = requests.get(url)
    print(f'URL: {url} : Response: {response}')
    response.raise_for_status()
    data = response.json()

    df = pd.DataFrame(data['results'])

    return df


