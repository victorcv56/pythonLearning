"""Learn to write user input to a file"""

#function that will take a list as arg and append to existing file
def new_file(tips):
    filename = input("Enter date(ddmmyy): ")
    filepath = filename + ".txt"
    
    f = open(filepath, "a")
    f.write(tips)
    f.close()



