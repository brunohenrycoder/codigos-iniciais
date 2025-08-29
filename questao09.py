print("-----recibo de mercado-----")
n = int(input("quantos produtos da nossa loja você deseja ?  1 ou mais : "))
produtos = [
    {
        'nome': 'batata',
        'preço' : 5
    },
    {
        'nome' : 'macarrão',
        'preço' : 7
    },
    {
        'nome' : 'banana',
        'preço' : 3
    },
    {
        'nome' : 'pera',
        'preço' : 10
    },
    {
        'nome' : 'maçã',
        'preço' : 10
    },
    
]
if n == 1 :
 print(' escolha um desses produtos:  ') 
 for i,produto in enumerate(produtos,1):
   print(f'{i} - {produto['nome']} R${produto['preço']}')
 escolha = input("digite o numero do produto (1-5) : ")
 match escolha:
    case '1':
        print(f"Você escolheu {produtos[0]['nome']} por R${produtos[0]['preço']}")
    case '2':
        print(f"Você escolheu {produtos[1]['nome']} por R${produtos[1]['preço']}")
    case '3':
        print(f"Você escolheu {produtos[2]['nome']} por R${produtos[2]['preço']}")
    case '4':
        print(f"Você escolheu {produtos[3]['nome']} por R${produtos[3]['preço']}")
    case '5':
         print(f'Você escolheu {produtos[4]['nome']} por R${produtos[4]['preço']}')
    case _:
        print("Opção inválida.")  

elif n > 1:
    print('Escolha entre esses produtos:')
    for i, produto in enumerate(produtos, 1):
        print(f"{i} - {produto['nome']} R${produto['preço']}")
    escolhas = input(f"Digite os números dos {n} produtos separados por vírgula (ex: 1,3,4): ")
    indices = [int(x.strip()) - 1 for x in escolhas.split(',') if x.strip().isdigit()]
    selecionados = [produtos[i] for i in indices if 0 <= i < len(produtos)]
    if len(selecionados) != n:
        print("Quantidade ou opções inválidas.")
    else:
        total = sum(p['preço'] for p in selecionados)
        print("Você escolheu:")
        for p in selecionados:
            print(f"- {p['nome']} R${p['preço']}")
        print(f"Total a pagar: R${total}")
else:
    print("Quantidade inválida.")


    

