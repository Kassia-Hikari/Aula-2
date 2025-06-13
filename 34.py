agenda = []

def adicionar_compromisso():
    data = input("Digite a data: ")
    compromisso = input("Digite o compromisso: ")
    agenda.append((data, compromisso))

def exibir_compromissos():
    if not agenda:
        print("Nenhum compromisso cadastrado.\n")
        return
    print("Compromissos cadastrados: ")
    for data, compromisso in sorted(agenda):
        print(f"{data} - {compromisso}")
    print()

def buscar_por_data():
    data = input("Digite a data para buscar: ")
    encontrados = [c for d, c in agenda if d == data]
    if encontrados:
        print(f"Compromissos em {data}:")
        for c in encontrados:
            print(f"- {c}")
    else:
        print("Nenhum compromisso nessa data.")
    print()

while True:
    print("Agenda de Compromissos")
    print("1. Adicionar compromisso")
    print("2. Exibir compromissos")
    print("3. Buscar por data")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        adicionar_compromisso()
    elif opcao == '2':
        exibir_compromissos()
    elif opcao == '3':
        buscar_por_data()
    elif opcao == '4':
        break
    else:
        print("Opção inválida. Tente novamente.\n")
