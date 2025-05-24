import pygame as pg

class Entity:

    # if no image just set image_name to None
    def __init__(self, x,y,w,h, image_name, img_w,img_h):
        if image_name != None:
            self.image=pg.image.load(image_name).convert()
            self.image=pg.transform.scale(self.image, (img_w,img_h))
            

        self.has_image = False

        self.rect=pg.Rect(0,0,0,0)
        self.rect.x=x
        self.rect.y=y
        self.rect.w=w
        self.rect.h=h
        

        