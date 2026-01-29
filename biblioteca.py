#AÇÕES DO SISTEMA
from menu import pausar
from time import sleep

def cadastrar_livro():
    print('Cadastrar Livro (em breve).')
    pausar()


def nao_lidos():
    print('Listar Livros Não Lidos (em breve)')
    pausar()


def finalizados():
    print('Listar Livros Finalizados (em breve)')
    pausar()
    

def listar_biblioteca():
    print('Listar Biblioteca Completa (em breve)')
    pausar()
    

def marcar_como_finalizado():
    print('Marcar Livro como Finalizado (em breve)')
    pausar()
    

def excluir_livro():
    continuar_excluindo = True

    while continuar_excluindo:
        titulo = input('Digite o Título que Deseja Excluir: ')

        while True:
            resp = input(f'Tem Certeza que Deseja Excluir {titulo}? [S/N] ').upper().strip()

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

    
def encerrar():
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

