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
             img_forward = pygame.transform.scale(img_forward, (120, 150))
             self.images_forward.append(img_forward)
         for num in range(1, 5):
             img_backward = pygame.image.load(f'img/zombbackward{num}.png')
             img_backward = pygame.transform.scale(img_backward, (120, 150))
             self.images_backward.append(img_backward)
         self.image = self.images_forward[self.index]    
         img = pygame.image.load('img/zombforward1.png')
         self.image = pygame.transform.scale(img, (120, 150))
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
        if key[pygame.K_a] == False and key[pygame.K_d] == False and key[pygame.K_w] == False and key[pygame.K_s] == False: 
            self.index = 0
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

def display_game(screen, player, map_number):
    #displays background map and player
    pygame.display.set_caption("Zombie Grrrlz")
    map = pygame.image.load(f'img/map{map_number}.png') 
           

def main():
    player = Player(100, screen_height - 250)
    running = True
    while running:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        map_number = 1
        display_game(screen, Player, map_number)
        pygame.display.flip()
        player.update()

        if player.rect.x > 760 and player.rect.y > 200 and player.rect.y < 400:
            map_number += 1 
    pygame.quit()

if __name__ == "__main__":
    main()