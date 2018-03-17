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
    
    def load_data(self):
        self.jump_sound = pg.mixer.Sound('sounds/jump.wav')

    def new(self):
        # load data
        self.load_data()
        # load the spritesheet
        self.spritesheet = Spritesheet('images/spritesheet_jumper.png')
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        for plat in PLATFORM_LIST:
            Platform(self, *plat)
        self.player = Player(self)
        pg.mixer.music.load('sounds/happy.ogg')
        self.run()

    
    def run(self):
        # Game loop
        pg.mixer.music.play(loops=-1)
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
                lowest = hits[0]
                for hit in hits:
                    if hit.rect.bottom > lowest.rect.bottom:
                        lowest = hit
                if self.player.pos.x < lowest.rect.right + 10 and \
                   self.player.pos.x > lowest.rect.left - 10:
                    if self.player.pos.y < lowest.rect.centery:
                        self.player.pos.y = lowest.rect.top
                        self.player.vel.y = 0
                        self.player.jumping = False

        if self.player.rect.top <= HEIGHT / 4:
            self.player.pos.y += max(abs(self.player.vel.y), 2)
            for plat in self.platforms:
                plat.rect.y += max(abs(self.player.vel.y), 2)
                if plat.rect.top >= HEIGHT + 100:
                    plat.kill()
        # Extra logic for moving to the right 
        if self.player.rect.right >= WIDTH * 0.75:
            self.player.pos.x += -max(abs(self.player.vel.x), 2)
            for plat in self.platforms:
                plat.rect.x += -max(abs(self.player.vel.x), 2)
        if self.player.rect.left <= WIDTH / 4:
            self.player.pos.x += max(abs(self.player.vel.x), 2)
            for plat in self.platforms:
                plat.rect.x += max(abs(self.player.vel.x), 2)

        # When the player goes 100 px down 
        if self.player.rect.y > HEIGHT - 200:
            self.player.rect.y += -max(abs(self.player.vel.y), 2) - 5
            for plat in self.platforms:
                plat.rect.y += -max(abs(self.player.vel.y), 2) - 5
        # When the player dies
        if self.player.rect.y > HEIGHT + 100:
            self.playing = False

        # Generate new platforms
        while len(self.platforms) < 10:
            Platform(self,
                     random.randrange(-100, WIDTH + 100),
                     random.randrange(-75, -30))


    def events(self):
        for event in pg.event.get():
            if event.type == QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()
            if event.type == pg.KEYUP:
                if event.key == pg.K_SPACE:
                    self.player.jump_cut()



    def draw(self):
        self.screen.fill(CHAIN)
        self.all_sprites.draw(self.screen)
        self.screen.blit(self.player.image, self.player.rect)
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