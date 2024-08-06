import re

def validar_telefone(numero):
    """
    Valida se o número de telefone está no formato (XX) 9XXXX-XXXX.
    
    Args:
    numero (str): A string representando o número de telefone.
    
    Returns:
    str: Mensagem indicando se o número de telefone é válido ou inválido.
    """
    # Define o padrão regex para o formato (XX) 9XXXX-XXXX
    padrao = r'^\(\d{2}\) 9\d{4}-\d{4}$'
    
    # Utiliza a função fullmatch para verificar se a string inteira corresponde ao padrão
    if re.fullmatch(padrao, numero):
        return "Número de telefone válido."
    else:
        return "Número de telefone inválido."

# Exemplos de uso
numeros_teste = [
    "(88) 98888-8888",  # Válido
    "(11)91111-1111",   # Inválido, falta o espaço após o código de área
    "225555-555",       # Inválido, falta o código de área e o 9 inicial
]

for numero in numeros_teste:
    print(f"{numero}: {validar_telefone(numero)}")
