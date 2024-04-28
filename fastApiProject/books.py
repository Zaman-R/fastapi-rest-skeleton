from fastapi import FastAPI, Body

app = FastAPI()

Books = [
    {'tittle': "Tittle One", 'author': 'A1', 'category': 'science'},
    {'tittle': "Tittle two", 'author': 'A2', 'category': 'com'},
    {'tittle': "Tittle three", 'author': 'A3', 'category': 'math'},
    {'tittle': "Tittle Four", 'author': 'A3', 'category': 'phy'},
    {'tittle': "Tittle Five", 'author': 'A4', 'category': 'science'},
]


@app.get("/api-endpoint")
async def first_api():
    return Books

# Get
# Topic Path and Query Params
# sequence matters

# for Path dynamic param
@app.get("/books/{book_tittle}")
async def read_book_by_title(book_tittle: str):
    for book in Books:
        if book.get('tittle').casefold() == book_tittle.casefold():
            return book


# for query params
@app.get("/books/")
async def read_category_by_query(category: str):
    books_to_return = []
    for book in Books:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


@app.get("/books/by_author/")
async def read_book_by_author(book_author: str):
    books_to_return = []
    for book in Books:
        if book.get('author').casefold() == book_author.casefold():
            books_to_return.append(book)
    return books_to_return


# for both query and dynamic one
@app.get("/books/{book_author}/")
async def read_book_by_author_category(book_author: str, category: str):
    books_to_return = []
    for book in Books:
        if book.get('author').casefold() == book_author.casefold() and book.get(
                'category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return



#  Post Method
@app.post("/books/create_book")
async def create_book(new_book=Body()):
    Books.append(new_book)

# Put Method
@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for i in range(len(Books)):
        if Books[i].get('tittle').casefold() == updated_book.get('tittle').casefold():
            Books[i].update(updated_book)

# Delete
@app.delete("/books/delete_book/{book_tittle}")
async def delete_book(book_tittle: str):
    for book in Books:
        if book.get('tittle').casefold() == book_tittle.casefold():
            Books.remove(book)
            break