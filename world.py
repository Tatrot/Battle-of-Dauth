
class World(object):

    def __init__(self, map_file, pygame_display, map_left, map_right):
        self.map = getattr(__import__("maps", fromlist=[map_file]), map_file)
        self.load_map(map_file)
        self.screen = pygame.display

        self.pos_layer0 = 0
        self.size_layer0 = self.layer0.get_size()
        self.helper_layer0 = "left"

        self.pos_layer1 = 0
        self.size_layer1 = self.layer1.get_size()

        self.map_left = map_left
        self.map_right = map_right


    def __del__(self):
        pass


    def load_map(self, map_file):
        self.layer0 = pygame.image.load(self.map.layer0).convert()
        self.layer0 = pygame.transform.scale(self.layer0, (window_size[0]+200,window_size[1]+200))

        self.layer1 = pygame.image.load(self.map.layer1).convert_alpha()
        self.layer1 = pygame.transform.scale(self.layer1, (window_size[0]+200,window_size[1]+200))

        self.tiles = []


        for self.zeile in range(len(self.map.map_data)):
            self.tiles.append([])
            for self.feld in range(len(self.map.map_data[0])):
                if self.map.map_data[self.zeile][self.feld] > 0:
                    self.tiles[self.zeile].append(pygame.image.load(self.map.tileset[self.map.map_data[self.zeile][self.feld]]).convert_alpha())
                    self.tiles[self.zeile][-1] = pygame.transform.scale(self.tiles[self.zeile][-1], (tile_size[0],tile_size[1]))
                else:
                    self.tiles[self.zeile].append(self.map.tileset[0])

    def blit(self):
        self.move_layer0()
        screen.blit(self.layer0, (self.pos_layer0 , 0))
        screen.blit(self.layer1, (self.pos_layer1 , 0))
        for self.zeile in range(len(self.tiles)):
            for self.feld in range(len(self.tiles[0])):
                if(self.tiles[self.zeile][self.feld] == "none"):
                    pass
                else:
                    screen.blit(self.tiles[self.zeile][self.feld], (self.feld*tile_size[0] , self.zeile*tile_size[1]))


    def move_layer1_left(self):
        if(self.pos_layer1 - 1 > -200):
            self.pos_layer1 -= 0.5

    def move_layer1_right(self):
        if(self.pos_layer1 + 1 < 0):
            self.pos_layer1 += 0.5

    def move_layer0(self):
        if(self.helper_layer0 == "left"):
                self.pos_layer0 = self.pos_layer0 - 0.45
                if(self.pos_layer0 <= -200):
                    self.helper_layer0 = "right"

        if(self.helper_layer0 == "right"):
                self.pos_layer0 = self.pos_layer0 + 0.45
                if(self.pos_layer0 >= 0):
                    self.helper_layer0 = "left"
