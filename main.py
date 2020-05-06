import pygame as py
import time
import math
import random
from pygame import mixer

py.init ( )
screen = py.display.set_mode ((400, 600))

back=mixer.Sound("background.wav")
back.play(-1)
blast=mixer.Sound("explosion.wav")

icon = py.image.load ("vehicle.png")
py.display.set_icon (icon)

py.display.set_caption ("Car Crash")

playerImg = py.image.load ("transport.png")

# variables
playerX_change = 0
playerY_change = 0
midX = 185
midY = 70

width = 20
height = 100
g=1
playerX = 150
playerY = 520

enemyImg = []
enemyX = []
enemyY = []
enemyY_change = 0.8
num_of_car = 2

enemyImg.append (py.image.load ("oponent.png"))

enemyImg.append (py.image.load ("oponent.png"))
enemyX.append (random.randint (200, 250))

enemyX.append (random.randint (235, 280))
enemyY.append (random.randint (-200, -100))

enemyY.append (random.randint (60, 100))

enemy2Img = []
enemy2X = []
enemy2Y = []
enemy2Y_change = -0.8
num_of_car2 = 2

enemy2Img.append (py.image.load ("transport.png"))
#enemyImg.append (py.image.load ("oponent.png"))
enemy2Img.append (py.image.load ("transport.png"))
enemy2X.append (random.randint (70, 100))
#enemyX.append (random.randint (210, 235))
enemy2X.append (random.randint (125, 130))
enemy2Y.append (random.randint (700, 900))
#enemyY.append (random.randint (-50, 20))
enemy2Y.append (random.randint (300, 450))

go_font = py.font.Font("freesansbold.ttf",32)

def isColision(px,pY,ex,ey):
    distance = math.sqrt (math.pow ((px - ex), 2) + math.pow ((pY - ey), 2))
    if distance <50:
        return True
    else:
        return False

def g1():
    if g ==0:

        return True
    else:
        return False

def isColision2(px, pY, e2x, e2y):
    distance = math.sqrt (math.pow ((px - e2x), 2) + math.pow ((pY - e2y), 2))
    if distance < 50:
        return True
    else:
        return False

def enemy(enx, eny, i):
    screen.blit (enemyImg[i], (enx, eny))


def enemy2(enx, eny, i):
    screen.blit (enemy2Img[i], (enx, eny))


def player(x, y):
    screen.blit (playerImg, (x, y))

def GO():
    gO = go_font.render ("Game Over!", True, (255, 0, 0))
    screen.blit (gO, (100, 280))

    back.stop()

running = True
while running:
    screen.fill ((40, 255, 30))
    if midY > 530:
        midY = 0

    py.draw.rect (screen, (255, 255, 255), (midX, (midY - 300), width, height))
    py.draw.rect (screen, (255, 255, 255), (midX, (midY), width, height))
    py.draw.rect (screen, (255, 255, 255), (midX, (midY + 300), width, height))
    py.draw.rect (screen, (0, 0, 0), (0, 0, 70, 600))
    py.draw.rect (screen, (0, 0, 0), (330, 0, 400, 600))
    player (playerX, playerY)

    for event in py.event.get ( ):
        if event.type == py.QUIT:
            running = False

        if event.type == py.KEYDOWN:  # keydown means key pressed
            if event.key == py.K_LEFT:
                playerX_change = -1

            if event.key == py.K_RIGHT:
                playerX_change = 1

            if event.key == py.K_UP:
                playerY_change = -1

            if event.key == py.K_DOWN:
                playerY_change = 1


        if event.type == py.KEYUP:
            if event.key == py.K_RIGHT or event.key == py.K_LEFT or event.key == py.K_UP or event.key == py.K_DOWN:
                playerX_change = 0
                playerY_change = 0

        if g1():
            GO()

            break
        # player mechanism
    playerX += playerX_change
    playerY += playerY_change

    if playerX <= 70:
        playerX = 70
    elif playerX >= 330:
        playerX = 330

    if playerY <= 0:
        playerY = 0
    elif playerY >= 570:
        playerY = 570

    # mid (midX,midY,height,width)



    for i in range (num_of_car):
        enemy (enemyX[i], enemyY[i], i)
        enemyY[i] += enemyY_change
        if enemyY[i] > 600:
            enemyY[i] = random.randint (0, 40)

        if g1():
            GO()
            #blast.stop ( )
            break
    for i in range (num_of_car2):
        enemy2 (enemy2X[i], enemy2Y[i], i)
        enemy2Y[i] += enemy2Y_change
        if enemy2Y[i] < -100:
            enemy2Y[i] = random.randint (600, 700)

        if g1():
            GO()

            break

    for i in range(2):
        if isColision(playerX,playerY,enemyX[i],enemyY[i]) or isColision2(playerX,playerY,enemy2X[i],enemy2Y[i]):
            blast.play ( )
            enemyY_change=0
            enemyY[i]=2000
            enemy2Y_change=0
            enemy2Y[i]=2000
            GO()
            #blast.stop ( )
            midY +=0
            g=0
            break
        elif g==1:
            midY += 1



    py.display.update ( )
