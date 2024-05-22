'''Desafio 1
num1 = int(input('digite seu numero: '))
if num1 >= 100:
   num1 += 150
print(num1)
'''

'''Desafio 2
num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))
if num1 % num2 == 0:
   print(f'A divisão do {num1} por {num2} é exata' )
else:
   print('essa conta nao é exata')'''

'''
print('*-* Cálculo do IMC *-*')
#entrada
peso = float(input('Peso: '))
altura = float(input('Altura: '))
#processamento
imc = peso / (altura * altura) # ou altura ** 2
if imc < 18.5:
    print(f'Imc: {imc : .1f} - Peso baixo!')
elif imc >= 18.5 and imc <= 24.99:
    print(f'Imc: {imc : .1f} - Norm al')
elif imc >= 25 and imc <= 29.99:
    print(f'Imc: {imc : .1f} - Sobrepeso!')
else:
    print(f'Imc: {imc : .1f} - Obesidade!')
'''




'''
kwh = int(input('Digite o valor do gasto (kwh): '))
valor_conta = 0
if kwh < 150:
    print('valor do kwh é 0,20$')
elif kwh >= 150 and kwh < 500:
    print('valor do kwh é 0,25$')
elif kwh >= 500:
    print("valor do kwh é 0,30$")
else :
    print('Valor minimo da conta é de 11,90$')
'''

'''
gasto_em_kwh = int(input('Digite o valor do gasto (kWh): '))
valor_conta = 0
if(gasto_em_kwh < 150):
    valor_conta = gasto * 0.20
elif(gasto_em_kwh >= 150 and gasto_em_kwh < 500):
    valor_conta = gasto * 0.25
else:
    valor_conta = gasto * 0.30
valor_conta += 11.90
print(f'O gasto foi de R$ {valor_conta:.2f}')
'''



'''
num = int(input('Digite um numero: '))#le o numero digitado pelo usuario

#inicializamos index = 1, por que queremos começar a contar a partir do 1
#poderiamos iniciar como index = 0, para contar a partir do 0 :)
index = 1

#enquanto index for menor ou igual ao numero digitado pelo usuario, faremos esse loop
while index <= num:
    if(index % 2 == 0):#se o resto da divisão de index por 2 for 0, então index é par
        print(f'{index} é par')
    else:
        print(f'{index} é impar')#se não, index é impar
    index += 1 #incrementamos index em 1, para que possamos verificar o proximo numero
'''
