import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import  log_state 

def main():
    pygame.init()

    # set up the display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((92, 148, 252))
        pygame.display.flip()



if __name__ == "__main__":
    main() 
