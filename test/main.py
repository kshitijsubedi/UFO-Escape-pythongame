import pygame as pg

pg.init()
screen = pg.display.set_mode((800,600))
pg.display.set_caption('Basketball Game By KshitijSubedi ')
clock=pg.time.Clock()
#logo= pg.image.load("gamelogo32x32.png")
#pg.display.set_icon(logo)
white=(255,255,255)
black=(0,0,0)

#game file haru
ball=pg.image.load("ball.png")
#bg=pg.image.load("bg.png")
#post=pg.image.load("post.png")
#postfc=pg.image.load("postfc.png")


#aba game suru
def bal(x,y):
    screen.blit(ball,(x,y))

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running =False
        print(event)
        if event.type==pg.KEYDOWN:
            pg.message_display('You crashed')
    screen.fill(white)
    pg.display.update()
    pg.draw.rect(screen,(0,128,255),pg.Rect(30,30,60,60,))

    #############
    bal(100,150)
    pg.display.update()
    clock.tick(60)
pg.quit()
quit()




