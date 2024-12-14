from models.book import Book

class BookService:
    def __init__(self, db):
        self.db = db

    def get_all_books(self):
        query = "SELECT * FROM books"
        with self.db.get_connection() as conn:
            cursor = conn.execute(query)
            books = [Book(row[0], row[1]).to_dict() for row in cursor.fetchall()]
        return books

    def get_book_by_title(self, title):
        query = "SELECT * FROM books WHERE title = ?"
        with self.db.get_connection() as conn:
            cursor = conn.execute(query, (title,))
            row = cursor.fetchone()
            if row:
                return Book(row[0], row[1]).to_dict()
        return None
    
    def create_book(self, title):
        query = "INSERT INTO books (title) VALUES (?)"
        with self.db.get_connection() as conn:
            cursor = conn.execute(query, (title,))
            conn.commit()
            return Book(cursor.lastrowid, title).to_dict()

    def update_book(self, bookId, title):
        query = "UPDATE books SET title = ? WHERE id = ?"
        with self.db.get_connection() as conn:
            cursor = conn.execute(query, (title, bookId))
            conn.commit()
            if cursor.rowcount > 0:
                return Book(bookId, title).to_dict()
        return None

    def delete_book(self, bookId):
        query = "DELETE FROM books WHERE id = ?"
        with self.db.get_connection() as conn:
            cursor = conn.execute(query, (bookId,))
            conn.commit()
            if cursor.rowcount > 0:
                return Book(bookId, None).to_dict()
        return None