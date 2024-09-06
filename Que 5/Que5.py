#Question (5). Implement user sessions in a Flask app to store and display user-specific data.

from flask import Flask, session, redirect, url_for, request, render_template, flash

app = Flask(__name__)

# Secret key is required to use sessions. Ensure it's complex and secret in production.
app.secret_key = 'replace_with_a_strong_secret_key'

@app.route('/')
def index():
    # Check if the user is logged in by checking the session
    if 'username' in session:
        username = session['username']
        return f'Hello, {username}! Welcome back!'
    return 'You are not logged in.'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        # Store the username in the session object
        session['username'] = username
        flash(f'{username}, you have successfully logged in!', 'info')
        return redirect(url_for('index'))
    
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # Remove the username from the session
    session.pop('username', None)
    flash('You have successfully logged out.', 'info')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        session['username'] = username
        flash(f'{username}, you have successfully logged in!', 'info')
        return redirect(url_for('index'))
    
    return render_template('login.html')