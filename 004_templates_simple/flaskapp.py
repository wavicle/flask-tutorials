from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/hello.html')
def hello():
  name = request.args.get('name')
  return render_template('hello.html', name=name)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)
