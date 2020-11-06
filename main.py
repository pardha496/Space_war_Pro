import math
import random

import pygames
from pygame import mixer

pygames.init()

screen = pygames.display.set_mode((800, 600))

background = pygames.image.load('assests/background.png')

mixer.music.load("assests/background.wav")
mixer.music.play(-1)

pygames.display.set_caption("Space Invader")
icon = pygames.image.load('ufo.png')
pygames.display.set_icon(icon)

playerImg = pygames.image.load('assests/player.png')
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('assests/enemy.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)

bulletImg = pygames.image.load('assests/bullet.png')
bulletX = 0
bulletY = 480
bulletX_change=0
bulletY_change=10
bullet_state="ready"

score_value=0
font=pygames.font.Font('freesansbold.tff',32)
textX=10
textY=10

over_font=pygames.font.Font('freesansbold',64)

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

running = True

def main():

    global playerImg
    global playerX
    global playerY
    global playerX_change
    global bulletY
    global bulletX
    global bullet_state
    global score_value
    global running
    global win