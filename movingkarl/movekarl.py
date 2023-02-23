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

#add karl
karl = pygame.image.load('images/karl.jpg')
karl = pygame.transform.scale(karl, (150,150))
#this bit here makes a rectangle for karl that will handle collision
karl_rect = karl.get_rect()
karl_rect.center = (960, 540)

#karl's initial position
karl_rect.x = 960
karl_rect.y = 540

#how far karl moves
velocity = 10

#adding some fences
fence = pygame.image.load('images/fence.png')
fence = pygame.transform.scale(fence, (100,200))
fence_rect = fence.get_rect()
fence_rect.center = (500, 200)
fence_rect.x = 500
fence_rect.y = 200

#main loop
running = True
while running:
        clock.tick(60)
        window.blit(bg_img,(0,0))
        window.blit(karl, karl_rect)
        window.blit(fence, fence_rect)
        for event in pygame.event.get():
            if event.type == quit:
                running = False
            #checking key press for direction
            keys = pygame.key.get_pressed()

            if keys[pygame.K_a]:
                karl_rect.x -= velocity

            if keys[pygame.K_d]:
                karl_rect.x += velocity

            if keys[pygame.K_w]:
                karl_rect.y -= velocity

            if keys[pygame.K_s]:
                karl_rect.y += velocity
            #checking if karl has ran into the fence
            collide = pygame.Rect.colliderect(karl_rect, fence_rect)
            if karl_rect.colliderect(fence_rect):

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