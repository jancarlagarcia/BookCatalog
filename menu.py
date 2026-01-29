#SÓ FUNÇÕES DE MENU

import os

def limpar_tela():
    os.system('cls')

def pausar():
    input('Pressione ENTER para voltar ao MENU PRINCIPAL! ')

#TÍTULO
def mostrar_titulo():
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
