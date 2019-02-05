from flask import jsonify, request, Response
from UsersModule import *
from functools import wraps
from BookModule import *
from settings import *
import json
import jwt
import datetime
# import time


def valid_book(bookObj):
    if ("name" in bookObj
            and 'price' in bookObj
                and 'isbn' in bookObj):
        return True
    else:
        return False


@app.route('/login', methods=['POST'])
def get_token():
    req_data = request.get_json()
    username = str(req_data['username'])
    password = str(req_data['password'])

    match = User.username_password_match(username, password)

    if match:
        exp_date = datetime.datetime.utcnow() + datetime.timedelta(minutes=2)
        token = jwt.encode({'exp': exp_date}, app.config['SECRET_KEY'], algorithm='HS256')
        return token
    else:
        return Response('', 401, mimetype=JSON_MIME_TYPE)


def token_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = request.args.get('token')
        try:
            jwt.decode(token, app.config['SECRET_KEY'])
            return func(*args, **kwargs)
        except:
            return Response(json.dumps({'error': 'Need a valid token'}), 401, mimetype=JSON_MIME_TYPE)
    return wrapper

#POST book
@app.route('/books', methods=['POST'])
@token_required
def add_book():
    req_data = request.get_json()
    if valid_book(req_data):
        Book.add_book(req_data['name'], req_data['price'], req_data['isbn'])

        #books.insert(0, book)
        response = Response("", 201, mimetype=JSON_MIME_TYPE)
        response.headers['Location'] = "/books/" + str(req_data['isbn'])

    else:
        invalidBookObjectErrorMsg = {
            "error": "Invalid book object",
            "helpStr": "Data passed is not in the correct format"
        }
        response = Response(json.dumps(invalidBookObjectErrorMsg), status=400, mimetype=JSON_MIME_TYPE)

    return response


#PUT
@app.route('/books/<int:isbn>', methods=['PUT'])
@token_required
def put_book(isbn):
    new_data = request.get_json()
    new_book = {'name': new_data['name'],
                'price': new_data['price'],
                'isbn': isbn
                }
    # for book in books:
    #     if book['isbn'] == isbn:
    #         books.remove(book)
    #         books.insert(0, new_book)
    #
    if Book.delete_book(isbn) == True:
        Book.add_book(new_book['name'], new_book['price'], new_book['isbn'])
        response = Response("", status=204, mimetype=JSON_MIME_TYPE)
    else:
        invalidBookObjectErrorMsg = {
            "error": "Invalid book object",
            "helpStr": "Data passed is not in the correct format"
        }
        response = Response(json.dumps(invalidBookObjectErrorMsg), status=400, mimetype=JSON_MIME_TYPE)

    return response


#PATCH
@app.route('/books/<int:isbn>', methods=['PATCH'])
@token_required
def edit_book(isbn):
    req_data = request.get_json()
    response = Response("", status=204, mimetype=JSON_MIME_TYPE)

    if 'name' in req_data:
        Book.update_book_name(isbn, req_data['name'])
    if 'price' in req_data:
        Book.update_book_price(isbn, req_data['price'])

    return response


#DELETE
@app.route('/books/<int:isbn>', methods=['DELETE'])
@token_required
def del_book(isbn):
    # i = 0
    # response = Response("", status=404, mimetype=JSON_MIME_TYPE)
    # for book in books:
    #     if book['isbn'] == isbn:
    #         books.remove(book)
    #         response = Response("", status=204, mimetype=JSON_MIME_TYPE)
    #         break
    response = Response("", status=404, mimetype=JSON_MIME_TYPE)

    if Book.delete_book(isbn) == True:
        response = Response("", status=204, mimetype=JSON_MIME_TYPE)
    return response


#GET /store
@app.route("/books", methods=['GET'])
def get_books():
    return jsonify({'books': Book.get_all_books()})


@app.route('/books/<int:isbn>')
def get_book_by_isbn(isbn):
    return_val = Book.get_book(isbn)
    return jsonify(return_val)


if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    User.create_user('admin', 'pass')
    # print(User.get_all_users())
    # print("Hello")
    app.run(port=8000)

