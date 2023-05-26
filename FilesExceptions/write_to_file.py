def write_text(filename, newfile):
    with open(filename, 'a') as f:
        contents = f.read()
        newfile.append(contents)


