from pygame import *
import math
import time
import c4w

#initialize pygame
init()

#create screen
screen = display.set_mode((1000,600))

#asthetics
display.set_caption("TicTacToe")
icon = image.load('icons/tic-tac-toe.png')
display.set_icon(icon)

#grid
grid = transform.scale(image.load('icons/grid.png'), (500,500))
gridX = 500
gridY = 310
def printGrid():
    screen.blit(grid,(gridX-grid.get_width()/2,gridY-grid.get_height()/2),)

#all placed o and x
xlist = []
olist = []

#button
class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        action = False
        pos = mouse.get_pos()

        if self.rect.collidepoint(pos):
            if mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
            if mouse.get_pressed()[0] == 0:
                self.clicked = False

        #draw button on screen
        screen.blit(self.image,(self.rect.x,self.rect.y))
        return action

replay_btn = Button(805,235,transform.scale(image.load('icons/replay.png'), (130,130)))

x_coordinates_of_Rublikas = [342,500,656]
y_coordinates_of_Rublikas = [155,310,464]

#dict of Rublikas
rublikas = {
    x_coordinates_of_Rublikas[0]: [i for i in y_coordinates_of_Rublikas],
    x_coordinates_of_Rublikas[1]: [i for i in y_coordinates_of_Rublikas],
    x_coordinates_of_Rublikas[2]: [i for i in y_coordinates_of_Rublikas]
}

#x
ximage = transform.scale(image.load('icons/x.png'), (80,80))
#o
oimage = transform.scale(image.load('icons/o.png'), (90,90))
#x won msg
xwonimage = image.load('icons/xwon.png')
#o won msg
owonimage = image.load('icons/owon.png')

#draw o and x
def printx():
    for x in xlist:

        screen.blit(ximage,(x[0]-ximage.get_width()/2,x[1]-ximage.get_height()/2),)
    
def printo():
    for o in olist:

        screen.blit(oimage,(o[0]-oimage.get_width()/2,o[1]-oimage.get_height()/2),)

#which player's turn is it
nextUp = 0 #0 means X, 1 means O

#game loop
running = True
while running:

    screen.fill((202,228,241)) #bg color

    for ev in event.get(): #going through all events that are happening
        if ev.type == QUIT:
            running = False
        if ev.type == MOUSEBUTTONUP and winner == None:
            pos = mouse.get_pos()
            distance = 20000
            closest = 0
            for key in rublikas:
                for y in rublikas[key]:
                    if math.sqrt((pos[0]-key)**2+(pos[1]-y)**2)<distance:
                        distance = math.sqrt((pos[0]-key)**2+(pos[1]-y)**2)
                        closest=(key,y)
            if not ((closest in olist) or (closest in xlist)):
                if nextUp == 0:
                    xlist.append(closest)
                    nextUp = 1
                else:
                    olist.append(closest)
                    nextUp = 0

    printGrid()
    printx()
    printo()

    finished = c4w.checkForWinner(xlist,olist,rublikas)[0]
    winner = c4w.checkForWinner(xlist,olist,rublikas)[1]

    if finished:
        if replay_btn.draw():
            
                xlist
                olist
                nextUp
                xlist = []
                olist = []
                nextUp = 0
                time.sleep(0.1)

        if winner == 'x':
            screen.blit(xwonimage,(500-xwonimage.get_width()/2,0))

        if winner == 'o':
            screen.blit(owonimage,(500-owonimage.get_width()/2,0))
        
        if winner == 'no one':
            pass

    display.update()