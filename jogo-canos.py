import pygame
import random

# Inicialização do pygame
pygame.init()

# Definindo cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0) 
BLUE = (0, 0, 255)

# Dimensões da janela
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Parâmetros do pássaro
BIRD_WIDTH = 40
BIRD_HEIGHT = 30
bird_x = 50
bird_y = SCREEN_HEIGHT // 2
bird_speed = 5
gravity = 0.5
jump_height = -7


# Parâmetros dos canos
PIPE_WIDTH = 70
PIPE_HEIGHT = 400
pipe_gap = 150
pipe_x = SCREEN_WIDTH
pipe_y = random.randint(100, SCREEN_HEIGHT - 100 - pipe_gap)
pipe_speed = 5

# Pontuação
score = 0
font = pygame.font.SysFont(None, 40)

# Função para mostrar a pontuação
def show_score():
    score_text = font.render(f"Pontuação: {score}", True, BLACK)
    screen.blit(score_text, [10, 10])

# Função principal do jogo
def game_loop():
    global bird_y, bird_speed, pipe_x, pipe_y, score
    clock = pygame.time.Clock()
    running = True

    while running:
        screen.fill(WHITE)

        # Eventos do jogo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird_speed = jump_height

        # Movimento do pássaro
        bird_speed += gravity
        bird_y += bird_speed

        # Movimento dos canos
        pipe_x -= pipe_speed
        if pipe_x < -PIPE_WIDTH:
            pipe_x = SCREEN_WIDTH
            pipe_y = random.randint(100, SCREEN_HEIGHT - 100 - pipe_gap)
            score += 1

        # Desenhando o pássaro
        pygame.draw.rect(screen, BLUE, [bird_x, bird_y, BIRD_WIDTH, BIRD_HEIGHT])


        # Desenhando os canos
        pygame.draw.rect(screen, BLACK, [pipe_x, 0, PIPE_WIDTH, pipe_y])
        pygame.draw.rect(screen, BLACK, [pipe_x, pipe_y + pipe_gap, PIPE_WIDTH, SCREEN_HEIGHT - pipe_y - pipe_gap])
 
        # Verificando colisão com o chão e o teto
        if bird_y > SCREEN_HEIGHT or bird_y < 0:
            running = False

        # Verificando colisão com os canos
        if (bird_x + BIRD_WIDTH > pipe_x and bird_x < pipe_x + PIPE_WIDTH):
            if (bird_y < pipe_y or bird_y + BIRD_HEIGHT > pipe_y + pipe_gap):
                running = False

        # Exibindo a pontuação
        show_score()

        # Atualizando a tela 
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    print(f"Game Over! Pontuação final: {score}")

# Iniciando o jogo  
game_loop()
