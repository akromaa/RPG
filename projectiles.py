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
        if self.rect.x <0 or self.rect.x > 1200:
            print("kiki")

    def update(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        #if self.rect.right and self.rect.left > 500:
            #print ("kiki")



class Cercle_feu_glace(Projectiles,pygame.sprite.Sprite):

    def __init__(self, x, y, direction_tir, vitesse):
        super().__init__( x, y, direction_tir, vitesse)


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

    def __init__(self, x, y, direction_tir, vitesse):
        super().__init__(x, y, direction_tir, vitesse)
        print(direction_tir)

        self.direction_tir = direction_tir
        self.velocity = 5
        self.images = []
        self.images.append(pygame.image.load('images/FlammeHaut.png'))
        self.images.append(pygame.image.load('images/FlammeBas.png'))
        self.images.append(pygame.image.load('images/FlammeDroite.png'))
        self.images.append(pygame.image.load('images/FlammeGauche.png'))
        #self.images = pygame.transform.scale(self.images, (50, 50))# pas dans une liste
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vitesse = vitesse




