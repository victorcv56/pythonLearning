#methods for dictionary with 2 keys(read, not-read), multiple values for keys
def reading_list(books):#create list of books user wants to read
    book = input("Please enter book name(enter 'q' to end): \n")
    while book != 'q':#while loop asking user to enter book until 'q' is entered
        books.append(book)
        book = input("Please enter book name(enter 'q' to end): \n")
    
    return books

def add_to_list(books):
    """Method to manipulate list and distribute into new list"""
    read = []
    not_read = []
    print("This is your reading list: \n")
    for book in books:
        current_book = input(f"Have you read {book}? (y/n)\n")
        if current_book == 'y':
            read.append(book)
        else:
            not_read.append(book)
    book_list = {'read': read, 'to_read': not_read}
    return book_list


def display_lists(book_lists):
    """Displays dictionary with lists of books read and not read"""
    for book_status, books in book_lists.items():
        print(f"Books {book_status} are: ")
        for book in books:
            print(f"{book}")
        print("")

books = []#list of books made by user
book_list = {}#dictionary with keys 'read' & 'not read' with lists as values

reading_list(books)
print('--------------------------------')
book_list = add_to_list(books)
print('----------------------------------')
display_lists(book_list)
