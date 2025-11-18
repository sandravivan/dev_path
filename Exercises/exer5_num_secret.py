#Jogo de adivinhação

#No jogo, o usuário precisa adivinhar um número secreto

#Ele pode tentar várias vezes até acertar

#Lógica de pensamento:
#existe um numero secreto - variavel
#o usuario tenta adivinhar - input
#se errar, o jogo continua - loop / while
#se acertar, o jogo para - print mensagem

# perguntar - comparar - acertou? se sim,  para. Se nao, repete


secret_number = 2
guess = None

while guess != secret_number:
    guess = int(input("Enter your guess"))
   
    if guess!= secret_number:
        print("Wrong! Try again.")
        
print("You got it!")
