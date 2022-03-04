from app import app, db
from flask import render_template, request, jsonify
from app.models import Author, Book

data = [{"title": "Harry", "author": "JK Rowling"}, {"title": "Lord of Rings", "author": "Whoever"}]

@app.route("/", methods=["GET"])
def home():
    books = db.session.query(Book).all()
    books_list = []

    for book in books:
        author = Author.query.get(book.author_id)
        book_object = {"id": book.book_id, "title": book.title, "author": author.name}
        books_list.append(book_object)

    return render_template("index.html", books=books_list)

@app.route("/delete/<int:id>", methods=["DELETE"])
def delete_book(id):
    book = Book.query.get(id)
    db.session.delete(book)
    db.session.commit()

    return ""

@app.route("/submit", methods=["POST"])
def submit():
    global_book_object = Book()

    title = request.form["title"]
    author_name = request.form["author"]

    author_exists = db.session.query(Author).filter(Author.name == author_name).first()
    print(author_exists)
    # check if author already exists in db
    if author_exists:
        author_id = author_exists.author_id
        book = Book(author_id=author_id, title=title)
        db.session.add(book)
        db.session.commit()
        global_book_object = book
    else:
        author = Author(name=author_name)
        db.session.add(author)
        db.session.commit()

        book = Book(author_id=author.author_id, title=title)
        db.session.add(book)
        db.session.commit()
        global_book_object = book

    response = f"""
    <tr>
        <td>{title}</td>
        <td>{author_name}</td>
        <td>
            <button hx-delete="/delete/{global_book_object.book_id}">Delete</button>
        </td>
    </tr>
    """
    return response