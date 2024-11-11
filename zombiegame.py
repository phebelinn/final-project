import pygame
pygame.init()
#define walking

#load background images

#set framerate
clock = pygame.time.Clock()
fps = 30
screen_width = 800
screen_height = 600
resolution = (screen_width, screen_height)
screen = pygame.display.set_mode(resolution)

class Player():
    def __init__(self, x, y, z):
         img = pygame.image.load('img/player_front.png')
         self.image = pygame.transform.scale((40, 60))
         self.rect = self.image.get_rect()
         self.rect.x = x
         self.rect.y = y 

    def update(self):
        #get key input
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            self.rect.x -= 5
        if key[pygame.K_d]:
            self.rect.x += 5
        if key[pygame.K_w]:
            self.rect.y -= 5
        if key[pygame.K_s]:
            self.rect.y += 5
        #adjust bounds
        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height 
        if self.rect.top < 0:
            self.rect.top = screen_height
        if self.rect.right > screen_width:
            self.rect.right = screen_width
        if self.rect.left < 0:
            self.rect.left = 0
        
        #draw player
        screen.blit(self.image, self.rect)


def main():
    pygame.display.set_caption("Zombie Grrrlz")
    player = Player(100, screen_height - 300)

    running = True
    while running:
        clock.tick(fps)
        player.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()

if __name__ == "__main__":
    main()