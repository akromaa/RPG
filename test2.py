import pygame


SIZE = WIDTH, HEIGHT = 600, 400 #the width and height of our screen
BACKGROUND_COLOR = pygame.Color('white') #The background colod of our window
FPS = 10 #Frames per second

class MySprite(pygame.sprite.Sprite):
    def __init__(self):
        super(MySprite, self).__init__()
      

        self.images = []
        self.images.append(pygame.image.load('Perso1.png'))
        self.images.append(pygame.image.load('Perso2.png'))
        self.images.append(pygame.image.load('Perso3.png'))
        self.images.append(pygame.image.load('Perso4.png'))
        self.images.append(pygame.image.load('Perso5.png'))
        self.images.append(pygame.image.load('Perso6.png'))
        self.images.append(pygame.image.load('Perso7.png'))
        self.images.append(pygame.image.load('Perso8.png'))
        self.images.append(pygame.image.load('Perso9.png'))
        self.images.append(pygame.image.load('Perso10.png'))
        
        self.image1 = pygame.image.load("Perso1.png")
        self.image1_rect=self.image1.get_rect() 
        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(0, 0, 33, 82)

    def update(self):
        self.index += 1        
        self.rect.x += 5
        self.rect.y += 5

        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]


background = pygame.image.load("map_debut.png")

def main():
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    my_sprite = MySprite()
    my_group = pygame.sprite.Group(my_sprite)
    clock = pygame.time.Clock()

    while True:
        screen.blit(background, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        print(my_sprite.image1.get_rect())
        my_group.update()
        screen.blit(my_sprite.image, my_sprite.rect )#modifier mys_sprite.rect pour le coller sur le rect de mon perso.
        #my_group.draw(screen)
        pygame.display.update()
        clock.tick(10)

if __name__ == '__main__':
    main()