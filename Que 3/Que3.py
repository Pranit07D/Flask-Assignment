#3. Develop a Flask app that uses URL parameters to display dynamic content.

from flask import Flask

app = Flask(__name__)

# Route that uses URL parameters
@app.route('/greet/<name>')
def greet(name):
    return f"Hello, {name}!"

@app.route('/multiply/<int:x>/<int:y>')
def multiply(x, y):
    result = x * y
    return f"{x} * {y} = {result}"

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=7000) 
