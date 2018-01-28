from flask import Flask, request, render_template
app = Flask(__name__)

def getFactorial(num):
  if num == 0 or num == 1:
    return 1
  else:
    return num * getFactorial(num - 1)

def isValidPositiveInt(numString):
  try:
    num = int(numString)
    return num > 0
  except:
    return False

@app.route('/factorial.html', methods=['GET','POST'])
def calFactorial():
  if request.method == 'GET':
    return render_template('factorial_entry_form.html')
  else:
    numberString = request.form.get('number')
    if isValidPositiveInt(numberString):
      number = int(numberString)
      factorial = getFactorial(number)
      return render_template (
        'show_factorial.html',
        number = numberString,
        factorial = factorial
      )
    else:
      return render_template (
        'factorial_entry_form.html',
        invalidNumber = True,
        number = numberString
      )

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)
