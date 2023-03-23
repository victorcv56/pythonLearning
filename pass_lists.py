def greet_users(names):
    """print a simple greeting to each user in list"""
    for name in names: 
        msg = f"Hello {name}, welcome to the matrix."
        print(msg)

usernames = ['lex', 'dan', 'fax', 'jer']
greet_users(usernames)