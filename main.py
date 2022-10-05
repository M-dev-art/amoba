from pygame import *
import math
import time
import checkforwinner as cfw
#initialize pygame
init()

#parameters;
#can only be set here at the moment

size_of_play_area = 10
amount_needed_for_win = 5

#create screen
screen = display.set_mode((1000,600))

#asthetics
display.set_caption("TicTacToe")
icon = image.load('icons/tic-tac-toe.png')
display.set_icon(icon)

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




size_of_half_a_Rublika = 500/(size_of_play_area*2)


x_coordinates_of_Rublikas = []
y_coordinates_of_Rublikas = []

for i in range(size_of_play_area*2):
    if i % 2 != 0:
        x_coordinates_of_Rublikas.append(250+i*size_of_half_a_Rublika)
        y_coordinates_of_Rublikas.append(80+i*size_of_half_a_Rublika)




#dict of Rublikas
rublikas = {}
for j in range(size_of_play_area):
    keyx = x_coordinates_of_Rublikas[j]
    rublikas[keyx] = [i for i in y_coordinates_of_Rublikas]


#square
size_of_square = x_coordinates_of_Rublikas[1]-x_coordinates_of_Rublikas[0]
square = transform.scale(image.load('icons/square.png'), (size_of_square,size_of_square))

"""
#grid
grid = transform.scale(image.load('icons/grid.png'), (500,500))
gridX = 500
gridY = 310

screen.blit(grid,(gridX-grid.get_width()/2,gridY-grid.get_height()/2),)
"""
def printGrid():
    
    for i in x_coordinates_of_Rublikas:
        for j in y_coordinates_of_Rublikas:
            screen.blit(square,(i-square.get_width()/2,j-square.get_height()/2),)

#x
ximage = transform.scale(image.load('icons/x.png'), (size_of_square*0.7,size_of_square*0.7))
#o
oimage = transform.scale(image.load('icons/o.png'), (size_of_square*0.7,size_of_square*0.7))
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
finished = False
winner = None
while running:

    screen.fill((202,228,241)) #bg color

    
    for ev in event.get(): #going through all events that are happening
        if ev.type == QUIT:
            running = False
        if ev.type == MOUSEBUTTONDOWN and winner == None and ev.button == 1:
            pos = mouse.get_pos()
            distance = 20000
            closest = 0
            for key in rublikas:
                for y in rublikas[key]:
                    if math.sqrt((pos[0]-key)**2+(pos[1]-y)**2)<distance:
                        distance = math.sqrt((pos[0]-key)**2+(pos[1]-y)**2)
                        closest=[key,y]
            if not ((closest in olist) or (closest in xlist)):
                if nextUp == 0:
                    xlist.append(closest)
                    if cfw.checkForWinner(xlist,olist,rublikas,size_of_play_area,amount_needed_for_win,"x",closest):
                        finished = True
                        winner = 'x'
                    nextUp = 1
                else:
                    olist.append(closest)
                    if cfw.checkForWinner(xlist,olist,rublikas,size_of_play_area,amount_needed_for_win,"o",closest):
                        finished = True
                        winner = 'o'
                    nextUp = 0

    printGrid()
    printx()
    printo()

    
    
    if finished:
        if replay_btn.draw():
                
                xlist
                olist
                nextUp
                xlist = []
                olist = []
                nextUp = 0
                finished = False
                winner = None

        if winner == 'x':
            screen.blit(xwonimage,(500-xwonimage.get_width()/2,0))

        if winner == 'o':
            screen.blit(owonimage,(500-owonimage.get_width()/2,0))
        
        if winner == 'no one':
            pass

    display.update()