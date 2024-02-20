#pylint: disable=all
import pandas as pd
import requests

def extract_to_save_people_data():
    urls=[]
    for url in range(1,6):
        if url == 1:
            urls.append('https://swapi.dev/api/people/')
        else:
            urls.append(f'https://swapi.dev/api/people/?page={url}')


    data_response = []
    for url in urls:
        try:
            response = requests.get(url)
            print(f'URL: {url} : Response: {response}')
            response.raise_for_status()
            data = response.json()
            data_response.append(data['results'])
        except Exception as exc:
            print(exc)


    df_1 = pd.DataFrame(data_response[0])
    df_2 = pd.DataFrame(data_response[1])
    df_3 = pd.DataFrame(data_response[2])
    df_4 = pd.DataFrame(data_response[3])
    df_5 = pd.DataFrame(data_response[4])
    df = pd.concat([df_1, df_2, df_3, df_4, df_5], axis=0)
    df.reset_index(inplace=True)

    return df