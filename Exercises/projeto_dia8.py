#Calculadora

#qual sera a operacao? - input
#repetir operacoes - loop
# usar float pois pode ser numeros nao inteiros

while True:
    number1 = float(input("Enter the first number: "))
    operator = input("Enter the operatio(+, -, *, /): ")
    number2 = float(input("Enter the second number: "))

    if operator == "+":
     result = number1 + number2

    elif operator == "-":
        result  = number1 - number2

    elif operator == "*":
        result = number1 * number2

    elif operator == "/":
     result = number1 / number2

    else:
     print("Invalid operation.")
     result = None

    if result is not None:
          if result.is_integer():
                result = int(result)
    
                print("Result: ", result)

    again = input(" Do you want to calculate again? (y/n): ")

    if again != "y":
        print("Exiting calculator. Bye!")
        break


