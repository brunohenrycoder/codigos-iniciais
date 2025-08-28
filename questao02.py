notas = []
contador = 1
while True : 
    
    if contador <= 3 :
      nota = float(input("digite a nota do usuario : "))
      notas.append(nota)
      contador += 1        
      media = sum(notas) / 3
    else : 
     if media >= 7 :
       print("aprovado")
       break
     elif media <7 and media >= 4 :
       print("reposição")
       break
     else :
       print("reprovado")
       break
       

       
       



    

    
