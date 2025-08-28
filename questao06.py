print("-------loja de produtos naturais-------")
produtos = [
{
       'nome' : 'farinha de amendoim',
       'preço': 4 
},
{
       'nome' : 'amendoim triturado',
       'preço': 6 
},
{
       'nome' : 'whey protein growth',
       'preço': 150 
},
]
for produto in produtos :
    print(f'nome : {produto['nome']}, preço : R${produto['preço']}')