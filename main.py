#PARTE VISÍVEL DO SISTEMA
from time import sleep
from menu import (
    limpar_tela,
    mostrar_titulo,
    mostrar_menu
)

from biblioteca import(
    cadastrar_livro,
    nao_lidos,
    finalizados,
    listar_biblioteca,
    marcar_como_finalizado,
    excluir_livro,
    encerrar
)

mostrar_titulo()

while True:
    limpar_tela()
    mostrar_menu()

    try:
        opcao = int(input('\nEscolha uma Opção: '))
    
    except ValueError:
        print('\nEntrada Inválida! Digite Apenas Números.')
        continue


    if opcao == 1:
        limpar_tela()
        cadastrar_livro()
    
    elif opcao == 2:
        limpar_tela()
        nao_lidos()
    
    elif opcao == 3:
        finalizados()
    
    elif opcao == 4:
        limpar_tela()
        listar_biblioteca()
    
    elif opcao == 5:
        marcar_como_finalizado()
    
    elif opcao == 6:
        excluir_livro()

    elif opcao == 7:
        if encerrar():
            print('\nEncerrando BookCatalog...\n')
            sleep(0.6)
            break

    else:
        print('Opção Inválida! Tente Novamente.')
        continue
