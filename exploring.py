import requests
import json

pokemon_names = ['pikachu', 'bulbasaur', 'charmander']

def pikachu_data():
    response = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')
    json_data = response.text

    pikachu_data = json.loads(json_data)

    pokemon = pikachu_data['name']
    ability1 = pikachu_data['abilities'][0]['ability']['name']
    ability2 = pikachu_data['abilities'][1]['ability']['name']

    print(f"\nPokemon Name: {pokemon}\nAbility 1: {ability1}\nAbility 2: {ability2}\n")

def fetch_pokemon_data():
    for name in pokemon_names:
        print("-" * 50)
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name}')
        
        pokemon_data = response.json()  
        pokemon = pokemon_data['name']

        print(f"\nPokemon Name: {pokemon}\n")
        for row in pokemon_data['abilities']:
            print(f"Ability: {row['ability']['name']}\n")

def calculate_average_weight():
    pokemon_weight = []
    
    for name in pokemon_names:
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name}')
        
        pokemon_data = response.json()  
        pokemon_weight.append(pokemon_data['weight'])

    average_weight = round(sum(pokemon_weight) / len(pokemon_names), 2)

    print("-" * 50)
    print(f"\nAverage Weight: {average_weight}\n")
    print("-" * 50)


pikachu_data()
fetch_pokemon_data()
calculate_average_weight()