nome = "kAiQuE"

print(nome.upper())
print(nome.lower())
print(nome.title())

texto = "  Olá mundo!     "

print(texto + ".")
print(texto.strip() + ".")#remove os espaços
print(texto.rstrip() + ".")#remove o espaço da direito
print(texto.lstrip() + ".")#remove o espaço da esquerda

menu = "Python"
print("####" + menu + "####")
print(menu.center(14))
print(menu.center(14, "#"))
print("P-y-t-h-o-n")
print("-".join(menu))