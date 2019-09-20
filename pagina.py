#!/usr/bin/bin/env python3
#-*- coding: utf-8 -*-

#pagina.py

import datetime
import threading
import time


class Pagina:

    def __init__( self ):
        self._momentoCriacao = datetime.datetime.now()
        self._bitR = 1
        #threading.Thread( target=self.tempoReferenciaTime(), args=[] ).start()
        threading.Thread(target=self.tempoReferenciaTime).start()

    def tempoReferencia( self ):
        tempoVidaAtual = datetime.datetime.now().second
        while( tempoVidaAtual < self._momentoCriacao + 10 % 60 ):
            tempoVidaAtual = datetime.datetime.now().second

        self._bitR = 0

    def tempoReferenciaTime( self ):
        time.sleep(1)
        self._bitR = 0

    @property
    def bitR(self):
        return self._bitR

    @bitR.setter
    def bitR( self, bitR):
        self._bitR = bitR

    @property
    def momentoCriacao(self):
        return self._momentoCriacao

    @momentoCriacao.setter
    def momentoCriacao( self, momentoCriacao ):
        self._momentoCriacao = momentoCriacao

