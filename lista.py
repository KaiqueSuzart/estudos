lista = [13, 40, 32, 85, 12, 144, 56, 51, 9, 95]
maior = lista[0]
menor = lista[0]
soma = 0
 
for i in lista:
    soma += i
   
    if i > maior:
        maior = i
   
    if i < menor:
        menor = i
 
print(f"Soma: {soma} Maior: {maior} Menor: {menor} \nLista: {lista}")