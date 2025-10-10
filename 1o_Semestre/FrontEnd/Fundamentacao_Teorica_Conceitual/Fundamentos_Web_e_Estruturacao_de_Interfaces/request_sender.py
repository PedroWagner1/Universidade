#   Este script Python destina-se a um programa que envia uma Request HTTP de acordo com os input's
#   do usuário e exibe uma resposta para tal.

import requests
import sys

#   Função que valida opções possíveis em campo de usuário:

def checar_opcoes(valor, *args):
    if valor not in args:
        print('\nvalor inválido. tente novamente em outra execução.')
        sys.exit()


def criar_headers(dicionario):
    x = True
    while x == True:

        p = input('Digite um parâmetro header')

        print(f'Parâmetro: {p}. Prosseguir? [y/n]\n\n_> ', end='')

        escolha = input().lower()
        checar_opcoes(escolha, 'y', 'n')

        a = input(f'Digite o argumento para o parâmetro {p}\n\n_> ')

        dicionario[p] = a   #   Adiciona Header ao dicionario

        print(f'Header Adicionado! \n{dicionario}\n\n. Continuar adicionando? [y/n]\n\n_> ', end='')
        escolha_b = input().lower()
        checar_opcoes(escolha_b, 'y', 'n')

        if escolha_b == 'n':
            x = False




while True:

    headers = {}
    print('Seja bem vindo !\n\nDigite a URL que deseja enviar a requisição: (formato: http(s)://seusitedeexemplo.com\n\n_> ', end='')

    url = input().lower()
    print()
    if not url.startswith('https://') and not url.startswith('http://'):
        print('\nUrl em formato inválido. Tente em outra execução')
        sys.exit()

    criar_headers(headers)

    try:
        print(f'\n\nResposta do Servidor {url}: \n\n', requests.get(url, headers=headers))
    except:
        print('Houve um Erro na resposta ou requisição. Tente mudar os Headers')
        sys.exit()

    escolha = input('\nDeseja tentar novamente? [y/n]').lower()
    checar_opcoes(escolha, 'y', 'n')

    if escolha == 'n':
        break