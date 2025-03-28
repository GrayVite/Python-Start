# How ot connect to API using python

import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"

    response = requests.get(url) # return a response objects. 200 mean okay, 404 -> not found
    
    if response.status_code == 200:
        pokmeon_data = response.json()
        return pokmeon_data
    else:
        print(f"Failed to retrieve data: {response.status_code}")

def main():
    pokemon_name = input("Enter pokemon name: ")
    pokemon_info = get_pokemon_info(pokemon_name)

    if pokemon_info:
        print(f"Name: {pokemon_info["name"].capitalize()}")
        print(f"ID: {pokemon_info["id"]}")
        print(f"Height: {pokemon_info["height"]}")
        print(f"Weight: {pokemon_info["weight"]}")

if __name__ == "__main__":
    main()