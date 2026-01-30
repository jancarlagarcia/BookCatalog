#AÇÕES DO SISTEMA
from menu import pausar
from time import sleep


def confirmar(mensagem):
    while True:
        resp = input(f'{mensagem} [S/N] ').upper().strip()
        
        if resp == 'S':
            return True
        elif resp == 'N':
            return False
        else:
            print('Opção Inválida! Digite S ou N.')

            
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
    while True:
        titulo = input('Digite o Título que Deseja Excluir: ')

        if  not confirmar(f'Tem Certeza que Deseja Excluir {titulo}? '): 
            print('Exclusão Encerrada!')
            sleep(0.6)
            return
        
        print(f'O livro {titulo} foi Excluído!')

        if not confirmar('Deseja Excluir Outro Exemplar?'):
            print('Voltando ao MENU PRINCIPAL...')
            sleep(0.6)
            return

    
def encerrar():
    return confirmar('Tem Certeza que Deseja Encerrar o Programa?')

