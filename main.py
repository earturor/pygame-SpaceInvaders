import pygame
from pygame import mixer

def main():
    # Intialize the game
    pygame.init()

    # Create the screen
    screen = pygame.display.set_mode((512, 512))

    # Background
    background = pygame.image.load('assets/Blue_Nebula_01-512x512.png')

    # Background music
    mixer.music.load('assets/Sci-Fi_1_Loop.mp3')
    mixer.music.play(loops=-1)
    mixer.music.set_volume(0.2)

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

    def player(posX, posY):
        screen.blit(playerImage, (posX, posY))

    # Define a varible to control the main loop
    running = True

    # Main loop
    while running:

        # RGB = Red, Green, Blue
        screen.fill((0, 0, 0))
        #Background image
        screen.blit(background, (0, 0))
        # Event handling, gets all event from the event queue
        for event in pygame.event.get():
            # Only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # Change the value to False to exit the main loop
                running = False

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

        # Position limits on screen
        playerPosX += playerPosX_change
        if playerPosX <= 20:
            playerPosX = 20
        elif playerPosX >= 460:
            playerPosX = 460

        playerPosY += playerPosY_change
        if playerPosY <= 20:
            playerPosY = 20
        elif playerPosY >= 460:
            playerPosY = 460

        player(playerPosX, playerPosY)
        pygame.display.update()

if __name__ == '__main__':
    main()