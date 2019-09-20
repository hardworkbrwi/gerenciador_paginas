#!/usr/bin/bin/env python3
#-*- coding: utf-8 -*-

#gerenciadorPaginas.py
from builtins import list

from pagina import Pagina

class GerenciadorPaginas:

    def __init__(self):
        self._listaPaginas = []
        self._tamanhoTotalListaPaginas = 3
    '''
    def inserirPagina( self, pagina ):
        #pagina = Pagina()
        tamanhoLista = len( self._listaPaginas )
        inserido = False
        if( tamanhoLista < self._tamanhoTotalListaPaginas ):
            self._listaPaginas.append( pagina )

        else:
            indicePaginaMaisAntiga = self.buscaPaginaTempoMaisAntigo( self._listaPaginas )

            if( self.listaPaginas[indicePaginaMaisAntiga].bitR == 0 ):
                self.listaPaginas[indicePaginaMaisAntiga] = pagina
                self.listaPaginas[indicePaginaMaisAntiga].bitR = 1
                self.listaPaginas[indicePaginaMaisAntiga].tempoReferenciaTime()
                inserido = True

            else:
                self.listaPaginas[indicePaginaMaisAntiga].bitR = 0

        return inserido
        '''

    def inserirPagina( self, pagina, posicao = -1 ):
        if( posicao == -1 ):
            self.listaPaginas.append( pagina )
        else:
            self.listaPaginas[posicao] = pagina

    def inserirPaginaPosicao( self, pagina, posicao ):
        self.listaPaginas[posicao] = pagina

    def buscaPaginaTempoMaisAntigo( self ):
        tamanhoLista = len( self._listaPaginas )
        indiceMaisAntigo = 0

        for i in range( 0, tamanhoLista - 1 ):
            flagIndiceAntigoAlterada = False
            paginaAtual = self._listaPaginas[i]
            momentoCriacaoPaginaAtual = paginaAtual.momentoCriacao
            for j in range( i + 1, tamanhoLista ):
                proximaPagina = self._listaPaginas[j]
                momentoCriacaoProximaPagina = proximaPagina.momentoCriacao
                if( momentoCriacaoProximaPagina <  momentoCriacaoPaginaAtual ):
                    indiceMaisAntigo = j
                    i = indiceMaisAntigo
                    flagIndiceAntigoAlterada = True
                    break
            if( not flagIndiceAntigoAlterada ):
                break

        return indiceMaisAntigo

    def bitRLivre( self, indicePagina ):
        bitR = self._listaPaginas[indicePagina].bitR
        espacoMemoriaLiberada = False
        if( bitR == 0 ):
            espacoMemoriaLiberada = True

        return espacoMemoriaLiberada



    @property
    def listaPaginas(self):
        return self._listaPaginas

    @property
    def tamanhoTotalListaPaginas(self):
        return self._tamanhoTotalListaPaginas
