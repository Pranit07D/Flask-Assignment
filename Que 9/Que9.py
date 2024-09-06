#9. Create a RESTful API using Flask to perform CRUD operations on resources like books or movies.

from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure SQLite Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define the Book model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    author = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'year': self.year
        }

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Create a new book (Create)
@app.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    title = data.get('title')
    author = data.get('author')
    year = data.get('year')

    if not title or not author or not year:
        abort(400, description="Missing required fields: 'title', 'author', 'year'")

    new_book = Book(title=title, author=author, year=year)
    db.session.add(new_book)
    db.session.commit()

    return jsonify(new_book.to_dict()), 201

# Retrieve all books (Read)
@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([book.to_dict() for book in books])

# Retrieve a single book by ID (Read)
@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = Book.query.get_or_404(id)
    return jsonify(book.to_dict())

# Update an existing book by ID (Update)
@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    book = Book.query.get_or_404(id)
    data = request.get_json()

    title = data.get('title', book.title)
    author = data.get('author', book.author)
    year = data.get('year', book.year)

    book.title = title
    book.author = author
    book.year = year

    db.session.commit()

    return jsonify(book.to_dict())

# Delete a book by ID (Delete)
@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()

    return '', 204

if __name__ == '__main__':
    app.run(debug=True)