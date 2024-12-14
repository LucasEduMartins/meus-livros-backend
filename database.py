import sqlite3

class SqliteDatabase:
    db_name = "database.db"

    def __init__(self, ):
        self._create_table()

    def _create_table(self):
        createBoookTable = """
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL
        );
        """

        createCommmentTable = """
        CREATE TABLE IF NOT EXISTS comments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            book_id INTEGER NOT NULL,
            comment TEXT NOT NULL,
            FOREIGN KEY (book_id) REFERENCES books(id)
        );
        """

        with self.get_connection() as conn:
            conn.execute(createBoookTable)
            conn.execute(createCommmentTable)


    def get_connection(self):
        return sqlite3.connect(self.db_name)
