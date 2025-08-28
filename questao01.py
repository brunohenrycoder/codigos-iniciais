num = int(input("digite um numero a ser analisado :"))
pares = []
impar = []
for i in range(1,num ) :
    if i % 2 == 0 :
        pares.append(i)
    else :
        impar.append(i)

print(f'numeros pares até : {num} : {pares}')
print(f'numeros impares até : {num} : {impar}')






