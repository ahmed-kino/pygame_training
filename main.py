#!/usr/bin/python

import sys
import pygame as pg
from pygame.locals import *

from settings import *
from sprites import *
import random

class Game:

    def __init__(self):
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode(SIZE)
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
    
    def new(self):
        # load the spritesheet
        self.spritesheet = Spritesheet('images/spritesheet_jumper.png')
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        for plat in PLATFORM_LIST:
            p =  Platform(self, *plat)
            self.all_sprites.add(p)
            self.platforms.add(p)
        self.player = Player(self)
        self.all_sprites.add(self.player)
        self.run()

    
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    
    def update(self):
        self.all_sprites.update()

        # check if the player hits the platform when falling
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = 0

        if self.player.rect.top <= HEIGHT / 4:
            self.player.pos.y += max(abs(self.player.vel.y), 2)
            for plat in self.platforms:
                plat.rect.y += max(abs(self.player.vel.y), 2)
                if plat.rect.top >=HEIGHT:
                    plat.kill()
        if self.player.rect.y > HEIGHT:
            self.playing = False

        while len(self.platforms) < 6:
            width = random.randrange(50, 100)
            p = Platform(self, random.randrange(0, WIDTH - width),
                         random.randrange(-75, -30))
            self.platforms.add(p)
            self.all_sprites.add(p)


    def events(self):
        for event in pg.event.get():
            if event.type == QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()



    def draw(self):
        self.screen.fill(CHAIN)
        self.all_sprites.draw(self.screen)
        pg.display.flip()


    def show_start_screen(self):
        pass

    def show_game_over_screen(self):
        pass



g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_game_over_screen()

pg.quit()