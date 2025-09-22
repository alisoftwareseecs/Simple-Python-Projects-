marks = int(input("Enter your marks(0-100):"))

if marks >= 90:
    print("Your grade is: A")

elif marks >= 75:
    print("Your grade is: B")
elif marks >= 65:
    print("Your grade is: C")
elif marks >= 50:
    print("Your grade is: D")
else:
    print("Sorry, you failed. Better luck next time.")