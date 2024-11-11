import pygame
pygame.init()

#load background images

#set framerate
clock = pygame.time.Clock()
fps = 30
screen_width = 800
screen_height = 600
resolution = (screen_width, screen_height)
screen = pygame.display.set_mode(resolution)

class Player():
    def __init__(self, x, y):
         #store images for animations
         self.images_right = []
         self.images_left = []
         self.images_backward = []
         self.images_forward = []
         self.index = 0
         self.counter = 0
         #run through images for animation 
         for num in range(0, 3):
             img_forward = pygame.image.load(f'img/zombforward{num}.png')
             img_forward = pygame.transform.scale(img_forward, (40, 60))
             self.images_forward.append(img_forward)
         for num in range(1, 5):
             img_backward = pygame.image.load(f'img/zombbackward{num}.png')
             img_backward = pygame.transform.scale(img_backward, (40, 60))
             self.images_backward.append(img_backward)
         self.image = self.images_forward[self.index]    
         img = pygame.image.load('img/player_front.png')
         self.image = pygame.transform.scale((40, 60))
         self.rect = self.image.get_rect()
         self.rect.x = x
         self.rect.y = y 

    def update(self):
        walk_cooldown = 10
        #get key input
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            self.rect.x -= 5
        if key[pygame.K_d]:
            self.rect.x += 5
        if key[pygame.K_w]:
            self.rect.y -= 5
            self.counter += 1
        if key[pygame.K_s]:
            self.rect.y += 5
            self.counter += 1
        #adjust bounds
        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height 
        if self.rect.top < 0:
            self.rect.top = screen_height
        if self.rect.right > screen_width:
            self.rect.right = screen_width
        if self.rect.left < 0:
            self.rect.left = 0
        #animation
        if self.counter > walk_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images_forward):
                self.index = 0
            self.image = self.images_forward[self.index]
        
        #draw player
        screen.blit(self.image, self.rect)


def main():
    pygame.display.set_caption("Zombie Grrrlz")
    player = Player(100, screen_height - 250)

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