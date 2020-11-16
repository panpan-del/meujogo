from random import randint
import pygame, sys
from pygame.locals import*


   

      
#tamanho da tela
larx = 1440
alty = 900
desfundo = True
#parte grafica
 

pygame.init()
icon = pygame.image.load('faca.png')
pygame.display.set_icon(icon)
fundo = []
f = pygame.image.load('lado_r.png')
fundo.append(f)
f = pygame.image.load('delegacia.png')
fundo.append(f)


btnin = pygame.image.load('iniciar.png')
btnex = pygame.image.load('exit.png')
tela = pygame.display.set_mode((larx, alty), 0, 32)
pygame.display.set_caption('Lado R do Crime')
trilhas = []
t = pygame.mixer.Sound('musicamenu.mp3')
trilhas.append(t)
trilhas[0].play(-1)

click = False

mx, my = pygame.mouse.get_pos()

fim = False


tela.blit(fundo[0], (0, -10))
tela.blit(btnin, (480, 620))
tela.blit(btnex, (800, 620))
pygame.display.update()
        
while not fim:
 
  if tela.blit(btnin, (mx, my)):
       if click:
          tela.blit(fundo[1], (0, -10))
          
               
  for event in pygame.event.get():
    if event.type == QUIT:
      fim = True
    if event.type == KEYDOWN:
      if event.key == K_ESCAPE:
        pygame.quit()
        sys.exit()
    if event.type == MOUSEBUTTONDOWN:
      if pygame.mouse.get_pressed()[0]:
        mx, my = pygame.mouse.get_pos()
        click = True
        print(click)
        
           

    
        
pygame.display.quit()
print("Fim do programa")
