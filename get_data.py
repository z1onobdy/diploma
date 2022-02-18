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
mycursor.execute("CREATE TABLE IF NOT EXISTS persons (id INT, name VARCHAR(255), gender VARCHAR(255), homeworld VARCHAR(255), PRIMARY KEY (id, name, gender, homeworld))")
mycursor.execute("CREATE TABLE IF NOT EXISTS planets (id INT, name VARCHAR(255), gravity VARCHAR(255), climate VARCHAR(255), residents VARCHAR(255), PRIMARY KEY(id, name, gravity, climate, residents))")

character_API = 'https://swapi.dev/api/people/'
planet_API = 'https://swapi.dev/api/planets/'
films_API = 'https://swapi.dev/api/films/'

character = 1
character_last = json.loads(requests.get(character_API).text)
character_last = character_last['count']
planet = 1
planet_last = json.loads(requests.get(planet_API).text)
planet_last = planet_last['count']

while character <= character_last:
    try:
      character_data = requests.get(character_API + str(character) + ('/')) 
      parse_character = json.loads(character_data.text)
      hworld = parse_character['homeworld'] 
      parse_hworld1 = requests.get(hworld)
      parse_hworld1 = json.loads(parse_hworld1.text)
      hworld_name = parse_hworld1['name']
      character_name = parse_character['name']
      character_gender = parse_character['gender']
      char_id = (character_API + str(character) + ('/')) .strip('/').split('/')[-1]
      sql = "INSERT IGNORE INTO persons (id, name, gender, homeworld) VALUES (%s, %s, %s, %s)"
      val = [char_id, character_name, character_gender, hworld_name]
      mycursor.execute(sql,val)
      
    except:
        pass
    character += 1

while planet <= planet_last:
    try:
      zz = []
      planet_data = requests.get(planet_API + str(planet) + ('/')) 
      parse_planet = json.loads(planet_data.text)
      planet_name = parse_planet['name']
      planet_gravity = parse_planet['gravity']
      planet_climate = parse_planet['climate']
      planet_residents = parse_planet['residents']
      for pp in planet_residents:
        parse_pp = requests.get(pp)
        parse_pp = json.loads(parse_pp.text)
        zz.append(parse_pp['name'])
      planet_id = (planet_API + str(planet) + ('/')) .strip('/').split('/')[-1]
      for ss in zz:
        sql = "INSERT INTO planets (id, name, gravity, climate, residents) VALUES (%s, %s, %s, %s, %s)"
        val = [planet_id, planet_name, planet_gravity, planet_climate, ss]
        mycursor.execute(sql,val)
    except:
        pass
    planet += 1

    swdb.commit()
    

