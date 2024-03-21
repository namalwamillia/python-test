from flask import Blueprint, request, jsonify
from authors_app.models.book import Book
from authors_app.extensions import db

books = Blueprint('book', __name__, url_prefix='/api/v1/books')

@books.route('/register', methods=['POST'])
def register_book():
    try:
        print("Request JSON:", request.json)  # Debugging statement
        # Extracting request data
        title = request.json.get('title')
        description = request.json.get('description')
        price = request.json.get('price')
        price_unit = request.json.get('price_unit')
        pages = request.json.get('pages')
        publication_date = request.json.get('publication_date')
        isbn = request.json.get('isbn')
        genre = request.json.get('genre')
        user_id = request.json.get('user_id')
        image = request.json.get('image')
        company_id = request.json.get("company_id")

        # Basic input validation
        if not all([title, description, price, pages,price_unit, publication_date, isbn, genre, user_id, company_id, image]):
            return jsonify({"error": 'All fields are required'}), 400

        # Creating a new book
        new_book = Book(
            title=title,
            description=description,
            image=image,
            price=float(price),
            price_unit=price_unit,
            pages=int(pages),
            publication_date=publication_date,
            isbn=isbn,
            genre=genre,
            user_id=int(user_id),
            company_id=company_id
        )

        # Adding and committing to the database
        db.session.add(new_book)
        db.session.commit()

        # Building a response message
        return jsonify({"message": f"Book '{new_book.title}', ID '{new_book.id}' has been uploaded"}), 201

    except Exception as e:
        # Handle exceptions appropriately
        return jsonify({"error": str(e)}), 500
