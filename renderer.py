## Imports
import pygame
if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'
import time
import maps
## Vars1 Init
gamename = "Adventure of Dauth"
mapfile = "map1"
window_size = (1024,768)
tile_size = (window_size[0]/16, window_size[1]/12)
fps = 30
pygame.init()

## Display Clock
screen = pygame.display.set_mode(window_size, 0, 32)
screen.fill((255, 255, 255))
clock = pygame.time.Clock()
world = World(mapfile, screen, "map2", "map3")
player = Player("Player", world.map.spawn[0], world.map.spawn[1]*tile_size[1], "0")


done = False
while not done:
        ## Eventhandler (Einmalige Tastenabfrage)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                   done = True
                """if event.type == pygame.KEYDOWN:
                   if event.key == pygame.K_SPACE:
                      player.jump()"""


        ## Tastenabfrage jeden Frame
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_RIGHT]:
             world.move_layer1_left()
             player.move_right()
        if pressed[pygame.K_LEFT]:
             world.move_layer1_right()
             player.move_left()
        if pressed[pygame.K_UP]:
             player.jump()
        if pressed[pygame.K_DOWN]:
             player.fall()
        if not(pressed[pygame.K_LEFT]) and not(pressed[pygame.K_RIGHT]) and not(pressed[pygame.K_UP]):
            player.standing()
        

        world.blit()
        player.blit()
        pygame.display.set_caption("Adventure of Dauth - FPS: " + str(clock.get_fps())[:5])
        pygame.display.update()
        clock.tick(fps)


pygame.quit()
