import os
n = int(input("digite um numero limite :"))
os.system('cls')
print(f'dobro dos numeros de 1 até {n}')
for i in range(1,n+1) :
    multi = i * 2
    print(f'{i}:{multi}')


    