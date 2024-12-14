from models.comment import Comment

class CommentService:
    def __init__(self, db):
        self.db = db

    def get_all_comments(self):
        query = "SELECT * FROM comments"
        with self.db.get_connection() as conn:
            cursor = conn.execute(query)
            comments = [Comment(row[0], row[1], row[2]).to_dict() for row in cursor.fetchall()]
        return comments

    def get_comments_by_book_id(self, book_id):
        query = "SELECT * FROM comments WHERE book_id = ?"
        with self.db.get_connection() as conn:
            cursor = conn.execute(query, (book_id,))
            comments = [Comment(row[0], row[1], row[2]).to_dict() for row in cursor.fetchall()]
        return comments

    def create_comment(self, book_id, comment):
        query = "INSERT INTO comments (book_id, comment) VALUES (?, ?)"
        with self.db.get_connection() as conn:
            cursor = conn.execute(query, (book_id, comment))
            conn.commit()
            return Comment(cursor.lastrowid, book_id, comment).to_dict()
    
    def update_comment(self, bookId, commentId, comment):
        query = "UPDATE comments SET comment = ? WHERE id = ? AND book_id = ?"
        with self.db.get_connection() as conn:
            cursor = conn.execute(query, (comment, commentId, bookId))
            conn.commit()
            if cursor.rowcount > 0:
                return Comment(commentId, bookId, comment).to_dict()
        return None
    
    def delete_comment(self, bookId, commentId):
        query = "DELETE FROM comments WHERE id = ? AND book_id = ?"
        with self.db.get_connection() as conn:
            cursor = conn.execute(query, (commentId, bookId,))
            conn.commit()
            if cursor.rowcount > 0:
                return Comment(commentId, None, None).to_dict()
        return None