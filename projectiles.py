import pygame

class Projectiles(pygame.sprite.Sprite):

    def __init__(self, x, y, direction_tir, vitesse):
        super().__init__()

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

    def update(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        if self.rect.right and self.rect.left > 500:
            print ("kiki")


