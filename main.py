import pygames

pygames.init()

playerImg = pygames.image.load('assets/player.png')
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

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