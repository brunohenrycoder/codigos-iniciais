print("------identificador de palindromos--------")
texto = input("digite uma palavra ou frase : ")
if texto == texto[::-1]:
    print("é um palindromo")
else :
    print("não é um palindromo")