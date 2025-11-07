price = float( input(" Enter the total price of your purchase: "))

if price >= 100:
    print ( "You get a 20% discount.")

elif price >= 50:
    print("You get a 10% discount.")

else:
    print("No discount this time.Thank you for shopping!")
