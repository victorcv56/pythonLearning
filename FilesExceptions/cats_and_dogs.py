
filenames = ['cats.txt', 'people.txt', 'dogs.txt']
def read_names(filename):
    """A simple method that will read pet names and display on screen"""
    for file in filenames:
        try:
            with open(file, 'r') as f:
                names = f.read()
                print(names)
                print('')
        except FileNotFoundError:
            pass

read_names(filenames)