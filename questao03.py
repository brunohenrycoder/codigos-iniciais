calculo = []
for numeros in range(0,5+1) : 
    num = float(input("digite um numero : "))
    calculo.append(num)
    soma = sum(calculo)
    
print(f'a soma dos numeros da lista : {calculo} é : {soma}')
    
