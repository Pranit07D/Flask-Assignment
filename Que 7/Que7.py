#7. Integrate a SQLite database with Flask to perform CRUD operations on a list of items.
import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session handling and flash messages

DATABASE = 'items.db'

# Connect to the SQLite database
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Initialize the database with a table
def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT NOT NULL
        );
    ''')
    conn.commit()
    conn.close()

# Route to display all items (Read)
@app.route('/')
def index():
    conn = get_db_connection()
    items = conn.execute('SELECT * FROM items').fetchall()
    conn.close()
    return render_template('index.html', items=items)

# Route to display the form for adding a new item (Create)
@app.route('/add', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']

        if not name or not description:
            flash('Name and description are required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO items (name, description) VALUES (?, ?)', (name, description))
            conn.commit()
            conn.close()
            flash('Item successfully added!')
            return redirect(url_for('index'))

    return render_template('add_item.html')

# Route to edit an item (Update)
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_item(id):
    conn = get_db_connection()
    item = conn.execute('SELECT * FROM items WHERE id = ?', (id,)).fetchone()

    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']

        if not name or not description:
            flash('Name and description are required!')
        else:
            conn.execute('UPDATE items SET name = ?, description = ? WHERE id = ?', (name, description, id))
            conn.commit()
            conn.close()
            flash('Item successfully updated!')
            return redirect(url_for('index'))

    conn.close()
    return render_template('edit_item.html', item=item)

# Route to delete an item (Delete)
@app.route('/delete/<int:id>', methods=['POST'])
def delete_item(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM items WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('Item successfully deleted!')
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Initialize the database
    init_db()
    app.run(debug=True)