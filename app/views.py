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
        book_object = {"title": book.title, "author": author.name}
        books_list.append(book_object)

    return render_template("index.html", books=books_list)

@app.route("/get")
def get_books():
    #books = db.session.query(Book).all()
    authors = db.session.query(Author).all()

    authors_list = []

    for author in authors:
        author_object = {"author": author.name, "books": author.books}
        print(author_object)

    authors_list.append(author_object)

    return jsonify({"authors": authors_list})
    #return authors

@app.route("/submit", methods=["POST"])
def submit():
    #Author = models.Author
    #Book = models.Book

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
    else:
        author = Author(name=author_name)
        db.session.add(author)
        db.session.commit()

        book = Book(author_id=author.author_id, title=title)
        db.session.add(book)
        db.session.commit()

    #book_d = {"title": title, "author": author}
    #data.append(book_d)

    response = f"""
    <tr>
        <td>{title}</td>
        <td>{author_name}</td>
        </tr>
    """
    return response