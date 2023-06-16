import json
"""Learn to write user input to a file"""

#function that will take a list as arg and append to existing file
def log_tips(tips, total):
    filename = input("Enter date(mm-dd-yy): ")
    filepath = filename + ".txt"
    
    with open(filepath, 'a') as fo:
        fo.write(filename + "\n")
        count = 1
        for tip in tips:
            fo.write("\tDay #{}: ".format(count))
            fo.write("{}\n".format(tip))
            count += 1
        fo.write("\nYour total tips this week: {}\n".format(total))
    
    return filepath

def write_info(filepath, hours, days, wage, tips):
    with open(filepath, 'a') as fo:
        fo.write("You worked {:.2f} hours in {} days this week.\n".format(hours, days))
        fo.write("You made {:.2f}/hr and made {} total in tips.\n\n".format(wage, tips))

def get_data():
    """Method that will use json to retrieve data"""
    filename = 'logged_tips.json' #name of json file
    #try block that will look for file and return data if found
    try:
        with open(filename) as f:
            data = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return data

def save_data():
    """Method that will create new data file"""
    filename = 'logged_tips.json'
    try:
        with open(filename, 'w') as f:
            data = json.dump(filename, f)

      