import pygame

#define walking

#set up display window with map

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