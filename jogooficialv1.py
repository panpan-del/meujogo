#!/usr/bin/python3.4
# Setup Python ----------------------------------------------- #
import pygame, sys
 
# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()

icon = pygame.image.load('faca.png')
pygame.display.set_icon(icon)
fundo = []
f = pygame.image.load('lado_r.png')
fundo.append(f)
f = pygame.image.load('delegacia.png')
fundo.append(f)

trilhas = []
t = pygame.mixer.Sound('musicamenu.mp3')
trilhas.append(t)
trilhas[0].play(-1)

pygame.display.set_caption('game base')
screen = pygame.display.set_mode((1440, 900),0,32)
desfundo = True
font = pygame.font.SysFont(None, 50)

btnin = pygame.image.load('iniciar.png')
btnex = pygame.image.load('exit.png')

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
 
click = False
 
def main_menu():
    while True:
 
        if desfundo:
          screen.blit(fundo[0], (0, -10))
        else:
          screen.fill((127, 127, 255))
        #draw_text('iniciar', font, (150, 152, 255), screen, 480, 550)
 
        mx, my = pygame.mouse.get_pos()
 
        button_1 = screen.blit(btnin, (480, 550))
        button_2 = screen.blit(btnex, (800, 550))
        if button_1.collidepoint((mx, my)):
            if click:
                personagem()
        if button_2.collidepoint((mx, my)):
            if click:
                pygame.quit()
                sys.exit()
        
        
 
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                    
 
        pygame.display.update()
        mainClock.tick(60)


def personagem():
    runnig = True
    while runnig:
        
        screen.fill((0, 0, 0))
        personagens = []
        p = pygame.image.load('personagem_marcelo.png')
        personagens.append(p)
        p = pygame.image.load('personagem_carol.png')
        personagens.append(p)
        
        
        mx, my = pygame.mouse.get_pos()
        
        p_1 = screen.blit(personagens[0], (100, 20))
        p_2 = screen.blit(personagens[1], (800, 20))
        if p_1.collidepoint((mx, my)):
            if click:
                main_menu()
        if p_2.collidepoint((mx, my)):
            if click:
                game()
        print(click)
        
        draw_text('Selecione seu Personagem', font, (255, 255, 255), screen, 550, 10)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                
        pygame.display.update()
        mainClock.tick(60)

def deck():
    runnig = True
    while runnig:
        screen.fill((250, 120, 300))
                       
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                
        pygame.display.update()
        mainClock.tick(60)
 
def game():
    running = True
    while running:
        screen.fill((0, 0, 0))
        
        
##      draw_text('game', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)
        
def options():
    for event in pygame.event.get():
       if event.type == QUIT:
          pygame.quit()
          sys.exit()
          running = False
       
    pygame.display.update()
    mainClock.tick(60)
 
main_menu()
