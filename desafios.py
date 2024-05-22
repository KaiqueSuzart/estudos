"""
print('CALCULADORA DE MULTIPLICAÇÃO')
num1 = float(input('digite o primeiro numero: '))
num2 = float(input('Digite o segundo numero: '))

Result = num1*num2
print(f'O resultado da conta deu {Result}')
"""
"""
print('CALCULADORA DE POTENCIA')
num1 = float(input('Digite a Base: '))
num2 = float(input('Digite o Expoente: '))

result = num1**num2
print(f'O resultado é {result}')
"""
"""
print('Calculadora de potencia soma')
num1 = float(input('Digite o primeiro numero: '))
num2 = float(input('Digite o segundo numero: '))

resul1 = num1*num1
result2 = num2*num2
resultado = result2+resul1
print(f'A soma das potencias é {resultado}')"""
"""
num1= int(input('Digite o primeiro numero: '))
num2= int(input('Digite o segundo numero: '))
result1 = num1 +1
result2 = num2 +1
print(f'Os numeros consecutivos são {result1} e {result2}')
"""
'''
print('calculadora de duração do jogo')
inicio= float(input('Horario que começou o jogo: '))
fim= float(input('Horario que terminou o jogo: '))
inicio >1
fim <24
result1=fim-inicio# quando o inicio é maior que o fim
if result1 <=0:
    result2 =(result1 +24)
    print(f'A duração do jogo é de: {result2} Horas')

elif result1>=0:
   result2=result1 *+1
   print(f'a duração do jogo é de: {result1} Horas')

else:
    result1= {inicio+fim} + 24
'''
'''
print('Funções')
print(''''''
[1]a área do triângulo retângulo que tem A por base e C por altura: 
[2] a área do círculo de raio C. (π = 3.14159): 
[3] a área do trapézio que tem A e B por bases e C por altura: 
[4] a área do quadrado que tem lado B:
[5]a área do retângulo que tem lados A e B:
[6] o perímetro do retângulo que tem lados A e B:
'''#)
'''
opçao=float(input('Escolha a opção: '))

if opçao == 1:
    numb1=float(input('Escolha a base: '))
    numb3=float(input('Escolha a altura: '))
    result = (numb1*numb3) / 2
    print(f'A aréa do Triangulo é {result:.2f} Metros') 

elif opçao == 2:
    numb3=float(input('Escolha o Raio '))
    result = (numb3*numb3) * 3.14159
    print(f'A aréa do Circulo é {result:.2f} Metros')

elif opçao == 3:
    numb1=float(input('Escolha a base 1: '))
    numb2=float(input('Escolha a base 2: '))
    numb3=float(input('Escolha a altura: '))     
    result = ((numb1+numb2) * numb3) /2
    print(f'A área do trapézio é {result:.2f} Metros')

elif opçao== 4:
    numb1=float(input('Escolha a altura: '))
    result = numb1 *2
    print(f'A área do quadrado é {result:.2f} Metros')

elif opçao==5:
    numb1=float(input('Escolha a base: '))
    numb2=float(input('Escolha a altura: '))
    result = numb1 *numb2
    print(f'A área do retangulo é {result:.2f} Metros')

elif opçao==6:
    numb1=float(input('Escolha a base:'))
    numb2=float(input('Escolha a altura: '))
    result= (numb1*numb2)*2
    print(f'A Perímetro do retangulo é {result:.2f} Metros')
'''
numb1=float(input('digite a primeira nota: '))
numb2=float(input('digite a segunda nota: '))
numb3=float(input('digite a terceira  nota: '))

media=(numb1+numb2+numb3)/3

if (media >= 9 and media <=10):
    conceito = 'A'
    mensagem = 'Excelente'
    status = 'Aprovado'
elif(media >=8 and media <=9):
        conceito = 'B'
        mensagem = 'Otimo'
        status = 'Aprovado'
elif(media >=7 and media <=8):
    conceito = 'C'
    mensagem = 'Bom'
    status = 'Aprovado'
elif(media >=6 and media <=7):
    conceito = 'D'
    mensagem = 'Regular'
    status = 'Aprovado'
elif(media >=5 and media <=6):
    conceito = 'E'
    mensagem = 'Ruim'
    status = 'Reprovado / Exame'
else:
    conceito = 'F'
    mensagem = 'Se fudeu KKKKKKK'
    status = 'Reprovado'

match conceito:
     case 'A':
         print(f'{mensagem} \n {conceito}\n {status}')
     case 'B':
        print(f'{mensagem} \n {conceito}\n {status}')
     case 'C':
        print(f'{mensagem} \n {conceito}\n {status}')
     case 'D':
        print(f'{mensagem} \n {conceito}\n {status}')
     case 'E':
        print(f'{mensagem} \n {conceito}\n {status}')
     case 'F':
        print(f'{mensagem} \n {conceito}\n {status}')
 

