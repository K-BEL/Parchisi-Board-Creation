
import sys

from pygame.locals import *
import pygame.freetype

pygame.font.init()
clock = pygame.time.Clock()

screen_width = 2000 
screen_height = 2000
screen = pygame.display.set_mode((screen_width, screen_height),HWSURFACE|DOUBLEBUF|RESIZABLE )
pygame.display.set_caption('Parchisi')
#pygame.transform.flip(screen,1500,1500)
#pygame.transform.scale(screen)



black = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
YELLOW = ((255, 255, 0))
GRAY = ((127, 127, 127))
GREEN1 = ((0, 50, 0))
YELLOW1 = ((255, 200, 0))
BLUE1 = ((0, 0, 100))
RED1 = (255, 0, 0, 255)

screen.fill(WHITE)
pygame.draw.rect(screen, (black), (50, 15, 801, 801), 3)

r1 = pygame.draw.rect(screen, (black), (50, 15, 267, 267), 2)
r2 = pygame.draw.rect(screen, (black), (317, 15, 267, 267), 2)
r3 = pygame.draw.rect(screen, (black), (584, 15, 267, 267), 2)

r4 = pygame.draw.rect(screen, (black), (50, 282, 267, 267), 3)
r5 = pygame.draw.rect(screen, (black), (317, 282, 267, 267), 3)
r6 = pygame.draw.rect(screen, (black), (584, 282, 267, 267), 3)

r7 = pygame.draw.rect(screen, (black), (50, 549, 267, 267), 3)
r8 = pygame.draw.rect(screen, (black), (317, 549, 267, 267), 3)
r9 = pygame.draw.rect(screen, (black), (584, 549, 267, 267), 3)

r10 = pygame.draw.rect(screen, (black), (355, 320, 191, 191), 1)

r11 = pygame.draw.polygon(screen,BLUE, ((355, 320), (356, 510),(450,416)))
r12 = pygame.draw.polygon(screen,YELLOW, ((355, 320), (355+191, 320),(450,416)))
r13 = pygame.draw.polygon(screen,GREEN, ((355+191, 320), (355+191, 320+191),(450,416)))
r14 = pygame.draw.polygon(screen,RED, ((355+191, 320+191), (356, 510),(450,416)))

pygame.draw.line(screen, black, [317, 282], [355, 320], 4 )
pygame.draw.line(screen, black, [355+191, 320], [584, 282], 4 )
pygame.draw.line(screen, black, [584, 549], [355+191, 320+191], 4 )
pygame.draw.line(screen, black, [317, 549], [356, 510], 4 )

pygame.draw.line(screen, black, [50, 549], [317, 549], 4 )
#pygame.draw.line(screen, black, [317, 549], [356, 510], 4 )
#pygame.draw.line(screen, black, [317, 549], [356, 510], 4 )
#pygame.draw.line(screen, black, [317, 549], [356, 510], 4 )
#



for i in range(0, 7):
    if i != 4:
        pygame.draw.rect(screen, (black), (317, 15 + 38.1 * i, 89, 38.1), 2)
        font = pygame.font.Font('freesansbold.ttf', 15)
        text = font.render(str(i + 1), True, black, WHITE)
        textRect = text.get_rect()
        textRect.center = (362, 35 + 38.1* i)
        screen.blit(text, textRect)
    else:
        ys = pygame.draw.rect(screen, (black), (317, 15 + 38.1 * i, 89, 38.1), 3)
        screen.fill(Color("YELLOW"), ys)

for i in range(0, 8):
    if i != 0:
        gs = pygame.draw.rect(screen, (black), (317 + 89, 15 + 38.1 * i, 89, 38.1), 2)
        screen.fill(Color("YELLOW"), gs)
    else:
        ys = pygame.draw.rect(screen, (black), (317 + 89, 15 + 38.1 * i, 89, 38.1), 3)
        screen.fill(Color("GRAY"), ys)
for i in range(0, 7):
    if i != 4:
        pygame.draw.rect(screen, (black), (317 + 89 * 2, 15 + 38.1 * i, 89, 38.1), 2)
        font = pygame.font.Font('freesansbold.ttf', 15)
        j=67
        text = font.render(str(j-i ), True, black, WHITE)
        textRect = text.get_rect()
        textRect.center = (317 + 89 * 2+45, 35 + 38.1* i)
        screen.blit(text, textRect)
    else:
        ys = pygame.draw.rect(screen, (black), (317 + 89 * 2, 15 + 38.1 * i, 89, 38.1), 3)
        screen.fill(Color("GRAY"), ys)

for i in range(0, 7):
    if i != 2:
        pygame.draw.rect(screen, (black), (317, 549 + 38.1 * i, 89, 38.1), 2)
        font = pygame.font.Font('freesansbold.ttf', 15)
        j = 27
        text = font.render(str(j + i), True, black, WHITE)
        textRect = text.get_rect()
        textRect.center = (317 + 45,549 + 38.1 * i+20 )
        screen.blit(text, textRect)
    else:
        ys = pygame.draw.rect(screen, (black), (317, 549 + 38.1 * i, 89, 38.1), 3)
        screen.fill(Color("GRAY"), ys)
for i in range(0, 8):
    if i != 7:
        gs = pygame.draw.rect(screen, (black), (317 + 89, 510.9 + 38.1 * i, 89, 38.1), 2)
        screen.fill(Color("RED"), gs)
    else:
        ys = pygame.draw.rect(screen, (black), (317 + 89, 510.9 + 38.1 * i, 89, 38.1), 2)
        screen.fill(Color("GRAY"), ys)
for i in range(0, 7):
    if i != 2:
        pygame.draw.rect(screen, (black), (317 + 89 * 2, 549 + 38.1 * i, 89, 38.1), 2)
        font = pygame.font.Font('freesansbold.ttf', 15)
        j=41
        text = font.render(str(j - i), True, black, WHITE)
        textRect = text.get_rect()
        textRect.center = (317 + 89 * 2+45, 549 + 38.1 * i+20)
        screen.blit(text, textRect)
    else:
        ys = pygame.draw.rect(screen, (black), (317 + 89 * 2, 549 + 38.1 * i, 89, 38.1), 2)
        screen.fill(Color("RED"), ys)

for i in range(0, 7):
    if i != 4:
        pygame.draw.rect(screen, (black), (50 + 38.1 * i, 282, 38.1, 89), 2)
        font = pygame.font.Font('freesansbold.ttf', 15)
        j=16
        text = font.render(str(j - i), True, black, WHITE)
        textRect = text.get_rect()
        textRect.center = (50 + 38.1 * i+20, 282+45)
        screen.blit(text, textRect)
    else:
        ys = pygame.draw.rect(screen, (black), (50 + 38.1 * i, 282, 38.1, 89), 3)
        screen.fill(Color("GRAY"), ys)
for i in range(0, 8):
    if i != 0:
        gs = pygame.draw.rect(screen, (black), (50 + 38.1 * i, 371, 38.1, 89), 2)
        screen.fill(Color("BLUE"), gs)
    else:
        ys = pygame.draw.rect(screen, (black), (50 + 38.1 * i, 371, 38.1, 89), 2)
        screen.fill(Color("GRAY"), ys)
for i in range(0, 7):
    if i != 4:
        pygame.draw.rect(screen, (black), (50 + 38.1 * i, 460, 38.1, 89), 2)
        j=18
        text = font.render(str(j + i), True, black, WHITE)
        textRect = text.get_rect()
        textRect.center = (50 + 38.1 * i+20, 460+45)
        screen.blit(text, textRect)
    else:
        ys = pygame.draw.rect(screen, (black), (50 + 38.1 * i, 460, 38.1, 89), 3)
        screen.fill(Color("BLUE"), ys)

for i in range(0, 7):
    if i != 2:
        pygame.draw.rect(screen, (black), (584 + 38.1 * i, 282, 38.1, 89), 2)
        font = pygame.font.Font('freesansbold.ttf', 15)
        j=58
        text = font.render(str(j - i), True, black, WHITE)
        textRect = text.get_rect()
        textRect.center = (584 + 38.1 * i+20, 282+45)
        screen.blit(text, textRect)
    else:
        ys = pygame.draw.rect(screen, (black), (584 + 38.1 * i, 282, 38.1, 89), 2)
        screen.fill(Color("GREEN"), ys)
for i in range(0, 8):
    if i != 7:
        gs = pygame.draw.rect(screen, (black), (545 + 38.1 * i, 371, 38.1, 89), 2)
        screen.fill(Color("GREEN"), gs)
    else:
        ys = pygame.draw.rect(screen, (black), (545 + 38.1 * i, 371, 38.1, 89), 2)
        screen.fill(Color("GRAY"), ys)
for i in range(0, 7):
    if i != 2:
        pygame.draw.rect(screen, (black), (584 + 38.1 * i, 460, 38.1, 89), 2)
        font = pygame.font.Font('freesansbold.ttf', 15)
        j=44
        text = font.render(str(j + i), True, black, WHITE)
        textRect = text.get_rect()
        textRect.center = (584 + 38.1 * i+20, 460+45)
        screen.blit(text, textRect)
    else:
        ys = pygame.draw.rect(screen, (black), (584 + 38.1 * i, 460, 38.1, 89), 2)
        screen.fill(Color("GRAY"), ys)


font = pygame.font.Font('freesansbold.ttf', 15)
text = font.render(str(8), True, black, WHITE)
textRect = text.get_rect()
textRect.center = (362, 35 + 38.1* 7)
screen.blit(text, textRect)

font = pygame.font.Font('freesansbold.ttf', 15)
text = font.render(str(60), True, black, WHITE)
textRect = text.get_rect()
textRect.center = (317 + 89 * 2+45, 35 + 38.1* 7)
screen.blit(text, textRect)

font = pygame.font.Font('freesansbold.ttf', 15)
text = font.render(str(26), True, black, WHITE)
textRect = text.get_rect()
textRect.center = (317 + 45,549 + 38.1 * (-1)+20)
screen.blit(text, textRect)

font = pygame.font.Font('freesansbold.ttf', 15)
text = font.render(str(42), True, black, WHITE)
textRect = text.get_rect()
textRect.center = (317 + 89 * 2+45, 549 + 38.1 * (-1)+20)
screen.blit(text, textRect)

font = pygame.font.Font('freesansbold.ttf', 15)
text = font.render(str(9), True, black, WHITE)
textRect = text.get_rect()
textRect.center = (50 + 38.1 * 7+20, 282+45)
screen.blit(text, textRect)

font = pygame.font.Font('freesansbold.ttf', 15)
text = font.render(str(25), True, black, WHITE)
textRect = text.get_rect()
textRect.center = (50 + 38.1 * 7+20, 460+45)
screen.blit(text, textRect)

font = pygame.font.Font('freesansbold.ttf', 15)
text = font.render(str(59), True, black, WHITE)
textRect = text.get_rect()
textRect.center = (584 + 38.1 * (-1)+20, 282+45)
screen.blit(text, textRect)

font = pygame.font.Font('freesansbold.ttf', 15)
text = font.render(str(43), True, black, WHITE)
textRect = text.get_rect()
textRect.center = (584 + 38.1 * (-1)+20, 460+45)
screen.blit(text, textRect)
       


    
    
    
    
screen.fill(Color("YELLOW1"), r1)
screen.fill(Color("GREEN1"), r3)
screen.fill(Color("BLUE1"), r7)
screen.fill(Color("RED1"), r9)




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == VIDEORESIZE:
                screen = pygame.display.set_mode(event.dict['size'], HWSURFACE|DOUBLEBUF|RESIZABLE)           

    pygame.display.flip()
    clock.tick(60)
