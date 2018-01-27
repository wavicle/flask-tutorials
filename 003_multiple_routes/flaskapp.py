from flask import Flask, request
app = Flask(__name__)

@app.route('/hello.html')
def hello():
  name = request.args.get('name')
  if name is None:
    return "No name was provided! Try http://localhost:8080/hello.html?name=Albert"
  else:
    return 'Hello, <b>' + name + '</b>'

@app.route('/namaste.html')
def namaste():
  name = request.args.get('name')
  if name is None:
    return "No name was provided! Try http://localhost:8080/hello.html?name=Albert"
  else:
    return 'Namaste, <b>' + name + '</b>'

@app.route('/hola.html')
def hola():
  name = request.args.get('name')
  if name is None:
    return "No name was provided! Try http://localhost:8080/hello.html?name=Albert"
  else:
    return 'Hola, <b>' + name + '</b>'

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)
