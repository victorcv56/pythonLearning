"""Simple methods that can find and manipulate text files."""
import write_to_file
 
def count_words(filename):
    """Count the approximate number of words in a text"""
    try:
        with open(filename, encoding='utf-8') as f:#opens and closes file after code block is ran 
            content = f.read()
    except FileNotFoundError:
        print("File was not found!")
    else:
        words = content.split()
        word_count = len(words)
        print("The file {} contains {} words.".format(filename, word_count))


def find_words(filename):#still trying to fix in order to find a word 
    """Find how many times a word is in a file"""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    
    except FileNotFoundError:
        print("Could not find file: {}".format(filename))
    
    else:
        words_list = contents.split()#turns into huge list of words
        #now we need to navigate this list of words
        count = 0 #initiating count 
        word_to_find = input("Enter word to find in '{}': ".format(filename))
        for word in words_list:
            if word_to_find in words_list:
                count += 1
        print("'{}' was found {} times in text {}".format(word_to_find, count, filename))