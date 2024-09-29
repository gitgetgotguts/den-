# request the data from the api and writing it a json file
from config import apikey
import requests
import json


def req_by_ingredients(ingredients,num_of_recipes,apikey,minimize_missing=0,ignore_typ=True):
    minimize_missing+=1
    url = 'https://api.spoonacular.com/recipes/findByIngredients'


    params = {
        'ingredients': ','.join(ingredients),
        'number': num_of_recipes,
        'apiKey': apikey
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
    # Parse the JSON response
    
        data = response.json()
    
        # print(data)
    else:
        print(f'Error: {response.status_code}')
    
    return data



# data=req_by_ingredients(['milk','eggs'],2,apikey)
# # data is a list of dicts containing products

# file_name='out.json'
# with open(file_name, 'w') as json_file:
#     json.dump(data, json_file, indent=4)






