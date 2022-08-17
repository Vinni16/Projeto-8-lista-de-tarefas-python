#projeto original https://www.makerzine.com.br/python/python-bloco-de-notas-ou-tarefas/

opcao_do_menu = 0

def menu():
    print(25*"*")
    print("1 - Incluir nova tarefa")
    print("2 - Ver lista de tarefas")
    print("3 - Excluir tarefa salva")
    print("4 - Sair")
    print(25*"*")

#chama o menu, cria a lista vazia e pede a escolha do usuario
menu()
lista_de_tarefas = []
opcao_do_menu = int(input("\nDigite o número da opção desejada: "))


while True:
    if opcao_do_menu == 1:
        # reseta a opção do menu pra zero, cria uma variavel e pede o input,
        # adiciona o valor a lista vazia criada anteriormente
        # exibe a lista atualizada com o novo valor adicionado
        # no final chama  a função do menu e solicita o input para seguir.
        print("Opção escolhoda: 1 - Incluir nova tarefa")
        opcao_do_menu = 0
        tarefa = input("Digite a tarefa a ser adicionada: ")
        lista_de_tarefas.append(tarefa)
        print("\nSua lista de tarefas")
        print(lista_de_tarefas)
        print("\n")
        menu()
        opcao_do_menu = int(input("\nDigite o número da opção desejada: "))

    if opcao_do_menu == 2:
        print("")