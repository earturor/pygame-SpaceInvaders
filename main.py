import math
import pygame

def main():
    # Intialize the game
    pygame.init()

    # Create the screen
    width = 512
    height = 512
    screen = pygame.display.set_mode((width, height))

    # Background
    background = pygame.image.load('assets/Blue_Nebula_01-512x512.png')
    bgScroll = 0
    tiles = math.ceil(height / background.get_height()) + 1

    # Background music
    pygame.mixer.music.load('assets/Sci-Fi_1_Loop.mp3')
    pygame.mixer.music.play(loops=-1)
    pygame.mixer.music.set_volume(0.2)

    # Caption and icon
    pygame.display.set_caption("Space Invaders")
    icon = pygame.image.load('assets/spaceship_icon.png')
    pygame.display.set_icon(icon)

    # Player
    playerImage = pygame.image.load('assets/spaceship.png')
    playerPosX = 240
    playerPosY = 460
    playerPosX_change = 0
    playerPosY_change = 0
    playerSpeed = 0.2

    # Enemy
    enemyImage = pygame.image.load('assets/ovni.png')
    enemyPosX = 240
    enemyPosY = 0
    enemyPosX_change = 0
    enemyPosY_change = 0
    enemySpeed = 0.1

    def player(posX, posY):
        screen.blit(playerImage, (posX, posY))

    def enemy(posX, posY):
        screen.blit(enemyImage, (posX, posY))

    # Define a varible to control the main loop
    running = True
    # Define a variable to control the movement of the enemy at the start
    pxs = 0
    # Main loop
    while running:

        # Looping background
        for i in range(tiles):
            screen.blit(background, (0, -background.get_height() * i + bgScroll))
        
        bgScroll += 0.01
        if abs(bgScroll) > background.get_height():
            bgScroll = 0

        # Event handling, gets all event from the event queue
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # only do something if the event is of type QUIT
                running = False # change the value to False to exit the main loop

            # if keystroke is pressed, check wether its left, down, up or down
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    playerPosX_change = -playerSpeed
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    playerPosX_change = playerSpeed
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    playerPosY_change = -playerSpeed
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    playerPosY_change = playerSpeed
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_d:
                    playerPosX_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_w or event.key == pygame.K_s:
                    playerPosY_change = 0

        # X position limits on screen
        playerPosX += playerPosX_change
        if playerPosX <= 15:
            playerPosX = 15
        elif playerPosX >= 465:
            playerPosX = 465
        # Y position limits on screen
        playerPosY += playerPosY_change
        if playerPosY <= 20:
            playerPosY = 20
        elif playerPosY >= 460:
            playerPosY = 460

        # Enemy movement
        if pxs < 400:
            enemyPosY_change = enemySpeed
            enemyPosY += enemyPosY_change
            enemyPosX = 200 * math.sin(enemyPosY / 32) + 240
            pxs += enemySpeed
        elif pxs >= 400 and pxs < 750:
            enemyPosY_change = -enemySpeed
            enemyPosY += enemyPosY_change
            enemyPosX_change = enemySpeed
            enemyPosX -= enemyPosX_change / (400 / 240)
            pxs += enemySpeed
        else:
            enemyPosX_change = 0
            enemyPosY_change = 0


        player(playerPosX, playerPosY)
        enemy(enemyPosX, enemyPosY)
        pygame.display.update()

if __name__ == '__main__':
    main()