# FastAPI Basic REST APIs

This project demonstrates the implementation of basic REST APIs using FastAPI, a modern web framework for building APIs with Python. The APIs allow you to perform CRUD operations (Create, Read, Update, Delete) on a collection of books.

## Overview

The project consists of the following endpoints:

- **GET /api-endpoint**: Returns a list of all books.
- **GET /books/{book_title}**: Retrieves a book by its title.
- **GET /books/?category={category}**: Retrieves books by category using query parameters.
- **GET /books/by_author/?book_author={author}**: Retrieves books by author using query parameters.
- **GET /books/{book_author}/{category}**: Retrieves books by both author and category using dynamic path parameters.
- **POST /books/create_book**: Creates a new book.
- **PUT /books/update_book**: Updates an existing book.
- **DELETE /books/delete_book/{book_title}**: Deletes a book by its title.

## Usage

To run the FastAPI server locally, follow these steps:

1. Install the required dependencies using `pip install -r requirements.txt`.
2. Start the server by running `uvicorn main:app --reload`.
3. Access the API endpoints using an API client such as [Postman](https://www.postman.com/) or by sending requests using tools like `curl` or Python's `requests` library.

## Example Requests

### GET /api-endpoint

```http
GET /api-endpoint
GET /books/Tittle%20One
GET /books/?category=science

POST /books/create_book
{
    "tittle": "New Book",
    "author": "New Author",
    "category": "New Category"
}


