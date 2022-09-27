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
bg_img = pygame.image.load('images/arnhelm.png')
bg_img = pygame.transform.scale(bg_img,(width,height))

#add karl
karl = pygame.image.load('images/karl.jpg')
karl = pygame.transform.scale(karl, (150,150))

#karl's initial position
x = 960
y = 540

#how far karl moves
velocity = 10

#main loop
running = True
while running:
        clock.tick(60)
        window.blit(bg_img,(0,0))
        window.blit(karl, (x,y))
        for event in pygame.event.get():
            if event.type == quit:
                running = False
            #checking key press for direction
            keys = pygame.key.get_pressed()

            if keys[pygame.K_a]:
                x -= velocity

            if keys[pygame.K_d]:
                x += velocity

            if keys[pygame.K_w]:
                y -= velocity

            if keys[pygame.K_s]:
                y += velocity
        #    This works however it requires many more keypresses so do not use this method. Use the one above
        #    if event.type == pygame.KEYDOWN:
                #left
        #        if event.key == pygame.K_a:
        #            x -= 5
                #right
        #        if event.key == pygame.K_d:
        #            x += 5
                #up
        #        if event.key == pygame.K_s:
        #            y += 5
                #down
        #        if event.key == pygame.K_w:
        #           y -= 5
        pygame.display.update()
pygame.quit()