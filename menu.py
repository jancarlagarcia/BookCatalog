from time import sleep
import os

def limpar_tela():
    os.system('cls')

def pausar():
    input('Pressione ENTER para voltar ao MENU PRINCIPAL!')


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

    try:
        opcao = int(input('\nEscolha uma Opção: '))
    
    except ValueError:
        print('\nEntrada Inválida! Digite Apenas Números.')
        continue


    if opcao == 1:
        print('Cadastrar Livro (em breve).')
        pausar()
    
    elif opcao == 2:
        print('Listar Livros Não Lidos (em breve)')
        pausar()
    
    elif opcao == 3:
        print('Listar Livros Finalizados (em breve)')
        pausar()
    
    elif opcao == 4:
        print('Listar Biblioteca Completa (em breve)')
        pausar()
    
    elif opcao == 5:
        print('Marcar Livro como Finalizado (em breve)')
        pausar()
    
    elif opcao == 6:
        continuar_excluindo = True

        while continuar_excluindo:
            excluir_livro = input('Digite o Título que Deseja Excluir: ')

            while True:
                resp = input(f'Tem Certeza que Deseja Excluir {excluir_livro}? [S/N] ').upper().strip()

                if resp == 'S':
                    print('LIVRO EXCLUÍDO COM SUCESSO!')

                    while True:
                        op = input('Deseja Excluir Outro Exemplar? [S/N] ').upper().strip()

                        if op == 'S':
                            break

                        elif op == 'N':
                            print('Voltando ao MENU PRINCIPAL...')
                            sleep(0.6)
                            continuar_excluindo = False
                            break

                        else:
                            print('Opção Inválida! Digite S ou N.')
                            
                    break

                elif resp == 'N':
                    print('Exclusão Encerrada.')
                    sleep(0.6)
                    continuar_excluindo = False
                    break

                else: 
                    print('Opção inválida! Digite S ou N.')
    
    elif opcao == 7:
        while True:
            resp = input('Tem Certeza que Deseja Encerrar o Programa? [S/N] ').upper().strip()

            if resp == 'S':
                print('\nEncerrando BookCatalog...\n')
                exit()

            elif resp =='N':
                print('Voltando ao MENU PRINCIPAL...')
                break

            else:
                print('Opção Inválida! Digite S ou N.')
                continue

    else:
        print('Opção Inválida! Tente Novamente.')
        continue
