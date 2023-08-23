vazio = " "
token = ["X", "O"]
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

def criar_tabuleiro():
    tabuleiro = [
        [vazio, vazio, vazio],
        [vazio, vazio, vazio],
        [vazio, vazio, vazio],
    ]
    return tabuleiro

def imprimir_tabuleiro(tabuleiro):
    ganhador = verificar_ganhador(tabuleiro)
    if not ganhador or ganhador == ["EMPATE"]:
        for i in range(0, len(tabuleiro)):
            print("|".join(tabuleiro[i]))
            if i != len(tabuleiro)-1:
                print("------")
    else:
        if ganhador[2] == "Linha":
            for i in range(0, len(tabuleiro)):
                if ganhador[1] == i:
                    print(f"{verde}", f"|".join(tabuleiro[i]), sep="")
                else:
                    print(f"{limpacor}|".join(tabuleiro[i]))
                if i != len(tabuleiro)-1:
                    print(f"{limpacor}------")
        
        if ganhador[2] == "Coluna":
            j = 0
            for i in range(0, len(tabuleiro)):
                print(f"{verde if j == ganhador[1] else limpacor}", f"{tabuleiro[i][0]}|", end="", sep="")
                j += 1
                print(f"{verde if j == ganhador[1] else limpacor}", f"{tabuleiro[i][1]}|", end="", sep="")
                j += 1
                print(f"{verde if j == ganhador[1] else limpacor}", f"{tabuleiro[i][2]}", sep="")
                j = 0
                if i != len(tabuleiro)-1:
                    print(f"{limpacor}------")
        
        if ganhador[2] == "Diagonal" and ganhador[1] == 1:
            j = 0
            for i in range(0, 3):
                print(f"{verde if j == i else limpacor}", f"{tabuleiro[i][0]}|", end="", sep="")
                j += 1
                print(f"{verde if j == i else limpacor}", f"{tabuleiro[i][1]}|", end="", sep="")
                j += 1
                print(f"{verde if j == i else limpacor}", f"{tabuleiro[i][2]}", sep="")
                j = 0
                if i != len(tabuleiro)-1:
                    print(f"{limpacor}------")

        if ganhador[2] == "Diagonal" and ganhador[1] == 2:
            j = 0
            for i in range(0, 3):
                print(f"{verde if j + i == ganhador[1] else limpacor}", f"{tabuleiro[i][0]}|", end="", sep="")
                j += 1
                print(f"{verde if j + i == ganhador[1] else limpacor}", f"{tabuleiro[i][1]}|", end="", sep="")
                j += 1
                print(f"{verde if j + i == ganhador[1] else limpacor}", f"{tabuleiro[i][2]}", sep="")
                j = 0
                if i != len(tabuleiro)-1:
                    print(f"{limpacor}------")
                

def input_valido(mensagem):
    try:
        n = int(input(mensagem))
        if n >= 1 and n <= 3:
            return n-1
        else:
            print("Número precisa estar entre 1 e 3")
            return input_valido(mensagem)
    except:
        print("Número inválido")
        return input_valido(mensagem)

def verificar_movimento(tabuleiro, linha, coluna):
    return tabuleiro[linha][coluna] == vazio

def fazer_movimento(tabuleiro, linha, coluna, jogador):
    if jogador == 0:
        tabuleiro[linha][coluna] = token[0]
    else:
        tabuleiro[linha][coluna] = token[1]

def verificar_ganhador(tabuleiro):
    for i in range(0, 3):
        if tabuleiro[i][0] != vazio and tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2]:
            return [tabuleiro[i][0], i, "Linha"]
    
    for i in range(0, 3):
        if tabuleiro[0][i] != vazio and tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i]:
            return [tabuleiro[0][i], i, "Coluna"]
        
    if tabuleiro[1][1] != vazio and tabuleiro[1][1] == tabuleiro[0][0] == tabuleiro[2][2]:
        return [tabuleiro[1][1], 1, "Diagonal"]
    
    if tabuleiro[1][1] != vazio and tabuleiro[1][1] == tabuleiro[2][0] == tabuleiro[0][2]:
        return [tabuleiro[1][1], 2, "Diagonal"]
    
    for i in range(0, 3):
        for j in range(0, 3):
            if tabuleiro[i][j] == vazio:
                return False
    return ["EMPATE"]