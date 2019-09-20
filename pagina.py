#!/usr/bin/bin/env python3
#-*- coding: utf-8 -*-

#pagina.py

import datetime
import threading
import time

class Pagina:
    '''
    Classe contendo telas de exibição do gerenciador de tarefas
    '''

    def __init__( self ):
        self._momentoCriacao = datetime.datetime.now()
        self._bitR = 1
        threading.Thread(target=self._contaTempoDeReferencia, args=[]).start()

    def _contaTempoDeReferencia( self ):
        time.sleep(10)
        self._bitR = 0
        #self._contaTempoDeReferencia()

    def exibeInformacoesPagina(self):
        print( "{}|{}".format( str(self._momentoCriacao).center(10), str(self._bitR).center(10) ) )

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

    '''
    def exibirProcessos(self, listaProcessos):
            
            grade = 90 * '_'
            print(grade)
            print("{}|{}|{}|{}".format("PID".center(10), "NAME".center(40), "USERNAME".center(20),
                                       "HORA_CRIACÃO".center(20)))
            print(grade)
            for processo in listaProcessos:
                print("{}|{}|{}|{}".format(str(processo.pid).ljust(10),
                                           str(processo.nome).ljust(40),
                                           str(processo.usuario).ljust(20),
                                           str(self.horaInicialProcesso(processo)).ljust(20)))

            print(grade)
'''
