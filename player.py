
class Player(object):

      def __init__(self, name, posx, posy, sprite):
          self.name = name
          self.posx = posx
          self.posy = posy
          self.sprite = sprite
          self.state = "standing"

          self.anim_help = 0
          self.anim_speed = 5
          self.model = pygame.image.load("./sprites/player/"+self.sprite+"/m1.png").convert_alpha()

          ##Animations
          self.ani_stand = []
          self.ani_stand.append(pygame.image.load("./sprites/player/"+self.sprite+"/m1.png").convert_alpha())
          self.ani_stand.append(pygame.image.load("./sprites/player/"+self.sprite+"/m2.png").convert_alpha())
          self.ani_stand.append(pygame.image.load("./sprites/player/"+self.sprite+"/m3.png").convert_alpha())
          self.ani_stand.append(pygame.image.load("./sprites/player/"+self.sprite+"/m4.png").convert_alpha())

          for x in range(len(self.ani_stand)):
              self.ani_stand[x] = pygame.transform.scale(self.ani_stand[x], (tile_size[0],tile_size[1]))


          self.ani_walk = []
          self.ani_walk.append(pygame.image.load("./sprites/player/"+self.sprite+"/c1.png").convert_alpha())
          self.ani_walk.append(pygame.image.load("./sprites/player/"+self.sprite+"/c2.png").convert_alpha())
          self.ani_walk.append(pygame.image.load("./sprites/player/"+self.sprite+"/c3.png").convert_alpha())
          self.ani_walk.append(pygame.image.load("./sprites/player/"+self.sprite+"/c4.png").convert_alpha())

          for x in range(len(self.ani_walk)):
              self.ani_walk[x] = pygame.transform.scale(self.ani_walk[x], (tile_size[0],tile_size[1]))



      def __del__(self):
          print "Player "+ name + " destroyed"

      def blit(self):
          self.animation()
          if(self.state != "jumping"):
             self.fall()
          self.font = pygame.font.Font(None, 15)
          self.text2 = self.font.render(self.name, 5, (255, 255, 240))
          screen.blit(self.text2, (self.posx, self.posy-12))
          screen.blit(self.model, (self.posx , self.posy))

      def animation(self):
          if(self.anim_speed == 0):
              if(self.state == "standing"):
                            self.model = pygame.transform.flip(self.ani_stand[self.anim_help], True, False)
                            self.anim_help += 1
              if(self.anim_help > len(self.ani_stand)):
                                self.anim_help = 0


              if(self.state == "walking_right"):
                            self.model = pygame.transform.flip(self.ani_walk[self.anim_help], True, False)
                            self.anim_help += 1
              if(self.anim_help > len(self.ani_walk)-1):
                                self.anim_help = 0


              if(self.state == "walking_left"):
                            self.model = pygame.transform.flip(self.ani_walk[self.anim_help], False, False)
                            self.anim_help += 1
              if(self.anim_help > len(self.ani_walk)-1):
                                self.anim_help = 0
              self.anim_speed = 5
          else:
               self.anim_speed -= 1

      def standing(self):
            self.state = "standing"

      def move_right(self):
          if(not(self.collision("right"))):
              if(self.posx < window_size[0]-self.model.get_width()):
                  self.posx += 3
                  self.state = "walking_right"

      def move_left(self):
          if(not(self.collision("left"))):
             if(self.posx-1 > 0):
                self.posx -= 3
                self.state = "walking_left"

      def jump(self):
          if(not(self.collision("up"))):
                  self.state = "jumping"
                  self.posy -= 5

      def fall(self):
          if(self.collision("down") != True):
              self.posy += 5

      def collision(self, direction):

          for self.zeile in range(len(world.tiles)):
            for self.feld in range(len(world.tiles[0])):
                if(type(world.tiles[self.zeile][self.feld]) is not str):
                   self.world_rect = pygame.Rect(self.feld*tile_size[0], self.zeile*tile_size[1], tile_size[0], tile_size[1])
                else:
                   self.world_rect = pygame.Rect(-64, -64, 64, 64)

                if(direction == "right"):
                   self.player_rect =  pygame.Rect(self.posx, self.posy, tile_size[0]-10, tile_size[1])
                   if(self.player_rect.colliderect(self.world_rect)      and      self.player_rect.x < self.world_rect.x):
                      return True
                if(direction == "left"):
                   self.player_rect =  pygame.Rect(self.posx-1, self.posy, tile_size[0]-10, tile_size[1])
                   if(self.player_rect.colliderect(self.world_rect)      and      self.player_rect.x > self.world_rect.x):
                      return True
                if(direction == "up"):
                   self.player_rect =  pygame.Rect(self.posx+10, self.posy-2.9, tile_size[0]-10, tile_size[1])
                   if(self.player_rect.colliderect(self.world_rect)      and      self.player_rect.y >= self.world_rect.y):
                      return True
                if(direction == "down"):
                   self.player_rect =  pygame.Rect(self.posx, self.posy, tile_size[0]-14, tile_size[1]+3)
                   if(self.player_rect.colliderect(self.world_rect)      and      self.player_rect.y < self.world_rect.y):
                      return True




