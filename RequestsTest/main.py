import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'твой токен'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

body_create = {
    "name": "pikachu",
    "photo_id": 12
}

body_name_change = {
    "pokemon_id": "321947",
    "name": "Чармелион",
    "photo_id": 2
}

body_catch_in_a_Pokeball = {
    "pokemon_id": "321947"
}





response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)
message = response_create.json()['message']
print(message)

response_name_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_name_change)
print(response_name_change.text)
message = response_name_change.json()['message']
print(message)

response_catch_in_a_Pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch_in_a_Pokeball)
print(response_catch_in_a_Pokeball.text)
message = response_catch_in_a_Pokeball.json()['message']
print(message)