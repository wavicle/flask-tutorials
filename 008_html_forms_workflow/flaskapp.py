from flask import Flask, request, render_template
app = Flask(__name__)

capitalsByCountry={
  'India':'New Delhi',
  'USA': 'Washington, D.C.'
}

@app.route('/getCapital.html', methods=['GET','POST'])
def getCapital():
  if request.method == 'GET':
    return render_template(
    'getCapital.html'
  )
  else:
    country = request.form.get('country')
    capital = capitalsByCountry.get(country)
    return render_template (
      'getCapital.html',
      country = country, capital = capital,
      calcSuccess = True
    )

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)

