from player import Player
import pygame
from constants import *
from logger import log_state

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    
    clock = pygame.time.Clock()
    dt = 0
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        player.update(dt)
        screen.fill("black")  # Clear the screen with black
        player.draw(screen)
        pygame.display.flip()
        clock.tick(60)  # Limit to 60 frames per second
        dt = clock.get_time() / 1000.0  # Convert milliseconds to seconds
        

if __name__ == "__main__":
    main()
