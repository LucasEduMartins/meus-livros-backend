class Comment:
    def __init__(self, id, bookId, comment):
        self.id = id
        self.bookId = bookId
        self.comment = comment

    def to_dict(self):
        return {
            "id": self.id,
            "bookId": self.bookId,
            "comment": self.comment
        }