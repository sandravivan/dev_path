 # ATM Simulador

balance = 500
choice = " "

while balance > 0:
    print(f"Current balance: ${balance}")

    print("1- Withdraw money")
    print("2- Exit")

    choice = input("Enter your choice (1 or 2): ")

    #Option 1: Withdraw
    if choice == "1":
        withdraw_amount = int(input("Enter withdraw amount: "))
        if withdraw_amount <=0:
         print("Invalid amount.")

        elif withdraw_amount > balance:
         print("Insuficient funds>")

        else:
         balance -= withdraw_amount
         print(f"You withdrew ${withdraw_amount}")
         print(f"New balance: ${balance}")

    elif choice =="2":
     print("Thank you")
    break

else:
    print("Invalid option.")

if balance == 0:
     print(" Your balance is now $0. No more withdraws are possible.")


      
            


