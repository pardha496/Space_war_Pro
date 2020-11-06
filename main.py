import math
import random
from typing import Collection
import pygame
from pygame import mixer

# Initialize the pygame
pygame.init()

# Dimensions
WIDTH, HEIGHT = 750, 750

# Clock
clock = pygame.time.Clock()

# Fonts
lost_font = pygame.font.SysFont("comicsans", 50)

# screen resolution
screen = pygame.display.set_mode((800, 600))

# Background Image
background = pygame.image.load('assets/background.png')

# Opening Sound
mixer.music.load("assets/background.wav")
mixer.music.play(-1)

# Game Title and Icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('assets/player.png')
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('assets/enemy.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(1)
    enemyY_change.append(5)


# Bullet

# Ready - You can't see the bullet
# Fire - The bullet is currently moving
bulletImg = pygame.image.load('assets/bullet.png')
bulletX = 0
bulletY = 480
bulletX_change=0
bulletY_change=10
bullet_state="ready"

# Score
score_value=0
font=pygame.font.Font('freesansbold.tff',32)
textX=10
textY=10

# define game pause here
# def pause()
 
# Game Over
over_font=pygame.font.Font('freesansbold.ttf',64)

def endofLevel1 ():
    levelEnd = over_font.render("Thanks for play!", True, (255, 255, 255))
    screen.blit(levelEnd, (200, 250))
    levelEnd = over_font.render("Level 1 Completed", True, (255, 255, 255))
    screen.blit(levelEnd, (110, 340))

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


# Game Loop
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

    while running:

        # RGB = Red, Green, Blue filters for game
        screen.fill((0, 0, 0)) # Setting default to value 0
        
        # Calling background image
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            # if keystroke is pressed check conditions
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_change = -5
                if event.key == pygame.K_RIGHT:
                    playerX_change = 5
                if event.key == pygame.k_SPACE:
                    if bullet_state == "ready":
                        bulletsound = mixer.Sound("assets/laser.wav")
                        bulletsound.play()

                        # Get the current x cordinate of the spaceship
                        bulletX = playerX
                        fire_bullet(bulletX, bulletY)
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0

        # 5 = 5 + -0.1 -> 5 = 5 - 0.1
        # 5 = 5 + 0.1

        playerX += playerX_change
        if playerX <= 0:
            playerX = 0
        elif playerX > 736:
            playerX = 736
        
        # Enemy Movement
        if i in range(num_of_enemies):

            # Game Over
            if enemyY[i] > 400:
                for j in range (num_of_enemies):
                    enemyY[j] = 2000
                game_over_text()
                break
            elif score_value >= 7:
                endofLevel1()
                break
            else:
                enemyX[i] += enemyX_change[i]
                if enemyX[i] <= 0:
                    enemyY_change[i] = 4
                    enemyY[i] += enemyY_change[i]
                elif enemyX[i] >= 736:
                    enemyX_change[i] = -4
                    enemyY[i] += enemyY_change[i]
                
                # Collision
                collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
                if collision:
                    explosionSound = mixer.Sound("assets/explosion.wav")
                    explosionSound.play()
                    bulletY = 480
                    bullet_state = "ready"
                    score_value += 1
                    enemyX[i] = random.randint(0, 736)
                    enemyY[i] = random.randint(50, 150)
                
                enemy(enemyX[i], enemyY[i], i)
    
    # BUllet Movement
    if bulletY <= 0:
        bulletY = 400
        bullet_state = "ready"
    
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletX_change
    
    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()