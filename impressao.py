#! /usr/bin/env python3
# -*- coding: utf-8 -*-

def menu():
    print("----- Manipulador de páginas -----")
    print("O que você deseja fazer?\n" +
          "Entre com um dos valores numéricos referêntes aos itens abaixo.")
    print("1 - Inserir nova página\n" +
          "2 - Mostrar tabela de páginas\n" +
          "3 - Encerrar programa\n")

    menuSelecionado = input("Digite um valor: ")

    print("Você selecionou a opção {}.".format(menuSelecionado) )

    return menuSelecionado


def imprimePIDProcesso(pid):
    print("PID do processo selecionado: " + pid + ".")


def imprimeProcessoFilhoMorto(pid):
    print("O processo filho com PID " + pid + " foi encerrado com sucesso.")


def imprimeProcessoPrincipalMorto(pid):
    print("O processo principal com PID " + pid + " foi encerrado com sucesso.")