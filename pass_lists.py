def add_to_list(not_read, read):
    """Method to create a list of read books and books i want to read"""
    print("This is your reading list: \n")
    for book in not_read:#for loop to pass books to new list
        pass_to_list = input(f"Have you read this book?(y/n) \n{book}\n")
        if pass_to_list == 'y':#if user enters yes, this will add book to already read list
            read.append(book)#if i answer yes it skips the next book
            #not_read.remove(book)


def reading_list(books):
    book = input("Please enter book name(enter 'q' to end): \n")
    while book != 'q':
        books.append(book)
        book = input("Please enter book name(enter 'q' to end): \n")
    
    return books

books = []
read = []
reading_list(books)
print("------------------------")
print("This is your book list: \n")
print("-----------------------")
count = 0
for book in books:
    count = 0#for loop that will print out reading list
    print(book)

add_to_list(books, read)

print("------------------------")
print("This is your 'next to read' list: ")#for loop that will print modified list
for book in books:
    print(book)
print("------------------------------")
print("These are your 'already read' books: ")#for loop that will print appended list
for book in read:
    print(book)

