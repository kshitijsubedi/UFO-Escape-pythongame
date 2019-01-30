import pygame
import random

pygame.init()
screen=pygame.display.set_mode((800,700))
pygame.display.set_caption(" UFO Escape Game By Kshitij Subedi")
clock=pygame.time.Clock()

#################
bg=(230,251,255)
pipey=(0,230,77)
birdy=(255,128,0)
white=(255,255,255)
black=(0,0,0)
font = arial18 = pygame.font.SysFont('arial',18, False, False)
pipes=[]
#score=0

#################################
class Bird():
    def __init__(self):
        self.x = 250
        self.y = 250
        self.yV = 0
    
    def flap(self):
        self.yV = -11
    
    def update(self):
        self.yV += 0.7
        self.y += self.yV
        if self.y >= 650:
            self.y = 650
            self.yV = 0
        if self.yV > 10:
            self.yV = 10

    def draw(self):
        #pygame.draw.rect(screen,birdy,(self.x,self.y,35,35))
        img = pygame.image.load("ufo.png")
        screen.blit(img,(self.x,self.y))

    def reset(self):
        self.x = 200
        self.y = 250
        self.yV = 0

bird = Bird()

class Pipe():
    def __init__(self):
        self.centerY = random.randrange(120,600)
        self.x = 800
        self.size = 100
    
    def update(self):
        global pipes
        global bird
        global game
        global score
        self.x -= 5

        if self.x == 320:
            pipes.append(Pipe())
        if self.x <=0:
            del pipes[0]
        if self.x >= 200 and self.x <= 300 and (bird.y) <= (self.centerY - self.size) or self.x >= 150 and self.x <= 300 and (bird.y+40) >= (self.centerY + self.size):
            game = 3
        if self.x==170 and bird.y > (self.centerY - 100) and bird.y < (self.centerY + 100):
            score+= 1
        if bird.y >= 650:
            game = 3

    def draw(self):
        pygame.draw.rect(screen,pipey,(self.x,0,80,(self.centerY - self.size)))
        pygame.draw.rect(screen,pipey,(self.x,(self.centerY + self.size),80,(600 - self.centerY)))

pipes.append(Pipe())
##############

hs=0
play=True
game=1
score=0
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type ==pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if game==1:
                    game=2
                if game==3:
                    bird.reset()
                    pipes=[]
                    pipes.append(Pipe())
                    game==2
                else:  
                    bird.flap()
    screen.fill(bg)
    if game==1:
        # intro aba
        pygame.draw.rect(screen,(189,183,107),(250,250,300,150))
        text= font.render(" Welcome to UFO Escape !!! ",True,black)
        screen.blit(text,(300,300))
        text4= font.render(" Use SPACE to play .  ",True,black)
        screen.blit(text4,(300,320))
        

    if game==2:
        bird.update()
        bird.draw()
        for pipe in pipes:
            pipe.update()
            pipe.draw()
        if score>hs:
            hs=score
        text=font.render(str(score),True,black)
        screen.blit(text,(400,50))
    if game==3:
        ### game over case 
        pygame.draw.rect(screen,(255,182,193),(300,300,300,150))
        text1=font.render("Your score was :",True,black)
        text2=font.render(str(score),True,black)
        screen.blit(text1,(400,350))
        screen.blit(text2,(420,380))
        text3=font.render("Press Right-ALT To restart ",True,black)
        screen.blit(text3,(400,400))
        if event.type ==pygame.KEYDOWN:
            if event.key == pygame.K_RALT:
                bird.reset()
                score = 0
                game=1
    pygame.display.flip()
    clock.tick(60)
pygame.quit()

