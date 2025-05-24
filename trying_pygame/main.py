import pygame as pg

import system

game = system.System()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            break
        
    game.update()
    game.draw()

    pg.display.update()
    game.clock.tick(60)