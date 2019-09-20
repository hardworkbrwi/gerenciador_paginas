#!/usr/bin/bin/env python3
#-*- coding: utf-8 -*-

#gerenciadorPaginas.py
from builtins import list

from pagina import Pagina

class GerenciadorPaginas:

    def __init__(self):
        self._listaPaginas = []
        self._tamanhoTotalListaPaginas = 10

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



    @property
    def listaPaginas(self):
        return self._listaPaginas

    @property
    def tamanhoTotalListaPaginas(self):
        return self._tamanhoTotalListaPaginas
