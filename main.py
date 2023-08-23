from jogo_da_velha import criar_tabuleiro, imprimir_tabuleiro, input_valido, verificar_movimento, fazer_movimento, verificar_ganhador
from minimax import movimento_ia, pega_posicoes, minimax


# variáveis de cor

vermelho = '\033[31m'
verde = '\033[32m'
azul = '\033[34m'
ciano = '\033[36m'
magenta = '\033[35m'
amarelo = '\033[33m'
preto = '\033[30m'
branco = '\033[37m'

limpacor = '\033[m'

negrito = '\033[1m'
sublinhado = '\033[4;36m'
reverso = '\033[7m'

fundopreto = '\033[40m'
fundovermelho = '\033[41m'
fundoverde = '\033[42m'
fundoamarelo = '\033[43m'
fundoazul = '\033[44m'
fundomagenta = '\033[45m'
fundociano = '\033[46m'
fundobranco = '\033[47m'

tabuleiro = criar_tabuleiro()
ganhador = verificar_ganhador(tabuleiro)
jogador = 0

while not ganhador:
    imprimir_tabuleiro(tabuleiro)
    if jogador == 1:
        linha, coluna = movimento_ia(tabuleiro, jogador)
    else:
        linha = input_valido("Digite a linha ")
        coluna = input_valido("Digite a coluna ")
    if verificar_movimento(tabuleiro, linha, coluna):
        fazer_movimento(tabuleiro, linha, coluna, jogador)
        jogador = (jogador+1) % 2
    else:
        print(f"A posição ({linha}, {coluna}) já está ocupada")
    
    ganhador = verificar_ganhador(tabuleiro)
    print("\n")

if ganhador[0] == "EMPATE":
    print("Jogo empatado")
elif ganhador[0] == "X":
    print("Jogador 1 jogando com X ganhou")
else:
    print("Jogador 2 jogando com O ganhou")
imprimir_tabuleiro(tabuleiro)