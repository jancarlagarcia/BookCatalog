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
            print(f'\nO livro {titulo} Já Existe No Acervo!')

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
        print('\nVoltando ao MENU PRINCIPAL!')
        sleep(0.6)
        
        return


def nao_lidos():
    print('\n===   LIVROS NÃO LIDOS   ===\n' )

    livros_nao_lidos = {}

    for livro in acervo:
        if not livro['lido']:
            genero = livro['genero']

            if genero not in livros_nao_lidos:
                livros_nao_lidos[genero] = []
            
            livros_nao_lidos[genero].append(livro)

    if not livros_nao_lidos:
        print('Nenhum Livro Não Lido foi Encontrado!')
        pausar()
        return

    for genero in sorted(livros_nao_lidos):
        livros = livros_nao_lidos[genero]
        print(f'\nGênero: {genero}\n')
        

        for livro in livros:
            print(f"- Título: {livro['titulo']}")
            print(f"  Autor: {livro['autor']}\n")
        print('-' * 47)
    pausar()

def finalizados():
    print('\n===   LIVROS FINALIZADOS   ===\n' )
    
    livros_lidos = []

    for livro in acervo:
        if livro['lido']:  
            livros_lidos.append(livro)

    if not livros_lidos:
        print('Nenhum Livro Finalizado Foi Encontrado!')
        pausar()
        return
    
    livros_lidos_ordenados = sorted(
        livros_lidos,
        key = lambda livro: livro['classificacao'] or 0,
        reverse = True
    )
    
    for livro in livros_lidos_ordenados:
        if livro['classificacao']:
            estrelas = '⭐' * livro ['classificacao'] 
            
        else:
            estrelas = 'Sem Avaliação!'

        print(f"- Título: {livro['titulo']}")
        print(f"  Autor: {livro['autor']}")
        print(f"  Avaliação: {estrelas}\n")
    pausar()

def listar_biblioteca():
    print('\n===   ACERVO COMPLETO   ===\n' )

    ordem = sorted(acervo, key = lambda livro: livro['titulo'])

    for livro in ordem:
        print(f"- Título: {livro['titulo']}")
        print(f"  Autor: {livro['autor']}")
        print(f"  Gênero: {livro['genero']}\n")

    total = len(acervo)
    lidos = 0
    nao_lidos = 0

    for livro in acervo:
        if livro['lido']:
            lidos += 1
        else:
            nao_lidos += 1

    print(f'Esta Biblioteca Contém {total} {"Título" if total == 1 else "Títulos"}.')
    print(f'Desse Total, {nao_lidos} {"Não lido" if nao_lidos == 1 else "Não Lidos"} ', end='')
    print(f'e {lidos} {"Finalizados" if lidos == 1 else "Finalizados"}.')

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
