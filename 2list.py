#defining method that will take two arguments 
#and a third one if given..
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return full name, neatly formatted."""
    if middle_name: 
        full_name = f"{first_name} {middle_name} {last_name}"
    else: 
        full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name("jimi", "hendrix")
print(musician)

another_musician = get_formatted_name("Amy", "Winehouse", "F.")
print(another_musician)