import requests

choice = input("What is your fav pokeman")
url = "https://pokeapi.co/api/v2/pokemon/"
fullurl= url+choice

resp = requests.get(fullurl)
print(resp.json())