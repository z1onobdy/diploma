import mysql.connector

swdb = mysql.connector.connect(
  host="localhost",
  user="z10",
  password="password",
  database="sw"
)
mycursor = swdb.cursor()
planet_name_cursor = swdb.cursor()
planet_name_cursor.execute("SELECT planets.name, planets.gravity, planets.climate FROM planets group by planets.name, planets.gravity, planets.climate")
pln = planet_name_cursor.fetchall()
for i in pln:
  print('Planet name: ' ,i[0])
  print('Planet gravity:' ,i[1])
  print('Planet climate:' ,i[2])
  mycursor.execute("SELECT persons.name as resident, persons.gender as gender, persons.homeworld as homeworld from persons inner join planets on persons.name = planets.residents where planets.name = '%s'" %i[0])
  res = mycursor.fetchall()
  for l in res:
    print('  Resident:' ,l[0],'\n', '    Gender:' , l[1],'\n', '    Homeworld:' , l[2])
  print('\n')
  