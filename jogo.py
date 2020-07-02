import pygame
import time
import random
pygame.init()

# Variáveis Gerais #############
def user():  
    nome = input("Nome: ")
    email = input("E-mail: ")
    arquivo = open("login.txt","r")
    login = arquivo.readlines()
    login.append(nome)
    login.append("\n")
    login.append(email)
    login.append("\n")
    arquivo = open("login.txt","w")
    arquivo.writelines(login)

    arquivo = open("login.txt","r")
    texto = arquivo.readlines()
    for line in texto:
        print(line)
    arquivo.close() 

user()

larguraTela = 700
alturaTela = 500
gamedisplay = pygame.display.set_mode((larguraTela, alturaTela))
clock = pygame.time.Clock()
# RGB (Red, Green, Blue) (0,255)
fontes = pygame.font.get_fonts()
#print(fontes)
black = (0, 0, 0)
white = (255, 255, 255)
gray = (100, 100, 100)
naveImg = pygame.image.load('material/nave.png').convert_alpha()
asteroidImg = pygame.image.load('material/asteroid.png').convert_alpha()
fundo = pygame.image.load("material/fundo.jpg")
iconeJogo = pygame.image.load("material/icon.jpg")
pygame.display.set_icon(iconeJogo)
pygame.display.set_caption('Star Piana')
# Funções Gerais #############
def mostraNave(x, y):
    gamedisplay.blit(naveImg, (x, y))
def mostraAsteroid(x, y):
    gamedisplay.blit(asteroidImg, (x, y))
def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 70)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((larguraTela/2, alturaTela/2))
    gamedisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(5)
    game_loop()
def mortenave():
    message_display("Você foi destruido!")
def escrevePlacar(contador):
    font = pygame.font.SysFont("perpetua", 40)
    text = font.render("Desvios: "+str(contador), True, white)
    gamedisplay.blit(text, (10, 30))
def game_loop():
    # Looping do Jogo
    #pygame.mixer.music.load("materiais/navesound.mp3")
    # parametro -1, é looping infinito
    #pygame.mixer.music.play(-1)
    #pygame.mixer.music.set_volume(0.1)
    navePosicaoX = 200
    navePosicaoY = 400
    movimentoX = 0
    largura_nave = 111
    altura_nave = 70
    # random é um sorteio de 0 até 800
    asteroidPosicaoX = random.randrange(0, larguraTela)
    asteroidPosicaoY = -600
    largura_asteroid = 108
    altura_asteroid = 99
    asteroid_speed = 7
    contador = 0
    nave_speed = 10
    while True:
        # inicio -  event.get() devolve uma lista de eventos que estão acontecendo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                # quit() é comando native terminar o programa
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    movimentoX = nave_speed * -1 
                elif event.key == pygame.K_RIGHT:
                    movimentoX = nave_speed
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    movimentoX = 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("Posição do Mouse")
                print(event.pos)
        # fim -  event.get() devolve uma lista de eventos que estão acontecendo



        navePosicaoX = navePosicaoX + movimentoX
        gamedisplay.fill(white)
        gamedisplay.blit(fundo, (0, 0))
        mostraNave(navePosicaoX, navePosicaoY)
        escrevePlacar(contador)
        if navePosicaoX > larguraTela - largura_nave :
            navePosicaoX = larguraTela-largura_nave
        elif navePosicaoX < 0:
            navePosicaoX = 0
        mostraAsteroid(asteroidPosicaoX, asteroidPosicaoY)
        asteroidPosicaoY = asteroidPosicaoY + asteroid_speed
        if asteroidPosicaoY > alturaTela:
            asteroidPosicaoY = 0 - altura_asteroid
            asteroidPosicaoX = random.randrange(0, larguraTela)
            asteroid_speed = asteroid_speed + 1
            contador = contador + 1
        if navePosicaoY + 50 < asteroidPosicaoY + altura_asteroid:
            if navePosicaoX < asteroidPosicaoX and navePosicaoX + largura_nave > asteroidPosicaoX or asteroidPosicaoX+largura_asteroid > navePosicaoX and asteroidPosicaoX+largura_asteroid < navePosicaoX + largura_nave:
                mortenave()
        pygame.display.update()
        clock.tick(60)
game_loop()