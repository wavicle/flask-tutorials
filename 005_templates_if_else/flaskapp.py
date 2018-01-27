from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/greet.html')
def greet():
  name = request.args.get('name')
  language = request.args.get('lang')
  return render_template (
    'greet.html', 
    name=name,
    language=language
  )

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)
