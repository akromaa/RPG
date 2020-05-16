import pygame
from Player import *

class Projectiles(pygame.sprite.Sprite):

    def __init__(self,player, x, y, direction_tir, vitesse):
        super().__init__()

        self.player = player
        self.direction_tir = direction_tir
        self.velocity = 5
        self.images = []
        self.images.append(pygame.image.load('images/feu_glace1.png'))
        self.images.append(pygame.image.load('images/feu_glace2.png'))
        self.images.append(pygame.image.load('images/feu_glace3.png'))
        self.images.append(pygame.image.load('images/feu_glace4.png'))
        self.images.append(pygame.image.load('images/feu_glace5.png'))
        self.images.append(pygame.image.load('images/feu_glace6.png'))
        self.images.append(pygame.image.load('images/feu_glace7.png'))
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x - 80
        self.rect.y = y - 50
        self.vitesse = vitesse



    def mouvement(self):
        if self.direction_tir == "right":
            self.rect.x += self.vitesse
        elif self.direction_tir == "left" :
            self.rect.x -= self.vitesse
        elif self.direction_tir == "up":
            self.rect.y -= self.vitesse
        elif self.direction_tir == "down":
            self.rect.y += self.vitesse
        if self.rect.x <0 or self.rect.x > 1200: # x de la taille de l'ecran
            self.remove()
        elif self.rect.y <0 or self.rect.y > 1000: # y de la taille de l'ecran
            self.remove()
        if self.player.game.check_collision(self.player.game.squellette, self.player.all_projectile): # si collision remove du projectile
            self.remove()

    def update(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]

    def update_spell(self):
        self.index += 1
        if self.index == len(self.images):
            self.remove()
        self.image = self.images[self.index]


        #if self.rect.right and self.rect.left > 500:
            #print ("kiki")


    def remove(self):
        self.player.all_projectile.remove(self)
        self.player.all_spell.remove(self)



class Cercle_feu_glace(Projectiles,pygame.sprite.Sprite):

    def __init__(self,player, x, y, direction_tir, vitesse):
        super().__init__(player, x, y, direction_tir, vitesse)


        self.direction_tir = direction_tir
        self.velocity = 5
        self.images = []
        self.images.append(pygame.image.load('images/feu_glace1.png'))
        self.images.append(pygame.image.load('images/feu_glace2.png'))
        self.images.append(pygame.image.load('images/feu_glace3.png'))
        self.images.append(pygame.image.load('images/feu_glace4.png'))
        self.images.append(pygame.image.load('images/feu_glace5.png'))
        self.images.append(pygame.image.load('images/feu_glace6.png'))
        self.images.append(pygame.image.load('images/feu_glace7.png'))
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x - 80
        self.rect.y = y - 50
        self.vitesse = vitesse

class Flamme(Projectiles,pygame.sprite.Sprite):

    def __init__(self,player, x, y, direction_tir, vitesse):
        super().__init__(player, x, y, direction_tir, vitesse)
        print(direction_tir)

        self.direction_tir = direction_tir
        self.velocity = 5
        self.images = []
        #self.images = pygame.transform.scale(self.images, (50, 50))# pas dans une liste

        self.image1 = pygame.image.load("images/feux.png")
        self.spell = 0
        print(self.spell)

        self.images.append(self.image1.subsurface(pygame.Rect(0 % 5 * 64, 0 // 5 * 64, 64, 64)))
        self.images.append(self.image1.subsurface(pygame.Rect(1 % 5 * 64, 1 // 5 * 64, 64, 64)))
        self.images.append(self.image1.subsurface(pygame.Rect(2 % 5 * 64, 2 // 5 * 64, 64, 64)))

        self.rect = pygame.Rect(0, 0, 64, 64)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vitesse = vitesse




