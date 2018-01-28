from flask import Flask, request, render_template
app = Flask(__name__, static_url_path = '/static')

@app.route('/greet.html')
def greet():
  p_name = request.args.get('name')
  p_language = request.args.get('lang')
  return render_template (
    'greet.html', 
    name = p_name,
    language = p_language
  )

if __name__ == '__main__':
  app.run(host = '0.0.0.0', port = 8080)
