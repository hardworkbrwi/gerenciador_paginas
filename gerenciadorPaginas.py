#!/usr/bin/bin/env python3
#-*- coding: utf-8 -*-

#gerenciadorPaginas.py
from builtins import list

from pagina import Pagina

class GerenciadorPaginas:

    def __init__(self):
        self._listaPaginas = []
        self._maxPaginasLista = 10

    def inserirPagina( self, pagina, posicao = -1 ):
        if( posicao == -1 ):
            self.listaPaginas.append( pagina )
        else:
            self.listaPaginas[posicao] = pagina

    def buscaIndicePaginaTempoMaisAntigo( self ):
        menorTempoCriacao = self._listaPaginas[0].momentoCriacao
        indiceMenorTempoCriacao = 0
        for index, pagina in enumerate(self._listaPaginas):
            tempoCriacaoAtual = pagina.momentoCriacao
            if tempoCriacaoAtual < menorTempoCriacao:
                menorTempoCriacao = tempoCriacaoAtual
                indiceMenorTempoCriacao = index

        return indiceMenorTempoCriacao


    def bitRLivre( self, indicePagina ):
        bitR = self._listaPaginas[indicePagina].bitR
        espacoMemoriaLiberada = False
        if( bitR == 0 ):
            espacoMemoriaLiberada = True

        return espacoMemoriaLiberada

    def exibirListaPaginas(self):
        grade = 90 * '_'
        print(grade)
        print("{}|{}|{}".format( "ID".center(10), "MOMENTO CRIAÇÃO".center(40), "BIT_R".center(20) ) )
        print(grade)
        for index, pagina in enumerate(self._listaPaginas):
            print("{}|{}|{}".format(str( index + 1 ).ljust(10),
                                       str( pagina.momentoCriacao ).ljust(40),
                                       str( pagina.bitR ).ljust(20)) )

        print(grade)

    @property
    def listaPaginas(self):
        return self._listaPaginas

    @property
    def maxPaginasLista(self):
        return self._maxPaginasLista
