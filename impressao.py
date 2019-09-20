#! /usr/bin/env python3
# -*- coding: utf-8 -*-

class Impressao:

    @staticmethod
    def menu():
        print("----- Simulador de páginas -----")
        print("O que você deseja fazer?\n" +
              "Entre com um dos valores numéricos referêntes aos itens abaixo.")
        print("1 - Inserir nova página\n" +
              "2 - Mostrar tabela de páginas\n" +
              "3 - Encerrar programa\n")

        menuSelecionado = int( input("Digite um valor: ") )

        print("Você selecionou a opção {}.".format(menuSelecionado) )

        return menuSelecionado