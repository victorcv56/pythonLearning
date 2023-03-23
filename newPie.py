import random

name = input("Hola, como te llamas: \n")
print(f"\nHola {name.title()},\n Quieres jugar a adivinar el numero?\n")

play = (input("Si o No?:\n"))
if play == "si":
    print("\nJuguemos!!")
else:
    print("\nBueno pues :(")
    quit()

num = random.randint(0, 30)
ans= int(input("Adivina un numero de 1 - 30: \n"))


while ans != num:
    if ans > num:
        print("Un poco alto! Intenta de nuevo!\n")
    elif ans < num:
        print("Un poco bajo! Intenta de nuevo!\n")
    elif ans == num:
        print(f"Muy bien!! Lo hiciste {name}!!!")
    ans = int(input("Intenta de nuevo: "))
    if ans == num:
        print(f"MUY BIEEN!! LO HICISTE {name.upper()}!!!")


