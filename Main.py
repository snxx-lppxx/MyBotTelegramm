import telebot
import DataParser
from DatabaseHandler import DatabaseHandler


bot = telebot.TeleBot("TOKEN")

def logic():
    # initialization
    db = DatabaseHandler()
    db.fill_database(DataParser.fetch_data())
    return
    # if len(a) == 0:
    #     # err handling here
    #     return
    # bot greeting

# inputting for bot via function
@bot.message_handler(regexp="SOME_REGEXP")
def handle_message(check_book_name):
    check_book_name = input("Введите название произведения: ")
    pass
    # check exist in db
    #write it by your own self

    # review  these before coding
    if (check_book_name == book_names):


# code for mistake occassion
   # else:
        handle_message("Произведение, которое ты ввел, не существует в нашей базе данных")



    # do stuff
    pass

# function for message in checking and other occassions
@bot.message_handler(regexp="SOME_REGEXP")
def handle_message(message):
	pass


if __name__ == "__main__":
    logic()
