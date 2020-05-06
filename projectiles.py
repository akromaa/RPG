import pygame

class Projectiles(pygame.sprite.Sprite):

    def __init__(self, x, y, direction_tir, vitesse):
        super().__init__()

        self.direction_tir = direction_tir
        self.velocity = 5
        self.image = pygame.image.load("images/flamme.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
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


    def explosionUpdate(deltaTime):
        self.explosionTimeCounter += deltaTime
        self.explosionStep = self.explosionTimeCounter / 100
