import os
import pygame
pygame.init()

class Player(object):
    #create the user as karl
    def __init__(karl):
        karl = pygame.image.load('images/karl.jpg')
        karl = pygame.transform.scale(karl, (150,150))
        #this bit here makes a rectangle for karl that will handle collision
        karl_rect = karl.get_rect()
        karl_rect.center = (960, 540)

    #add key input to move karl
    def movement_keys(karl):
        keys = pygame.key.get_pressed()
        #how far karl moves
        velocity = 10

        if keys[pygame.K_a]:
                karl.x -= velocity

        if keys[pygame.K_d]:
                karl.x += velocity

        if keys[pygame.K_w]:
                karl.y -= velocity

        if keys[pygame.K_s]:
                karl.y += velocity

    #spawn karl
    def spawn(karl, surface):
          surface.blit(karl, (960, 540))

player = Player()
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

#main loop
running = True
while running:
    window.blit(bg_img,(0,0))
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == quit:
            running = False
    #allows you to actually move karl
    player.movement_keys()
    #actually spawns karl
    player.spawn(window)


    pygame.display.update()
pygame.quit()