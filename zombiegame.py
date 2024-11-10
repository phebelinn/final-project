import pygame

#define walking

#load background images

#set framerate
clock = pygame.time.Clock()
fps = 24
screen_width = 800
screen_height = 600
resolution = (screen_width, screen_height)
screen = pygame.display.set_mode(resolution)

class Player():
    def __init__(self, x, y):
         img = pygame.image.load('img/player_front.png')
         self.image = pygame.transform.scale((40, 60))
         self.rect = self.image.get_rect()
         self.rect.x = x
         self.rect.y = y 

    def update(self):
        #get key input
        key = pygame.key.get_pressed()
        if key[pygame.A]:
            self.rect.x -= 5

        #draw player
        screen.blit(self.image, self.rect)


def main():
    pygame.init()
    pygame.display.set_caption("Zombie Grrrlz")
    player = Player(100, screen_height - 300)

    running = True
    while running:
        player.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()

if __name__ == "__main__":
    main()