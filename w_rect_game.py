'''
    Desenvolvido por Walisson Silva
    João Pessoa, 10/06/2018

    Visite o meu site: https://www.walissonsilva.com

    Boa diversão! =)
'''

import pygame
import random

def main():
    # Inicialização
    side_window = 250
    close = False
    game_over = False
    score = 0 # pontuação do jogador
    score_increment = True

    # Configurações da janela
    pygame.init()
    janela = pygame.display.set_mode([side_window, side_window])
    pygame.display.set_caption('W-Rect Game')
    clock = pygame.time.Clock()
    
    # Definição de Cores
    bg_color = (255, 255, 255)
    cor_roxo = (122, 16, 126)

    janela.fill(bg_color) # cor de preenchimento de tela

    # Definição de fontes
    pygame.font.init()
    font = pygame.font.get_default_font()
    font_game_over = pygame.font.SysFont('monospace', 30, bold=True)
    font_pontuacao = pygame.font.SysFont(font, 16)

    # Configurações do Salto
    rotina_pular = [-13, -13, -13, -13, -6, -6, -6, -3, -3, -3, 3, 3, 3, 6, 6, 6, 13, 13, 13, 13]
    pos_salto = 0
    salto = False

    # Configurações do Player
    pos_x, pos_y = 40, side_window - 15
    player = pygame.Rect((pos_x, pos_y), (20, 15))
    pygame.draw.rect(janela, (255, 0, 0), player)

    # Configurações do obstáculo
    tam_obs = random.randint(10, 35)
    posx_obs, posy_obs = side_window, side_window - tam_obs
    obs = pygame.Rect((posx_obs, posy_obs), (15, tam_obs))

    while (not close) and (not game_over):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                close = True
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_SPACE):
                    salto = True

        # Rotina para o salto do jogador
        if (salto):
            player.move_ip(0, rotina_pular[pos_salto])
            pos_salto += 1
            if (pos_salto >= len(rotina_pular)):
                pos_salto = 0
                salto = False
        
        # Rotina para o movimento dos obstáculos
        obs.move_ip(-3, 0)
        # Rotina para recriar a partícula
        if (obs.left < -30):
            tam_obs = random.randint(10, 35)
            posx_obs, posy_obs = side_window, side_window - tam_obs
            obs = pygame.Rect((posx_obs, posy_obs), (15, tam_obs))
            score_increment = True

        # Adicionando pontuação ao jogador
        if (obs.left < 30 and score_increment):
            score += 1
            score_increment = False


        # ------------- IMPRIMIR NA TELA ------------------ #
        janela.fill(bg_color) # preenchimento de tela
        pygame.draw.rect(janela, (255, 0, 0), player)
        pygame.draw.rect(janela, (0, 0, 255), obs)
        
        # Teste de colisão
        if (player.colliderect(obs)):
            game_over = True
            text_game_over = font_game_over.render("GAME OVER", True, cor_roxo)
            janela.blit(text_game_over, (int(side_window / 2 - 75), int(side_window / 2 - 22)))

        # Imprimindo pontuação
        text_pontuacao = font_pontuacao.render("SCORE: " + str(score), True, (0, 0, 0))
        janela.blit(text_pontuacao, (side_window - 65, 10))


        clock.tick(30) # Número de frames por segundo
        pygame.display.update() # Atualização das informações da tela
    
    if (close):
        pygame.quit()
    if (game_over):
        pygame.time.delay(3000)
        main()

main()