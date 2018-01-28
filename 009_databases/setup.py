import sqlite3
import os

try:
  os.remove('mydb.db')
  print('The database existed, but has been removed to be recreated')
except FileNotFoundError as e:
  print('The database will be created for the first time')

connection = sqlite3.connect('mydb.db')
cursor = connection.cursor()

cursor.execute('CREATE TABLE country_capital (country text, capital text)')

insertSql = 'INSERT INTO country_capital (country, capital) VALUES (:country, :capital)'

cursor.execute(insertSql, {'country': 'India', 'capital': 'New Delhi'})
cursor.execute(insertSql, {'country': 'USA', 'capital': 'Washington D.C'})
cursor.execute(insertSql, {'country': 'Canada', 'capital': 'Ottawa'})
cursor.execute(insertSql, {'country': 'Australia', 'capital': 'Canberrra'})

connection.commit()
connection.close()


