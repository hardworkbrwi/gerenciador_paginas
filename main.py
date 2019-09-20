from gerenciadorPaginas import GerenciadorPaginas
from pagina import Pagina

if __name__ == '__main__':
    gerenciadorPaginas = GerenciadorPaginas()

    while( True ):


        p1 = Pagina()
        quantidadeAtualLista = len( gerenciadorPaginas.listaPaginas )
        tamanhoLista = gerenciadorPaginas.tamanhoTotalListaPaginas
        if( quantidadeAtualLista < tamanhoLista ):
            gerenciadorPaginas.inserirPagina( p1 )
            print("pagina inserida na posição {}".format(quantidadeAtualLista))

        else:
            indicePaginaMaisAntiga = gerenciadorPaginas.buscaPaginaTempoMaisAntigo()

            if( gerenciadorPaginas.bitRLivre( indicePaginaMaisAntiga ) ):
                #gerenciadorPaginas.inserirPaginaPosicao( p1, indicePaginaMaisAntiga )
                gerenciadorPaginas.inserirPagina(p1, indicePaginaMaisAntiga)
                print("indice página mais antiga {}".format(indicePaginaMaisAntiga))

            else:
                print("indice {} não está liberado".format(indicePaginaMaisAntiga))

    '''
    p2 = Pagina()
    gerenciadorPaginas.inserirPagina(p2)
    print("bitR da página {}: {}".format(p2,p2.bitR))

    p3 = Pagina()
    gerenciadorPaginas.inserirPagina(p3)
    print("bitR da página {}: {}".format(p3,p3.bitR))
    
    '''
