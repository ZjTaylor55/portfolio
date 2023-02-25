import os
import pygame
pygame.init()

#create window
width, height = 1920,1080
window = pygame.display.set_mode((width,height))
#framerate stuff
clock = pygame.time.Clock()

#window name
pygame.display.set_caption('Move Karl')

#background image
bg_img = pygame.image.load('images/grass.png')
bg_img = pygame.transform.scale(bg_img,(width,height))

class Player(object):
    #create the user as karl
    def __init__(self):
        self.karl = pygame.image.load('images/karl.jpg')
        self.karl = pygame.transform.scale(self.karl, (150,150))
        #this bit here makes a rectangle for karl that will handle collision
        karl_rect = self.karl.get_rect()
        karl_rect.center = (150, 150)

    #add key input to move karl
    def movement_keys(self):
        keys = pygame.key.get_pressed()
                #karl's initial position
        self.x = 960
        self.y = 540
        #how far karl moves
        velocity = 100 #this needs to be changed back to 10 was increased for testing purposes

        if keys[pygame.K_a]:
                self.x -= velocity

        if keys[pygame.K_d]:
                self.x += velocity

        if keys[pygame.K_w]:
                self.y -= velocity

        if keys[pygame.K_s]:
                self.y += velocity

    #spawn karl
    def draw(self, surface):
        surface.blit(self.karl, (self.x, self.y))

user = Player()

#main loop
running = True
while running:
    window.blit(bg_img,(0,0))
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == quit:
            running = False
    #allows you to actually move karl
    user.movement_keys()
    #actually spawns karl
    user.draw(window)
    pygame.display.update()
pygame.quit()