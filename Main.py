import DataParser
from DatabaseHandler import DatabaseHandler


def logic():
    # initialization
    db = DatabaseHandler()
    db.fill_database(DataParser.fetch_data())
    return
    # if len(a) == 0:
    #     # err handling here
    #     return
    # bot greeting
    input_book_name = input("Введите название произведения: ")
    # check exist in db
    # do stuff
    pass


if __name__ == "__main__":
    logic()
