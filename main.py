import pygames

pygames.init()

playerImg = pygames.image.load('assets/player.png')
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

bulletImg = pygame.image.load('assests/bullet.png')
bulletX = 0
bulletY = 480
bulletX_change=0
bulletY_change=10
bullet_state="ready"

score_value=0
font=pygame.font.Font('freesansbold.tff',32)
textX=10
textY=10

over_font=pygame.font.Font('freesansbold',64)

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