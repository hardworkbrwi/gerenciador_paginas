import os

from gerenciadorPaginas import GerenciadorPaginas
from impressao import Impressao
from pagina import Pagina


if __name__ == '__main__':
    gerenciadorPaginas = GerenciadorPaginas()

    while( True ):

        opcao = Impressao.menu()

        if( opcao == 1 ):

            quantidadePaginasNaLista = len( gerenciadorPaginas.listaPaginas )
            maxPaginasLista = gerenciadorPaginas.maxPaginasLista

            pagina = Pagina()
            if ( quantidadePaginasNaLista < maxPaginasLista ):
                gerenciadorPaginas.inserirPagina( pagina )
                print( "A página foi inserida na posição {}\n".format(quantidadePaginasNaLista) )

            else:
                indicePaginaMaisAntiga = gerenciadorPaginas.buscaIndicePaginaTempoMaisAntigo()

                if ( gerenciadorPaginas.bitRLivre(indicePaginaMaisAntiga) ):
                    gerenciadorPaginas.inserirPagina( pagina, indicePaginaMaisAntiga )
                    print( "A posição {} da lista foi substituida\n".format(indicePaginaMaisAntiga) )

                else:
                    print( "A posição {} da lista não está liberado\n".format(indicePaginaMaisAntiga) )

        elif( opcao == 2 ):
            gerenciadorPaginas.exibirListaPaginas()

        elif( opcao == 3 ):
            pid = os.getpid()
            os.kill( pid, 9 )

        else:
            print( "A opcao {} é inválida".format(opcao) )