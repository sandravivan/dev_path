# compras = []
# Lista de compras: ["leite", "chocolate, "banana"]

month = (
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "Ssptember",
    "October",
    "November",
    "December"
    )

number = int(input("Enter a number from 1 to 12: "))
if 1 <= number <=12:
    print("The month is: ", month [number -1])
else:
    print ("Invalid number. Please enter a number between 1 and 12.")
    
