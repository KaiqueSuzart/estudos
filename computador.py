print('Quer um PC gamer??')


escolha = input('Tem Dinheiro? ')
if escolha == 'sim':
    print('Compra!!!')
elif escolha == 'não':
    escolha1 = input('Você trabalha? ')
    if escolha1 == 'sim':        
        escolha2 = input('Te pagam?')
        if escolha2 == 'sim':
            print('Compra!!!')
        elif escolha2 == 'não':
            escolha3 = input('Tem algo de valor?')
            if escolha3 =='sim':
                print('Venda')
                print('Compra o PC!!!')
            elif escolha3 =='não':
                escolha4 = input('Você tem um rim???')
                if escolha4 =='sim':
                    print('Venda um')
                    print('Compra!!!')
                elif escolha4 == 'não':
                    print('MENTIROSO!!!')
                    escolha4 = input('Você tem um rim???')
                if escolha4 =='sim':
                    print('Venda um')
                    print('Compra!!!')
                elif escolha4 == 'não':
                    print('MENTIROSO!!!')
    
    elif escolha1 == 'não':
        escolha5 = input('Tem algo de valor? ')
        if escolha5 =='sim':
            print('Venda')
            print('Compre o PC!!!')
        elif escolha5 == 'não':
            escolha6 = input('Você tem um rim? ')
            if escolha6 == 'sim':
                print('Venda um')
                print('Compre o PC!!!')
            elif escolha6 == 'não':
                print('MENTIROSO!!!')                       
        


# i = int(input('inicio: '))
# f = int(input('fim: '))

# while i <= f:
#     print(f'valor atual de x: {i}')

#     i+=1

