'''texto = input("informa um texto: ")
Vogais = "AEIOU"

for letra in texto:
    if letra.upper() in Vogais:
        print(letra, end="")
else:
    print()
    print("Executa no final do laço")'''
'''
for numero in range(0,51):
    print(numero, end=" ")'''

opcao =-1

while opcao !=0:
    opcao= int(input("[1] Sacar \n[2]Extrato \n[0]Sair\n: "))

    if opcao ==1:
        print("Sacando...")
    elif opcao ==2:
        print("Exibindo o extrato...")
else:
    print("obrigado por usar nosso sxistema bancario,ate logo!")
     
