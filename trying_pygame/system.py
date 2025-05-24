import pygame as pg

import entity
import player

class System:
    def create_world(self):
        gap=64
        
        x_n=0
        y_n=0
        for block in self.level:
            if block == '\n':
                y_n += 1
                x_n=-1
            elif block == '*':
                self.player=player.Player(x_n*gap,y_n*gap,64,64, "../pictures/images.jpg", 64,64)
            elif block == '#':
                self.blocks.append(entity.Entity(x_n*gap,y_n*gap,64,64, "../pictures/images.jpg",64,64))
            x_n+=1
    
    def update(self):
        self.player.move(self.blocks)
        (self.camera_x, self.camera_y) = (self.player.rect.x, self.player.rect.y)

    def draw(self):
        
        self.screen.fill('black')
        self.camera_surf.fill('black')
        
        for b in self.blocks:
            self.camera_surf.blit(b.image, (b.rect.x, b.rect.y))
            
        self.camera_surf.blit(self.player.image, (self.player.rect.x, self.player.rect.y))
        self.screen.blit(self.camera_surf,(-self.camera_x+self.screen_w/2, -self.camera_y+self.screen_h/2))
    
    def __init__(self):
        pg.init()
        (self.screen_w, self.screen_h) = (640,480)
        
        self.camera_surf = pg.Surface((self.screen_w*10, self.screen_h*10))
        (self.camera_x, self.camera_y) = (0,0)
        
        self.screen=pg.display.set_mode((self.screen_w,self.screen_h))

        self.clock=pg.time.Clock()

        self.blocks = []

        self.level = """
        
        
        
                        #
                #    *   ##
                #       ###
                ###########
        """ 
        
        self.create_world()

    
