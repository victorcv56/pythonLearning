from name_function import get_formatted_name as full_name

print("Enter 'q' anytime to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("\nPlease give me a last name: ")
    if last == 'q':
        break

    formatted_name = full_name(first, last)
    print("\nNeatly formatted name: {}".format(formatted_name))