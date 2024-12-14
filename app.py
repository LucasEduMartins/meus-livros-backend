from pydantic import BaseModel

from flask_openapi3 import Info, Tag
from flask_openapi3 import OpenAPI

from flask import jsonify
from flask_cors import CORS



from services.bookService import BookService
from services.commentService import CommentService
from database import SqliteDatabase

# Create the database
dataBase = SqliteDatabase()

# Create the services
bookService = BookService(dataBase)
commentService = CommentService(dataBase)

# Create the API
info = Info(title="book API", version="1.0.0")
app = OpenAPI(__name__, info=info)

# Enable CORS
CORS(app)

# Create the tags for documentation
book_tag = Tag(name="book", description="Some Book")

# Create the book DTOs
class BookBody(BaseModel):
    title: str 

class BookPath(BaseModel):
    id: int

# Create the book routes
@app.get("/books", tags=[book_tag])
def get_books():
    """Retorna todos os livros cadastrados
    Retorna todos os livros cadastrados
    """
    books = bookService.get_all_books()
    return jsonify(books), 200

@app.post('/books', tags=[book_tag])
def create_book(body: BookBody):
    """Cadastra um livro
    Cadastra um livro
    """
    if not body.title:
        return jsonify({"message": "Titulo é obrigatório"}), 400
    
    bookExist = bookService.get_book_by_title(body.title)
    
    if bookExist and bookExist.get("title"):
        return jsonify({"message": "Livro já cadastrado"}), 400
    
    book = bookService.create_book(body.title)
    return jsonify(book), 201

@app.put("/books/<id>", tags=[book_tag])
def update_book(path: BookPath, body: BookBody):
    """Atualiza um livro
    Atualiza um livro
    """
    if not body.title:
        return jsonify({"message": "Titulo é obrigatório"}), 400    
    
    book = bookService.update_book(path.id, body.title)

    if book:
        return jsonify(book), 200
    
    return jsonify({"message": "Livro não encontrado"}), 404

@app.delete("/books/<id>", tags=[book_tag])
def delete_book(path: BookPath):
    """Remove um livro
    Remove um livro
    """
    if not path.id:
        return jsonify({"message": "Id é obrigatório"}), 400
    
    book = bookService.delete_book(path.id)
    if book:
        return jsonify(book), 200

    return jsonify({"message": "Livro não encontrado"}), 404


comment_tag = Tag(name="comment", description="Some Comment")

class CommentBody(BaseModel):
    comment: str 

class CommentPath(BaseModel):
    bookId: int
    commentId: int

@app.get("/books/<id>/comments", tags=[comment_tag])
def get_comments(path: BookPath):
    """Lista os comentários de um livro
    Lista os comentários de um livro
    """
    comments = commentService.get_comments_by_book_id(path.id)
    return jsonify(comments), 200

@app.post('/books/<id>/comments', tags=[comment_tag])
def create_comment(path: BookPath, body: CommentBody):
    """Cadastra um comentário
    Cadastra um comentário
    """
    if not body.comment:
        return jsonify({"message": "Comentário é obrigatório"}), 400
    
    
    book = commentService.create_comment(path.id, body.comment)
    return jsonify(book), 201

@app.put("/books/<bookId>/comments/<commentId>", tags=[comment_tag])
def update_comment(path: CommentPath, body: CommentBody):
    """Atualiza um comentário
    Atualiza um comentário
    """
    if not path.bookId:
        return jsonify({"message": "Id do livro é obrigatório"}), 400
    
    if not path.commentId:
        return jsonify({"message": "Id do comentário é obrigatório"}), 400
    
    if not body.comment:
        return jsonify({"message": "Comentário é obrigatório"}), 400
    
    comment = commentService.update_comment(path.bookId, path.commentId, body.comment)
    if comment:
        return jsonify(comment), 200
    
    return jsonify({"message": "Comentário não encontrado"}), 404

@app.delete("/books/<bookId>/comments/<commentId>", tags=[comment_tag])
def delete_comment(path: CommentPath):
    """Remove um comentário
    Remove um comentário
    """
    if not path.bookId:
        return jsonify({"message": "Id do livro é obrigatório"}), 400
    
    if not path.commentId:
        return jsonify({"message": "Id do comentário é obrigatório"}), 400
    
    comment = commentService.delete_comment(path.bookId, path.commentId)
    if comment:
        return jsonify(comment), 200

    return jsonify({"message": "Comentário não encontrado"}), 404


if __name__ == "__main__":
    app.run(debug=True)