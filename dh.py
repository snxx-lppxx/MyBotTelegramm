import sqlite3


class DatabaseHandler:

    def __init__(self):
        self.base = sqlite3.connect('data.db')
        self.cursor = self.base.cursor()

        self.base.execute('''CREATE TABLE IF NOT EXISTS DATA
                     (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, author TEXT NOT NULL, book TEXT NOT NULL)''')

    def fill_database(self, data: dict):
        for author_name, book_names in data.items():
            for i in book_names:
                try:
                    self.cursor.execute(f"""INSERT INTO DATA (author, book)
                                        VALUES ('{author_name}', '{i}')""")
                except sqlite3.OperationalError as e:
                    print("ERROR OCCURRED", )
                    print('author:', author_name)
                    print('book:', i)
                    print('type:', type(i))
                    rep = str(i).replace("'", "\"")
                    print("replaced:", rep)
                    self.cursor.execute(f"""INSERT INTO DATA (author, book)
                                                            VALUES ('{author_name}', '{rep}')""")

        self.base.commit()
        self.base.close()

    def get_value(self):
        pass
