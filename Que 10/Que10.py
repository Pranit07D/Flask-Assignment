#10. Design a Flask app with proper error handling for 404 and 500 errors.

from flask import Flask, render_template

app = Flask(__name__)

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route that triggers a 500 error for demonstration purposes
@app.route('/cause_500')
def cause_500():
    # This will intentionally cause a division by zero error to demonstrate a 500 error
    return 1 / 0

# Custom handler for 404 Not Found error
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

# Custom handler for 500 Internal Server Error
@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)