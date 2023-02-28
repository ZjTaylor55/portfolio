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

#a class that contains all things relating to the player
class Player(object):
        #create the user as karl
        def __init__(self):
                self.karl = pygame.image.load('images/karl.jpg')
                self.karl = pygame.transform.scale(self.karl, (150,150))
                #this bit here makes a rectangle for karl that will handle collision
                karl_rect = self.karl.get_rect()
                karl_rect.center = (150, 150)
                #karl's initial position
                self.x = 960
                self.y = 600
                self.velocity = 10

        #spawn karl
        def draw(self, surface):
                surface.blit(self.karl, (self.x, self.y))

#class for all fences and their properties
class Fence(object):
        def __init__(self):
                #make a happy little fence
                self.fence = pygame.image.load('images/fence.png')
                self.fence = pygame.transform.scale(self.fence, (960,400))
                #this bit here makes a rectangle for the fence that will handle collision
                fence_rect = self.fence.get_rect()
                fence_rect.center = (100, 200)
                self.x = 100
                self.y = 200

        #spawn the fence
        def draw(self, surface):
                surface.blit(self.fence, (500,200))
        
user = Player()
fence = Fence()

#main loop
running = True
while running:
        window.blit(bg_img,(0,0))
        clock.tick(60)
        for event in pygame.event.get():
                if event.type == quit:
                        running = False
                
        #collision
        if user.y == fence.y+400 and user.x > fence.x+200 or user.x <= 1440:
                user.y += 10
        if user.y == fence.y and user.x > fence.x+200:
                user.y -= 10

        #user input to move karl
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
                user.x -= user.velocity

        if keys[pygame.K_d]:
                user.x += user.velocity

        if keys[pygame.K_w]:
                user.y -= user.velocity

        if keys[pygame.K_s]:
                user.y += user.velocity

        #karl's coordinates for debugging
        print(user.x, user.y, fence.x)
        #actually spawns karl
        user.draw(window)
        fence.draw(window)
        pygame.display.update()
pygame.quit()