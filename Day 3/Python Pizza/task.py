print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

<<<<<<< HEAD
# todo: work out how much they need to pay based on their size choice.

bill = 0

=======
bill = 0
>>>>>>> 6e572c4318c91906a5d2b4445ba9b251897efd7d
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("You have chosen an invalid size.")

<<<<<<< HEAD
# todo: work out how much to add to their bill based on their pepperoni choice.
=======
>>>>>>> 6e572c4318c91906a5d2b4445ba9b251897efd7d
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

<<<<<<< HEAD
# todo: work out their final amount based on whether if they want extra cheese.
=======
>>>>>>> 6e572c4318c91906a5d2b4445ba9b251897efd7d
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")
<<<<<<< HEAD


=======
>>>>>>> 6e572c4318c91906a5d2b4445ba9b251897efd7d
