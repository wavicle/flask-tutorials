from flask import Flask, request
app = Flask(__name__)

def isValidInteger(someString):
  try:
    int(someString)
    return True
  except:
    return False

@app.route('/table.html')
def hellWorld():
  numString = request.args.get('num')
  if not isValidInteger(numString):
    return 'Invalid integer: ' + str(numString)
  else:
    responseString = 'Here is the mathematical table for ' + numString + '<br/>'
    number = int(numString)
    for i in range(1, 11):
     product = i * number
     responseString += str(product) + '<br/>'
    return responseString 

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)
