import os 
conversoes = []
while True :
    menu = input("escolha uma opção : C-fahnreiheit para celsius, S- sair, F - celsius para fahnreinheit :")
    match menu :
        case 'c' :
            os.system('cls')
            print("------conversão de fahnreinheit para celsius-------")
            temp = float(input("informe a temperatura em fahnreinheit: "))
            cel = float(temp - 32) * 5/9
            print(f'a conversão de {temp:.2f} em fahnreinheit para celsius é : {cel:.2f}')
            conversoes.append(cel)
            
        
            
        case 'f' :
            os.system('cls')
            print("------conversão de celsius para fahnreinheit")  
            temp = float(input("informe a temperatura em celsius : "))
            fah = float(temp * 9/5) + 32
            print (f'a conversão de {temp:.2f} em fahnreinheit para celsius é : {fah:.2f}')
            conversoes.append(fah)
            
            
        case 's' : 
            os.system('cls')
            print("saindo.....")
            print(f'registro de conversões : {conversoes}')
            break


  
  
    
        

