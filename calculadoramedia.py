# Função para calcular a nota necessária no trabalho final
def calcular_nota_necessaria(media_provas, media_sprints, media_desejada):
    # Média ponderada das provas e sprints
    media_ponderada = ((media_provas + media_sprints) / 2) * 0.4
    
    # Calculando a nota necessária no trabalho final
    nota_trabalho_final = (media_desejada - media_ponderada) / 0.6
    return round(nota_trabalho_final, 2)

# Função para calcular a frequência atual e verificar se está acima de 75%
def verificar_frequencia(total_aulas, faltas):
    aulas_faltadas = faltas * 2
    frequencia = ((total_aulas - aulas_faltadas) / total_aulas) * 100
    return frequencia, frequencia >= 75

# Função para calcular o número máximo de faltas permitido para manter a frequência acima de 75%
def calcular_faltas_permitidas(total_aulas):
    max_aulas_faltadas = total_aulas * 0.25
    max_faltas = max_aulas_faltadas // 2
    return int(max_faltas)

# Lista de disciplinas e o número total de aulas
disciplinas = [
    {'nome': 'ARTIFICIAL INTELLIGENCE & CHATBOT', 'aulas': 80},
    {'nome': 'BUILDING RELATIONAL DATABASE', 'aulas': 80},
    {'nome': 'COMPUTATIONAL THINKING USING PYTHON', 'aulas': 160},
    {'nome': 'DOMAIN DRIVEN DESIGN USING JAVA', 'aulas': 160},
    {'nome': 'FRONT-END DESIGN ENGINEERING', 'aulas': 160},
    {'nome': 'SOFTWARE ENGINEERING AND BUSINESS MODEL', 'aulas': 160}
]

# Lista para armazenar as informações de cada disciplina
informacoes_disciplinas = []

# Loop para adicionar informações de disciplinas
for disciplina in disciplinas:
    print(f"\nDigite as notas para a disciplina: {disciplina['nome']}")
    prova1 = float(input("Digite a nota da primeira prova: "))
    prova2 = float(input("Digite a nota da segunda prova: "))
    sprint1 = float(input("Digite a nota do primeiro sprint: "))
    sprint2 = float(input("Digite a nota do segundo sprint: "))
    faltas = int(input(f"Quantas faltas você já teve em {disciplina['nome']}? "))
    
    # Calculando a média das provas e sprints
    media_provas = (prova1 + prova2) / 2
    media_sprints = (sprint1 + sprint2) / 2
    
    # Verificar a frequência atual
    frequencia, acima_de_75 = verificar_frequencia(disciplina['aulas'], faltas)
    
    # Calcular o número máximo de faltas permitidas
    faltas_permitidas = calcular_faltas_permitidas(disciplina['aulas'])
    
    # Armazenando as informações da disciplina
    informacoes_disciplinas.append({
        'disciplina': disciplina['nome'],
        'media_provas': media_provas,
        'media_sprints': media_sprints,
        'faltas': faltas,
        'frequencia': frequencia,
        'acima_de_75': acima_de_75,
        'faltas_permitidas': faltas_permitidas
    })

# Solicitar a média desejada
media_desejada = float(input("\nDigite a média desejada: "))

# Imprimir a nota necessária no trabalho final e a frequência para cada disciplina
print("\nNotas necessárias no trabalho final e frequências:")
for disciplina_info in informacoes_disciplinas:
    nota_necessaria = calcular_nota_necessaria(disciplina_info['media_provas'], disciplina_info['media_sprints'], media_desejada)
    status_frequencia = "Acima de 75%" if disciplina_info['acima_de_75'] else "Abaixo de 75%"
    faltas_restantes = disciplina_info['faltas_permitidas'] - disciplina_info['faltas']
    print(f"Disciplina: {disciplina_info['disciplina']}, Nota necessária no trabalho final: {nota_necessaria}, Faltas: {disciplina_info['faltas']}, Frequência: {disciplina_info['frequencia']}%, Status: {status_frequencia}, Faltas restantes permitidas: {faltas_restantes}")

