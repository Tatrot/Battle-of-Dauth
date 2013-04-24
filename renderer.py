## Imports
import pygame
if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'
import time



gamename = "Battle of Dauth"
__builtins__.window_size = (1280,900)
__builtins__.tile_size = (window_size[0]/25, window_size[1]/16)
fps = 60
__builtins__.px = 0
__builtins__.py = 480
pygame.init()

__builtins__.screen = pygame.display.set_mode(window_size, 0, 32)
__builtins__.screen.fill((255, 255, 255))
clock = pygame.time.Clock()

from world import World
world = World()


done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            


        ## Tastenabfrage jeden Frame
    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_RIGHT]:
        __builtins__.px += 6
    if pressed[pygame.K_LEFT]:
        __builtins__.px -= 6
    if pressed[pygame.K_UP]:
        __builtins__.py -= 6
    if pressed[pygame.K_DOWN]:
        __builtins__.py += 6
    if not(pressed[pygame.K_LEFT]) and not(pressed[pygame.K_RIGHT]) and not(pressed[pygame.K_UP]):
        pass


    world.blit()
    pygame.display.set_caption("Adventure of Dauth - FPS: " + str(clock.get_fps())[:5])
    pygame.display.update()
    clock.tick(fps)


pygame.quit()
