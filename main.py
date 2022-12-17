#!/usr/bin/python

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
        # Change background colour
        self.colour_r = 0
        self.colour_b = 0
        self.colour_g = 0
        self.last_update = 0
        self.current_background_colour = 0
    
    def load_data(self):
        self.score = 0
        # load the spritesheet
        self.spritesheet = Spritesheet('images/spritesheet_jumper.png')
        self.jump_sound = pg.mixer.Sound('sounds/jump.wav')

    def new(self):
        # load data
        self.load_data()

        self.colour = SKY_COLOUR_RANGE[0]
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
                if plat.rect.top >= HEIGHT + 200:
                    plat.kill()
                    self.score += 1
        # Extra logic for moving to the right 
        if self.player.rect.right >= WIDTH * 0.75:
            self.player.pos.x += -max(abs(self.player.vel.x), 2)
            for plat in self.platforms:
                plat.rect.x += -max(abs(self.player.vel.x), 2)
        if self.player.rect.left <= WIDTH / 4:
            self.player.pos.x += max(abs(self.player.vel.x), 2)
            for plat in self.platforms:
                plat.rect.x += max(abs(self.player.vel.x), 2)

        # When the player dies
        if self.player.rect.bottom > HEIGHT:
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


    def change_colour(self, colour):
        self.colour_r, self.colour_g, self.colour_b = self.colour       
        if self.colour_r < colour[0]:
            self.colour_r += 1
        if self.colour_b < colour[1]:
            self.colour_b += 1
        if self.colour_g < colour[2]:
            self.colour_g += 1
        if self.colour_r > colour[0]:
            self.colour_r -= 1
        if self.colour_b > colour[1]:
            self.colour_b -= 1
        if self.colour_g > colour[2]:
            self.colour_g -= 1
        self.colour = (self.colour_r, self.colour_g, self.colour_b)
        return self.colour


    def moving_up(self):
        if self.score > 10 and self.score < 50:
            self.screen.fill(self.change_colour(SKY_COLOUR_RANGE[1]))
        if self.score > 50 and self.score < 100:
            self.screen.fill(self.change_colour(SKY_COLOUR_RANGE[2]))
        if self.score > 100 and self.score < 150:
            self.screen.fill(self.change_colour(SKY_COLOUR_RANGE[3]))
        if self.score > 150 and self.score < 200:
            self.screen.fill(self.change_colour(SKY_COLOUR_RANGE[4]))
        if self.score > 200 and self.score < 250:
            self.screen.fill(self.change_colour(SKY_COLOUR_RANGE[5]))
        if self.score > 250 and self.score < 300:
            self.screen.fill(self.change_colour(SKY_COLOUR_RANGE[6]))
        if self.score > 350 and self.score < 400:
            self.screen.fill(self.change_colour(SKY_COLOUR_RANGE[7]))
        if self.score > 400 and self.score < 450:
            self.screen.fill(self.change_colour(SKY_COLOUR_RANGE[8]))
        if self.score > 450 and self.score < 500:
            self.screen.fill(self.change_colour(SKY_COLOUR_RANGE[9]))
        if self.score > 500 and self.score < 550:
            self.screen.fill(self.change_colour(SKY_COLOUR_RANGE[10]))
        if self.score > 550 and self.score < 600:
            self.screen.fill(self.change_colour(SKY_COLOUR_RANGE[11]))
        if self.score > 600 and self.score < 650:
            self.screen.fill(self.change_colour(SKY_COLOUR_RANGE[12]))
        if self.score > 650 and self.score < 700:
            self.screen.fill(self.change_colour(SKY_COLOUR_RANGE[13]))
        if self.score > 700 and self.score < 750:
            self.screen.fill(self.change_colour(SKY_COLOUR_RANGE[14]))
        if self.score > 750 and self.score < 800:
            self.screen.fill(self.change_colour(SKY_COLOUR_RANGE[15]))
        if self.score > 800 and self.score < 850:
            self.screen.fill(self.change_colour(SKY_COLOUR_RANGE[16]))
        if self.score > 850 and self.score < 900:
            self.screen.fill(self.change_colour(SKY_COLOUR_RANGE[17]))
        if self.score > 900 and self.score < 950:
            self.screen.fill(self.change_colour(SKY_COLOUR_RANGE[17]))
        if self.score > 950 and self.score < 1000:
            self.screen.fill(self.change_colour(SKY_COLOUR_RANGE[17]))
        if self.score > 1000 and self.score < 1050:
            self.screen.fill(self.change_colour(SKY_COLOUR_RANGE[18]))
        if self.score > 1050 and self.score < 1100:
            self.screen.fill(self.change_colour(SKY_COLOUR_RANGE[19]))

    def draw(self):
        print(self.score)
        self.screen.fill(self.change_colour(self.colour))
        self.moving_up()            
                                
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