import pygame

#define walking

#load background images

class Player():
    def __init__(self, x, y):
         img = pygame.image.load()

def main():
    pygame.init()
    pygame.display.set_caption("Zombie Grrrlz")
    running = True
    resolution = (800, 600)
    screen = pygame.display.set_mode(resolution)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

if __name__ == "__main__":
    main()