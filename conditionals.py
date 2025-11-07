#if - se condicao verdadeira (se)
#elif - se a primeira FALSE, mas a segunda TRUE (se + se nao)
#else - se nenhuma for TRUE ( se nao)

name = input("Write your first and last name: ")
age = int(input("Write your age: "))
if age >= 21: 
    print("You can go!")
else:
    print("Sorry, but you are not old enoughn to enter.")
