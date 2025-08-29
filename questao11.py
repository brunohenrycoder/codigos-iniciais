num = int(input("Digite um número: "))
if num < 2:
    print("Não é primo")
else:
    primo = True
    for i in range(2, num):
        if num % i == 0:
            primo = False
            break
    if primo:
        print("Número é primo")
    else:
        print("Não é primo")