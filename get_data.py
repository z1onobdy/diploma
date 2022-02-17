import json
import requests
import mysql.connector

swdb = mysql.connector.connect(
  host="localhost",
  user="z10",
  password="password",
  database="sw"
)

mycursor = swdb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS persons (id INT, name VARCHAR(255), gender VARCHAR(255), films VARCHAR(255), PRIMARY KEY(id, name, gender,films))")

character = 1
character_last = 7
planet = 1
planet_last = 7

character_API = 'https://swapi.dev/api/people/'
planet_API = 'https://swapi.dev/api/planets/'
films_API = 'https://swapi.dev/api/films/'

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
      char_id = (character_API + str(character) + ('/')) .strip('/').split('/')[-1]
      for c in z:
        sql = "INSERT IGNORE INTO persons (id, name, gender, films) VALUES (%s, %s, %s, %s)"
        val = [char_id, character_name, character_gender, c]
        mycursor.execute(sql,val)
    except:
        pass
    character += 1
    swdb.commit()
