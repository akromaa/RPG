import sys, math, random, pygame

# PARAMETRES DU JEU
WIDTH = 640
HEIGHT = 480
FPS = 60
TITLE = "Mon jeu"

# INITIALISATION DU JEU
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
rectScreen = screen.get_rect()
fond = pygame.image.load("images/map_debut.png")


class Personnage(pygame.sprite.Sprite):
    spriteSheet = pygame.image.load("images/advnt_full.png").convert_alpha()

    sequences = [(0, 1, False), (1, 6, True), (7, 3, False)]

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = Personnage.spriteSheet.subsurface(pygame.Rect(0, 0, 32, 64))
        self.rect = pygame.Rect(0, 0, 32, 64)
        self.rect.bottom = HEIGHT

        self.numeroSequence = 0
        self.numeroImage = 0
        self.flip = False

        self.deltaTime = 0
        self.vitesse = int(round(100 / FPS))

    def update(self, time):
        self.deltaTime = self.deltaTime + time

        if self.deltaTime >= 150:
            self.deltaTime = 0

            n = Personnage.sequences[self.numeroSequence][0] + self.numeroImage
            self.image = Personnage.spriteSheet.subsurface(pygame.Rect(n % 10 * 32, n // 10 * 64, 32, 64))
            if self.flip:
                self.image = pygame.transform.flip(self.image, True, False)

            self.numeroImage = self.numeroImage + 1

            if self.numeroImage == Personnage.sequences[self.numeroSequence][1]:
                if Personnage.sequences[self.numeroSequence][2]:
                    self.numeroImage = 0
                else:
                    self.numeroImage = self.numeroImage - 1

    def setSequence(self, n):
        if self.numeroSequence != n:
            self.numeroImage = 0
            self.numeroSequence = n

    def goRight(self):
        self.rect = self.rect.move(self.vitesse, 0).clamp(rectScreen)
        self.flip = False
        self.setSequence(1)

    def goLeft(self):
        self.rect = self.rect.move(-self.vitesse, 0).clamp(rectScreen)
        self.flip = True
        self.setSequence(1)

# ... A COMPLETER AVEC LE CODE DE VOS INITIALISATIONS ...
perso = Personnage()
# BOUCLE DE JEU
clock = pygame.time.Clock()
while True:
    time = clock.tick(FPS)


    # GESTION DES EVENEMENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            perso.goRight()
        elif keys[pygame.K_LEFT]:
            perso.goLeft()
        elif keys[pygame.K_SPACE]:
            perso.setSequence(2)
        else:
            perso.setSequence(0)

        perso.update(time)

        screen.fill(pygame.Color("white"))
        screen.blit(perso.image, perso.rect)

    # ... A COMPLETER AVEC LE CODE DE VOTRE JEU ...

    # MAJ DE L'AFFICHAGE
    pygame.display.update()