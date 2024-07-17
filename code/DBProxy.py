import sqlite3


class DBProxy:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = sqlite3.connect(db_name)
        self.connection.execute('CREATE TABLE IF NOT EXISTS dados('
                                'id INTEGER PRIMARY KEY AUTOINCREMENT,'
                                'name TEXT NOT NULL,'
                                'score INTEGER NOT NULL,'
                                'date TEXT NOT NULL)', )

    def insert(self, score_dict):
        self.connection.execute('INSERT INTO dados (name, score, date)'
                                'VALUES (:name, :score, :date)', score_dict)
        self.connection.commit()

    def return_top10(self):
        return self.connection.execute('SELECT * FROM dados ORDER BY score DESC LIMIT 10').fetchall()

    def close(self):
        return self.connection.close()
