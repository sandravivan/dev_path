#verificando a nota de um aluno

grade = float(input("Please, enter your final grade: "))

if grade >= 7: 
    print("Congratulations! You pass the year.")

elif grade >=5:
    print("You are on academic probation. Study more and try again.")

else:
    print("Unfortunately, you failed. Try again next year.")

