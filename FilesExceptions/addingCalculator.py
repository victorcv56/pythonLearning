
flag = True

while flag:
    try: 
        num1 = int(input("Enter first number: "))
    except (ValueError, TypeError):
        print("Please enter a valid number.")
    else: 
        flag = False

print(num1)
while not flag:
    try: 
        num2 = int(input("Please enter second number: "))
    except(ValueError, TypeError):
        print("Please enter a valid number.")
    else: 
        flag = True

print(num1 + num2)
# try:
#     num2 = int(input("Enter second number: "))
# except (ValueError, TypeError):
#     print("Please enter a number")

# else:
#     result = num1 + num2