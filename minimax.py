from jogo_da_velha import vazio, token, verificar_ganhador

def movimento_ia(tabuleiro, jogador):
    possibilidades = pega_posicoes(tabuleiro)
    melhor_valor = None
    melhor_movimento = None
    for p in possibilidades:
        tabuleiro[p[0]][p[1]] = token[jogador]
        valor = minimax(tabuleiro, jogador)
        tabuleiro[p[0]][p[1]] = vazio

        if melhor_valor is None:
            melhor_valor = valor
            melhor_movimento = p
        elif jogador == 0:
            if valor > melhor_valor:
                melhor_valor = valor
                melhor_movimento = p
        elif jogador == 1:
            if valor < melhor_valor:
                melhor_valor = valor
                melhor_movimento = p

    return melhor_movimento[0], melhor_movimento[1]

def pega_posicoes(tabuleiro):
    posicoes = []
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == vazio:
                posicoes.append([i, j])
    return posicoes


score = {
    "EMPATE": 0,
    "X": 1,
    "O": -1,
}

def minimax(tabuleiro, jogador):
    ganhador = verificar_ganhador(tabuleiro)
    if ganhador:
        return score[ganhador[0]]
    jogador = (jogador+1) % 2
    melhor_valor = None
    possibilidades = pega_posicoes(tabuleiro)
    for p in possibilidades:
        tabuleiro[p[0]][p[1]] = token[jogador]
        valor = minimax(tabuleiro, jogador)
        tabuleiro[p[0]][p[1]] = vazio

        if melhor_valor is None:
            melhor_valor = valor
        elif jogador == 0:
            if valor > melhor_valor:
                melhor_valor = valor
        elif jogador == 1:
            if valor < melhor_valor:
                melhor_valor = valor
    return melhor_valor