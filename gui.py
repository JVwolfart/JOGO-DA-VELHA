import pygame
from jogo_da_velha import criar_tabuleiro, imprimir_tabuleiro, input_valido, fazer_movimento, verificar_movimento, verificar_ganhador
from minimax import movimento_ia

pygame.font.init()

def desenhar_tabuleiro(tela, tabuleiro):
    largura = 600
    altura = 600
    tamanho = 600/3
    for i in range(1, 3):
        pygame.draw.line(tela, (0, 0, 0), (0, i*tamanho), (largura, i*tamanho), 3)
        pygame.draw.line(tela, (0, 0, 0), (i*tamanho, 0), (i*tamanho, altura ), 3)

    for i in range(3):
        for j in range(3):
            font = pygame.font.SysFont("comicsans", 100)
            x = j*tamanho
            y = i*tamanho
            if tabuleiro[i][j] == "X":
                text = font.render(tabuleiro[i][j], 1, (0, 200, 50))
                tela.blit(text, ((x+75), (y+75)))
            else:
                text = font.render(tabuleiro[i][j], 1, (255, 0, 0))
                tela.blit(text, ((x+75), (y+75)))
            
                

def redesenhar_janela(tela, tabuleiro):
    tela.fill((255, 255, 255))
    desenhar_tabuleiro(tela, tabuleiro)

def main():
    tela = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Jogo da Velha")
    tabuleiro = criar_tabuleiro()
    ganhador = verificar_ganhador(tabuleiro)
    jogador = 0
    redesenhar_janela(tela, tabuleiro)
    pygame.display.update()
    

    while not ganhador:
        imprimir_tabuleiro(tabuleiro)
        if jogador == 3:
            linha, coluna = movimento_ia(tabuleiro, jogador)
        else:
            jogou = False
            while not jogou:
                for e in pygame.event.get():
                    if e.type == pygame.QUIT:
                        return
                    elif e.type == pygame.MOUSEBUTTONUP:
                        pos = pygame.mouse.get_pos()
                        linha = pos[1]//200
                        coluna = pos[0]//200
                        print(linha, coluna)
                        jogou = True
        if verificar_movimento(tabuleiro, linha, coluna):
            fazer_movimento(tabuleiro, linha, coluna, jogador)
            jogador = (jogador+1) % 2
        else:
            print(f"A posição ({linha}, {coluna}) já está ocupada")
        
        ganhador = verificar_ganhador(tabuleiro)
        redesenhar_janela(tela, tabuleiro)
        pygame.display.update()
    msg = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Fim de jogo")
    msg.fill((255, 255, 255))
    if ganhador[0] == "X":
        font = pygame.font.SysFont("comicsans", 50)
        text = font.render("Parabéns, você ganhou! :)", 1, (0, 200, 50))
        msg.blit(text, (100, 300))
    elif ganhador[0] == "O":
        font = pygame.font.SysFont("comicsans", 50)
        text = font.render("A inteligência artificial ganhou :(", 1, (255, 0, 0))
        msg.blit(text, (15, 300))
    else:
        font = pygame.font.SysFont("comicsans", 80)
        text = font.render("Jogo empatado.", 1, (255, 230, 0))
        msg.blit(text, (100, 300))
    pygame.display.update()
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return
main()