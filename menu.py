#Título
print('-' * 60)
print(f"{'BOOKCATALOG':^60}")
print('-' * 60)

#MENU
def mostrar_menu():
    print('\nMENU PRINCIPAL')
    print('\n[1] - Cadastrar Livro Novo')
    print('[2] - Listar Livros Não Lidos')
    print('[3] - Listar Livros Finalizados')
    print('[4] - Listar Biblioteca Completa')
    print('[5] - Marcar Livro como Finalizado')
    print('[6] - Apagar Livro')
    print('[7] - Sair')

#LOOP
while True:
    mostrar_menu()
    opcao = int(input('\nEscolha uma Opção: '))

    if opcao == 1:
        print('Cadastrar Livro (em breve).')
    
    elif opcao == 2:
        print('Listar Livros Não Lidos (em breve)')
    
    elif opcao == 3:
        print('Listar Livros Finalizados (em breve)')
    
    elif opcao == 4:
        print('Listar Biblioteca Completa (em breve)')
    
    elif opcao == 5:
        print('Marcar Livro como Finalizado (em breve)')
    
    elif opcao == 6:
        print('Apagar Livro')
    
    elif opcao == 7:
        print('\nEncerrando BookCatalog...')
        break

    else:
        print('Opção Inválida! Tente Novamente.')
        continue
