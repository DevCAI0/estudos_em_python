# Definindo uma lista de tarefas global para ser acessada pelas funções
tarefas = []

# Função para adicionar tarefa
def adicionar_tarefa():
    tarefa = input("Digite o nome da tarefa a ser adicionada: ")
    tarefas.append({"nome": tarefa, "completa": False})
    print(f"Tarefa '{tarefa}' adicionada com sucesso!")

# Função para ver todas as tarefas
def ver_tarefas():
    if not tarefas:
        print("Não há tarefas na lista.")
        return False  # Retorna False se a lista estiver vazia
    
    print("\nLista de tarefas:")
    for index, tarefa in enumerate(tarefas):
        status = "✔️" if tarefa["completa"] else "❌"
        print(f"{index + 1}. {tarefa['nome']} - {status}")
    return True  # Retorna True se houver tarefas

# Função para atualizar uma tarefa existente
def atualizar_tarefa():
    # Verifica se há tarefas antes de exibir
    if not tarefas:  # Verifica se a lista de tarefas está vazia
        print("Não há tarefas para atualizar.")
        return  # Sai da função, voltando ao menu
    
    ver_tarefas()  # Mostra as tarefas atuais
    
    while True:
        entrada = input("Digite o número da tarefa que deseja atualizar (ou SAIR para cancelar): ")
        if entrada.lower() == "sair":
            print("Operação cancelada. Voltando ao menu...")
            return  # Sai da função e volta ao menu
        
        try:
            indice = int(entrada) - 1
            if indice < 0 or indice >= len(tarefas):
                print("Número da tarefa inválido. Tente novamente.")
                continue  # Volta para pedir a entrada novamente
            
            nova_tarefa = input("Digite o novo nome da tarefa: ")
            tarefas[indice]["nome"] = nova_tarefa
            print("Tarefa atualizada com sucesso!")
            break  # Sai do loop após a atualização bem-sucedida
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")
            continue  # Volta para pedir a entrada novamente

# Função para completar uma tarefa existente
def completar_tarefa():
    # Verifica se há tarefas antes de exibir
    if not ver_tarefas():  # Verifica se a lista de tarefas está vazia
        return  # Sai da função, voltando ao menu
    
    while True:
        entrada = input("Digite o número da tarefa que deseja completar (ou SAIR para cancelar): ")
        if entrada.lower() == "sair":
            print("Operação cancelada. Voltando ao menu...")
            return  # Sai da função e volta ao menu
        
        try:
            indice = int(entrada) - 1
            if indice < 0 or indice >= len(tarefas):
                print("Número da tarefa inválido. Tente novamente.")
                continue  # Volta para pedir a entrada novamente
            
            if tarefas[indice]["completa"]:
                print("Esta tarefa já está marcada como completa.")
            else:
                tarefas[indice]["completa"] = True
                print(f"Tarefa '{tarefas[indice]['nome']}' marcada como completa!")
            
            break  # Sai do loop após a tarefa ser completada
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")
            continue  # Volta para pedir a entrada novamente
# Função para deletar tarefas completadas com a opção de escolher quais deletar ou deletar todas
def deletar_completadas():
    # Verifica se há tarefas completas
    tarefas_completas = [tarefa for tarefa in tarefas if tarefa["completa"]]
    
    if not tarefas_completas:
        print("Não há tarefas completadas para deletar.")
        return  # Sai da função, voltando ao menu

    print("\nTarefas completadas:")
    for index, tarefa in enumerate(tarefas_completas, start=1):
        print(f"{index}. {tarefa['nome']}")

    # Pergunta ao usuário o que ele deseja fazer
    opcao = input("Digite o número da tarefa que deseja deletar (ou 'TODAS' para deletar todas as tarefas completadas, ou 'SAIR' para cancelar): ")

    if opcao.lower() == "sair":
        print("Operação cancelada. Voltando ao menu...")
        return  # Sai da função, voltando ao menu

    elif opcao.lower() == "todas":
        # Remove todas as tarefas completas
        tarefas[:] = [tarefa for tarefa in tarefas if not tarefa["completa"]]
        print("Todas as tarefas completadas foram deletadas com sucesso!")

    else:
        try:
            # Transforma a entrada do usuário em um número
            indice = int(opcao) - 1
            if indice < 0 or indice >= len(tarefas_completas):
                print("Número inválido. Voltando ao menu...")
                return  # Volta ao menu se o número for inválido
            
            # Encontra a tarefa completa na lista original e remove
            tarefa_a_deletar = tarefas_completas[indice]
            tarefas.remove(tarefa_a_deletar)
            print(f"Tarefa '{tarefa_a_deletar['nome']}' deletada com sucesso!")
        
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido ou 'TODAS' para deletar todas.")


# Loop principal do menu
while True:  # Criamos um loop infinito, que só vai parar se o usuário digitar "6" para sair
    print("\nMenu de Gerenciamento de Lista de Tarefas: ")
    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Atualizar tarefa")
    print("4. Completar tarefa")
    print("5. Deletar tarefas completadas")
    print("6. Sair")
    print("-" * 50)
    
    # Recebe a escolha do usuário
    entrada = input("Digite um número do Menu: ")
    
    # Verifica a escolha do usuário e chama a função correspondente
    if entrada == "1":
        adicionar_tarefa()
    elif entrada == "2":
        ver_tarefas()
    elif entrada == "3":
        atualizar_tarefa()
    elif entrada == "4":
        completar_tarefa()
    elif entrada == "5":
        deletar_completadas()  # Esta função ainda não foi implementada
    elif entrada == "6":
        print("Programa finalizado.")
        break  # Sai do loop e encerra o programa
    else:
        print("Opção inválida. Tente novamente.")
    
    print("-" * 50)
