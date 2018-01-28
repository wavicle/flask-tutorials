from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

def getCapitalFromDB(country):
  connection = sqlite3.connect("mydb.db")
  connection.row_factory = sqlite3.Row
  cursor = connection.cursor()
  rows = cursor.execute(
    'SELECT capital FROM country_capital WHERE country = :country',
    {'country': country}
  ).fetchall()
  if len(rows) > 0:
    return rows[0]['capital']
  else:
    return None

@app.route('/getCapital.html', methods=['GET','POST'])
def getCapital():
  if request.method == 'GET':
    return render_template(
    'getCapital.html'
  )
  else:
    country = request.form.get('country')
    capital = getCapitalFromDB(country)
    return render_template (
      'getCapital.html',
      country = country, capital = capital,
      calcSuccess = capital is not None,
      capitalNotFound = capital is None
    )

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)

