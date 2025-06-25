import random

# Escolha de modalidade
print('1 - humano x humano\n2 - humano x computador\n3 - computador x computador')
modalidade = int(input('Insira a modalidade desejada: '))

jogar = 1
placar1 = 0
placar2 = 0

while jogar == 1:
    # Humano x humano
    if modalidade == 1:
        jogador1 = int(input('Jogador 1, escolha entre: 1 - pedra, 2 - papel ou 3 - tesoura: '))
        jogador2 = int(input('Jogador 2, escolha entre: 1 - pedra, 2 - papel ou 3 - tesoura: '))

        if jogador1 == jogador2:
            print('Empate')
        elif (jogador1 == 1 and jogador2 == 2) or (jogador1 == 2 and jogador2 == 1):
            vencedor = 1 if jogador1 == 2 else 2
            print('Papel vence, jogador', vencedor, 'vencedor')
            if vencedor == 1:
                placar1 += 1
            else:
                placar2 += 1
        elif (jogador1 == 1 and jogador2 == 3) or (jogador1 == 3 and jogador2 == 1):
            vencedor = 1 if jogador1 == 1 else 2
            print('Pedra vence, jogador', vencedor, 'vencedor')
            if vencedor == 1:
                placar1 += 1
            else:
                placar2 += 1
        elif (jogador1 == 2 and jogador2 == 3) or (jogador1 == 3 and jogador2 == 2):
            vencedor = 1 if jogador1 == 3 else 2
            print('Tesoura vence, jogador', vencedor, 'vencedor')
            if vencedor == 1:
                placar1 += 1
            else:
                placar2 += 1

        print('Placar: ', placar1, 'x', placar2)

    # Humano x computador
    elif modalidade == 2:
        jogador = int(input('Escolha entre: 1 - pedra, 2 - papel ou 3 - tesoura: '))
        computador = random.randint(1, 3)

        jogadas = {1: 'Pedra', 2: 'Papel', 3: 'Tesoura'}
        print(f'Jogador = {jogadas[jogador]}.\nComputador = {jogadas[computador]}.')

        if jogador == computador:
            print('Empate')
        elif (jogador == 1 and computador == 2) or (jogador == 2 and computador == 1):
            if jogador == 2:
                print('Papel vence. Jogador vencedor')
                placar1 += 1
            else:
                print('Papel vence. Computador vencedor')
                placar2 += 1
        elif (jogador == 1 and computador == 3) or (jogador == 3 and computador == 1):
            if jogador == 1:
                print('Pedra vence. Jogador vencedor')
                placar1 += 1
            else:
                print('Pedra vence. Computador vencedor')
                placar2 += 1
        elif (jogador == 2 and computador == 3) or (jogador == 3 and computador == 2):
            if jogador == 3:
                print('Tesoura vence. Jogador vencedor')
                placar1 += 1
            else:
                print('Tesoura vence. Computador vencedor')
                placar2 += 1

        print('Placar: ', placar1, 'x', placar2)

    # Computador x computador
    elif modalidade == 3:
        computador1 = random.randint(1, 3)
        computador2 = random.randint(1, 3)

        jogadas = {1: 'Pedra', 2: 'Papel', 3: 'Tesoura'}
        print(f'Computador 1 = {jogadas[computador1]}.\nComputador 2 = {jogadas[computador2]}.')

        if computador1 == computador2:
            print('Empate')
        elif (computador1 == 1 and computador2 == 2) or (computador1 == 2 and computador2 == 1):
            if computador1 == 2:
                print('Papel vence. Computador 1 vencedor')
                placar1 += 1
            else:
                print('Papel vence. Computador 2 vencedor')
                placar2 += 1
        elif (computador1 == 1 and computador2 == 3) or (computador1 == 3 and computador2 == 1):
            if computador1 == 1:
                print('Pedra vence. Computador 1 vencedor')
                placar1 += 1
            else:
                print('Pedra vence. Computador 2 vencedor')
                placar2 += 1
        elif (computador1 == 2 and computador2 == 3) or (computador1 == 3 and computador2 == 2):
            if computador1 == 3:
                print('Tesoura vence. Computador 1 vencedor')
                placar1 += 1
            else:
                print('Tesoura vence. Computador 2 vencedor')
                placar2 += 1

        print('Placar: ', placar1, 'x', placar2)

    # Continuar ou encerrar
    jogar = int(input('Insira 1 se deseja jogar mais uma partida ou 0 caso queira encerrar: '))
    while jogar != 0 and jogar != 1:
        print('Inserção inválida.')
        jogar = int(input('Insira 1 se deseja jogar mais uma partida ou 0 caso queira encerrar: '))

# Resultado final
print('Jogador 1:', placar1, 'X Jogador 2:', placar2)
if placar1 > placar2:
    print('O vencedor geral foi o Jogador 1')
elif placar2 > placar1:
    print('O vencedor geral foi o Jogador 2')
else:
    print('O placar final ficou empatado.')

print('\nObrigado por jogar o nosso joquempô. Feito por: Amanda O. B. Santos e Felyppe P. Silva')
