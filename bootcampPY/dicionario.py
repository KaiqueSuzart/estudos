pessoa = {"nome": "Guilherme", "idade": 28}


pessoa["telefone"] = "4002-8922" #{"nome": "Guilherme", "idade": 28,
#"telefone": "4002-8922"}

 
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

telefone = contatos["giovanna@gmail.com"]["telefone"]  # "3443-2121"​
print(contatos)