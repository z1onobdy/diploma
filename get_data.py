import json
import requests

character = 1
character_last = 5
planet = 1
planet_last = 5

character_API = 'https://swapi.dev/api/people/'
planet_API = 'https://swapi.dev/api/planets/'
films_API = 'https://swapi.dev/api/films/'

#print(character_API.status_code)

while character <= character_last:
    try:
      z = []
      character_data = requests.get(character_API + str(character) + ('/')) 
      parse_character = json.loads(character_data.text)
      #hworld = parse_character['homeworld'] 
      hworld = parse_character['films']
      for c in hworld:
       
        parse_c = requests.get(c)
        parse_c = json.loads(parse_c.text)
        z.append(parse_c['title'])
      #print(z)
      #parse_hworld1 = requests.get(hworld)
      #parse_hworld1 = json.loads(parse_hworld1.text)
      #hworld_name = parse_hworld1['name']
      character_name = parse_character['name']
      character_gender = parse_character['gender']
      id = (character_API + str(character) + ('/')) .strip('/').split('/')[-1]
      print('ID:',id, 'Name:',character_name, 'Gender:',character_gender, 'Films:', ", ".join(z))      
    except:
        pass
    character += 1
