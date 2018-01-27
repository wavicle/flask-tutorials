from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hellWorld():
  if request.args.get('name') is None:
    return "No name was provided! Try http://localhost:8080?name=Albert"
  else:
    return 'Hello, ' + request.args.get('name')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)
