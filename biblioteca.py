#AÇÕES DO SISTEMA
import os
from menu import pausar
from time import sleep
from dados import acervo



def confirmar(mensagem):
    while True:
        resp = input(f'{mensagem} [S/N] ').upper().strip()
        
        if resp == 'S':
            return True
        elif resp == 'N':
            return False
        else:
            print('Opção Inválida! Digite S ou N.')


def livro_existe(titulo):
    for livro in acervo:
        if livro['titulo'] == titulo:
            return True
    return False

            
def cadastrar_livro():
    print('\n===   CADASTRO DE LIVRO   ===\n' )

    while True:
        titulo = input('Título: ').strip().title()

        if livro_existe(titulo):
            print(f'\n O livro {titulo} Já Existe No Acervo!')

            if confirmar('Deseja Tentar Cadastrar Outro Livro?'):
                continue
            else:
                print('Voltando ao MENU PRINCIPAL...')
                sleep(0.6)
                return
        
        break

    autor = input('Autor: ').strip().title()
    genero = input('Gênero: ').strip().title()

    livro = {
        "titulo": titulo,
        "autor": autor,
        "genero": genero,
        "lido": False,
        "classificacao": None,
        "comentario": ""
        }

    acervo.append(livro)

    print('Livro Cadastrado com Sucesso!')

    if confirmar('Deseja Cadastrar Outro Livro?'):
        cadastrar_livro()

    else:
        print('Voltando ao MENU PRINCIPAL!')
        sleep(0.6)
        
        return


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
