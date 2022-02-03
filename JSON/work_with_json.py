import json


def import_json():
    with open('books-data-source.json') as f:
        bookshelf = json.load(f)
    return bookshelf


def generate_database():
    pass


books = import_json()
for title in books:
    print(title)
