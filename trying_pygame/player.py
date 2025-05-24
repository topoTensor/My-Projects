import pygame as pg
import entity

class Player(entity.Entity):
    
    def __init__(self, x, y, w, h, image_name, img_w, img_h):
        super().__init__(x, y, w, h, image_name, img_w, img_h)
        
        self.jump_str = 25
        self.can_jump = False
        
        self.speed_x=10
        
        self.vel_y=0
        
        self.gravity = 2
        self.max_falling_speed = 10
        
    def move(self,blocks):
        dx =0
        dy =0
        
        key=pg.key.get_pressed()
        if key[pg.K_w] and self.can_jump:
            self.vel_y -= self.jump_str
            self.can_jump = False

        if key[pg.K_a]:
            dx -= self.speed_x
        elif key[pg.K_d]:
            dx += self.speed_x
            
        self.vel_y += self.gravity
        if self.vel_y > self.max_falling_speed:
            self.vel_y = self.max_falling_speed
        dy += self.vel_y
        
        for b in blocks:
            if b.rect.colliderect(self.rect.x + dx, self.rect.y, self.rect.w, self.rect.h):
                dx = 0
    
            if b.rect.colliderect(self.rect.x, self.rect.y + dy, self.rect.w, self.rect.h):
                if self.vel_y < 0:
                    dy = b.rect.bottom-self.rect.top
                    self.vel_y =0
                else:
                    dy = b.rect.top-self.rect.bottom
                    self.vel_y =0
                    self.can_jump = True

        self.rect.x += dx
        self.rect.y += dy