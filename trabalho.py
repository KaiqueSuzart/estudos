# Importação de bibliotecas necessárias
import random

# Função para imprimir o menu e obter a escolha do usuário
def exibir_menu():
    print("=== MENU ===")
    print("1. Iniciar diagnóstico")
    print("2. Verificar histórico de diagnósticos")
    print("3. Sair")
    escolha = input("Escolha uma opção: ")
    return escolha

# Função para realizar o diagnóstico
def iniciar_diagnostico():
    print("=== DIAGNÓSTICO AUTOMOTIVO ===")
    sintomas = input("Descreva os sintomas do veículo: ")
    # Simulação de diagnóstico aleatório
    problemas = ['Problema no motor', 'Problema na transmissão', 'Problema elétrico']
    diagnostico = random.choice(problemas)
    print(f"Diagnóstico preliminar: {diagnostico}")

# Função principal
def main():
    historico = []  # Lista para armazenar histórico de diagnósticos
    while True:
        escolha = exibir_menu()
        if escolha == '1':
            iniciar_diagnostico()
        elif escolha == '2':
            if historico:
                print("=== HISTÓRICO DE DIAGNÓSTICOS ===")
                for diagnostico in historico:
                    print(diagnostico)
            else:
                print("Nenhum diagnóstico registrado.")
        elif escolha == '3':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
