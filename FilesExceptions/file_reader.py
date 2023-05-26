filename = 'learningPython.txt'

#Opening file and saving contents to a variable..
#with open(filename) as file_object:
 #   contents = file_object.read()


#Opening a file and reading it line by line..
#with open(filename) as file_object:
  #  for line in file_object:
   #     print(line.rstrip())

#Opening a file and saving lines to work outside 'with' block..
with open(filename) as fo:
    for line in fo:
        file1 = line.replace("python", "java")
        print(line.rstrip())
        print(file1.rstrip())
        print(line.rstrip())