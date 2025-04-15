import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '93c904306ac335a663267832505f6351'
HEADER = {'content - Type' : 'application/json', 'trainer_token' : TOKEN}

body_registration = {
    "trainer_token": TOKEN,
    "email": "ea136@bk.ru",
    "password": "1234"
}

body_confirmation = {
    "trainer_token": "токен_из_бота_котика"
}

body_create = {
    "name": "Корж",
    "photo_id": 1
}

body_new_name = {
    "pokemon_id": "288948",
    "name": "New Name",
    "photo_id": "2"}

body_add_pokeball = {
     "pokemon_id": "289872",
    "name": "Корж",
    "photo_id": "2"
}

'''response = requests.post(url= f'{URL}/trainers/reg' , headers = HEADER, json =body_registration)
print(response.text)'''


'''response_confirmation = requests.post(url = f'{URL}/confirm_email', headers= HEADER, json = body_confirmation)
print(response_confirmation.text)'''



response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)
message = response_create.json()['message']
print(message)


response_new_name = requests.put(url= f'{URL}/pokemons', headers= HEADER, json = body_new_name)
message = response_new_name.json()['message']
print(message)


response_add_pokeball = requests.post(url= f'{URL}/trainers/add_pokeball', headers= HEADER, json = body_add_pokeball)
message = response_add_pokeball.json()['message']
print(message)
