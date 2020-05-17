import pygame
import random
from dialogue import *
from projectiles import Projectiles, Cercle_feu_glace, Flamme



class Player(pygame.sprite.Sprite):


    def __init__(self, game, image_player, pos_player, view):
        super().__init__()

        self.image1 = pygame.sprite.Sprite()
        self.image1.image = pygame.image.load(image_player).convert_alpha()
        # self.image1.image = pygame.transform.scale(self.image1.image, (50, 50)) # à voir car change le découpage
        self.image1.rect = self.image1.image.get_rect()
        self.direction = view
        self.game = game
        self.velocity = 8
        self.index_img = 0
        self.frame = dict([(direction, [self.image1.image.subsurface(x, y, 64, 64) for x in range(0, 576, 64)])
        for direction, y in zip((pygame.K_UP, pygame.K_LEFT, pygame.K_DOWN, pygame.K_RIGHT), range(0, 256, 64))])
        self.vector = [3, 3]
        self.rect = self.frame[self.direction][self.index_img].get_rect()
        self.pos_player = self.rect.x, self.rect.y = pos_player
        print(self.rect.x, self.rect.y)
        self.all_projectile = pygame.sprite.Group()
        self.all_spell = pygame.sprite.Group()
        self.direction_tir = "down"
        self.vitesse = 5


    def move_bird(self):
        self.fps = pygame.time.Clock()
        self.size = (500, 500)
        self.fps.tick(8)
        self.index_img = (self.index_img + 1) % 3
        self.rect.x += self.vector[0]
        self.rect.y += self.vector[1]
        # On vérifie s'il y a collision avec le bord de l'écran
        # si oui on inverse les valeurs
        if self.rect.right >= self.size[0]:
            self.direction = pygame.K_LEFT
            self.vector[0] = -self.vector[0]
        elif self.rect.left <= 0:
            self.vector[0] = -self.vector[0]
            self.direction = pygame.K_RIGHT
        elif self.rect.bottom >= self.size[1]:
            self.direction = pygame.K_LEFT
            self.vector[1] = -self.vector[1]
        elif self.rect.top <= 0:
            self.direction = pygame.K_RIGHT
            self.vector[1] = -self.vector[1]

    def move_right(self):
        self.rect.x += self.velocity
        self.direction = pygame.K_RIGHT
        self.index_img = (self.index_img + 1) % 9
        if pygame.sprite.collide_mask(self.game.hero, self.game.squellette):
            self.rect.x -= self.velocity

        # self.rect.x, self.rect.y = 100, 100


    def move_left(self):
        self.rect.x -= self.velocity
        self.direction = pygame.K_LEFT
        self.index_img = (self.index_img + 1) % 9
        if pygame.sprite.collide_mask(self.game.hero, self.game.squellette):
            self.rect.x += self.velocity


    def move_up(self):
        self.rect.y -= self.velocity
        self.direction = pygame.K_UP
        self.index_img = (self.index_img + 1) % 9
        if pygame.sprite.collide_mask(self.game.hero, self.game.squellette):
            self.rect.y += self.velocity
            self.game.dialogue()


    def move_down(self):
        self.rect.y += self.velocity
        self.direction = pygame.K_DOWN
        self.index_img = (self.index_img + 1) % 9
        if pygame.sprite.collide_mask(self.game.hero, self.game.squellette):
            self.rect.y -= self.velocity

    @property
    def mask(self):
        return pygame.mask.from_surface(self.frame[self.direction][self.index_img])

    def launch_projectile(self, nb):
        self.nb = nb
        if self.nb == 1:
            self.all_projectile.add(Projectiles(self, self.rect.x, self.rect.y, self.direction_tir, 1))
        elif self.nb == 2:
            self.all_projectile.add(Cercle_feu_glace(self, self.rect.x, self.rect.y, self.direction_tir, 10))


    def launch_spell(self, spell):
        self.spell = spell
        if self.spell == 1:
            self.all_spell.add(Flamme(self, self.rect.x, self.rect.y, self.direction_tir, 100))
            print(self.direction_tir)


















