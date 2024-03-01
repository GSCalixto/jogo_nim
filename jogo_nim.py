def computador_escolhe_jogada(n, m):
    computadorRemove = 1

    while computadorRemove != m:
        if (n - computadorRemove) % (m+1) == 0:
            return computadorRemove
        else:
            computadorRemove += 1

    return computadorRemove

def usuario_escolhe_jogada(n, m):
    jogada = int(input('Quantas peças você vai tirar? '))

    if jogada >= m and jogada <= n:
        n = n - jogada
        return jogada
    else:
        print('Oops! Jogada inválida! Tente de novo.')
        usuario_escolhe_jogada(n, m)       

def campeonato():
    numeroRodada = 1
    while numeroRodada <= 3:
        print('\n**** Rodada', numeroRodada, '****\n')

        partida()
        numeroRodada += 1

    print('\nPlacar: Você 0 X 3 Computador')

def partida():
    n = int(input('\nPor favor defina quantas peças terão na mesa '))
    m = int(input('Defina o mínimo de peças retiradas a cada jogada '))

    vezDoPc = False

    if n % (m+1):
        print('\nUsuário começa!')
    else:
        print('\nComputador começa!')
        vezDoPc = True
    
    while n > 0:
        if vezDoPc:
            computadorRemove = computador_escolhe_jogada(n, m)
            n = n - computadorRemove

            print('\nO computador tirou', computadorRemove, 'peças')

            vezDoPc = False
        else:
            jogadorRemove = usuario_escolhe_jogada(n, m)
            n = n - jogadorRemove

            print('\nVocê tirou', jogadorRemove, 'peças')
                    
            vezDoPc = True
            
                
        if n == 1:
            print('Agora resta apenas uma peça no tabuleiro.\n')
        else:
            if n > 0:
                print('Agora restam,', n, 'peças no tabuleiro.\n')

        if n <= m:
            print("O jogo terminou!")
            break

def main():
    print('Bem-vindo ao jogo do NIM! Escolha: \n')

    tipoDePartida = int(input('1 - para jogar uma partida\n2 - para jogar um campeonato \n'))

    if tipoDePartida == 2:
        print('Voce escolheu um campeonato!\n')
        campeonato()
    elif tipoDePartida == 1:
        partida()
    else:
        print('Opção inválida, escolha apenas entre "1" e "2"')

if __name__ == "__main__":
    main()
