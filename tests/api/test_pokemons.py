import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '93c904306ac335a663267832505f6351'
HEADER = {'content - Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '28915'



def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params= {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url= f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]['name'] == 'Корж'



@pytest.mark.parametrize('key, value', [('name','Корж' ), ('trainer_id', TRAINER_ID), ('id','289880')])
def test_parametrize(key, value):
   response_parametrize = requests.get(url= f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID}) 
   assert response_parametrize.json()["data"][0][key] == value




def test_status_codee():
    response = requests.get(url = f'{URL}/trainers', params= {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200



def test_part_of_response_tr():
    response_get = requests.get(url= f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]['trainer_name'] == 'AlfaEcho'


'{"status":"success","data":[{"id":"28915","trainer_name":"AlfaEcho","level":"5","pokemons":["219730","220205","220158","220211","219974","220126","220207","218451","219927","220156","220213","214437","220130","217487","217498","217496","217499","217528","218452","219675","219731","219776","220128","220214","222506","220208","220066","220116","220127","220129","220210","251249","224530","250941","251248","250923","275343","288946","224529","288948","288941","288947","288944","288942","289860","289880","289871","220262","289872","214545","214546","214547","215357","214520","215356","214443","225263","223034","224528","217497","217481"],"pokemons_alive":["288946","288947","289880","289871","224528"],"pokemons_in_pokeballs":[],"get_history_battle":"0","is_premium":true,"premium_duration":949,"avatar_id":9,"city":"Казань"}]}'


