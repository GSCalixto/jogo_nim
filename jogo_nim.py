usuario = 0
computador = 0

def computador_escolhe_jogada(n, m):
    computadorRemove = 1
    
    if n == m:
        computadorRemove = m

        return computadorRemove
    else:
        while computadorRemove != m:
            if (n - computadorRemove) % (m+1) == 0:
                return computadorRemove
            else:
                computadorRemove += 1

    return computadorRemove


def usuario_escolhe_jogada(n, m):
    jogada = int(input('Quantas peças você vai tirar? '))

    if jogada <= m and jogada <= n and jogada != 0:
        n = n - jogada
        return jogada
    else:
        print('Oops! Jogada inválida! Tente de novo.')
        usuario_escolhe_jogada(n, m)

def verifica_ganhador(n, pcJogou):
    global computador

    if n == 0 and pcJogou == True:
        computador =+ 1
        print("Fim do jogo! O computador ganhou!")
    elif n== 0 and pcJogou == False:
        print("Fim de jogo! O usuário ganhou!")  

def campeonato():
    numeroRodada = 1
    while numeroRodada <= 3:
        print('\n**** Rodada', numeroRodada, '****\n')

        partida()
        numeroRodada += 1

    print('\nPlacar: Você 0 X 3 Computador')

def partida():
    n = int(input('\nQuantas peças?'))
    m = int(input('Limite de peças por jogada?'))

    vezDoPc = False

    if n % (m+1) == 0:
        print('\nVocê começa!')
    else:
        print('\nComputador começa!')
        vezDoPc = True
    
    while n > 0:
        if vezDoPc:
            computadorRemove = computador_escolhe_jogada(n, m)
            n = n - computadorRemove

            print('\nO computador tirou', computadorRemove, 'peças')
            verifica_ganhador(n, vezDoPc)

            vezDoPc = False
        else:
            jogadorRemove = usuario_escolhe_jogada(n, m)
            n = n - jogadorRemove

            print('\nVocê tirou', jogadorRemove, 'peças')
            verifica_ganhador(n, vezDoPc)
                    
            vezDoPc = True
            
                
        if n == 1:
            print('Agora resta apenas uma peça no tabuleiro.\n')
        else:
            if n > 0:
                print('Agora restam,', n, 'peças no tabuleiro.\n')


print('Bem-vindo ao jogo do NIM! Escolha: \n')

tipoDePartida = int(input('1 - para jogar uma partida\n2 - para jogar um campeonato \n'))

if tipoDePartida == 2:
    print('Voce escolheu um campeonato!\n')
    campeonato()
elif tipoDePartida == 1:
    partida()
else:
    print('Opção inválida, escolha apenas entre "1" e "2"')
