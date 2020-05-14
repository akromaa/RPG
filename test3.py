import pygame


SIZE = WIDTH, HEIGHT = 600, 400 #the width and height of our screen
BACKGROUND_COLOR = pygame.Color('white') #The background colod of our window
FPS = 10 #Frames per second

class MySprite(pygame.sprite.Sprite):
    def __init__(self):
        super(MySprite, self).__init__()
      

        self.images = []
        self.image1 = pygame.image.load("sprite/personnage.png")
        

        self.images.append(self.image1.subsurface(pygame.Rect(2 % 10 * 32, 2 // 10 * 64, 32, 64)))
        self.images.append(self.image1.subsurface(pygame.Rect(3 % 10 * 32, 3 // 10 * 64, 32, 64)))
        self.images.append(self.image1.subsurface(pygame.Rect(4 % 10 * 32, 4 // 10 * 64, 32, 64)))
        self.images.append(self.image1.subsurface(pygame.Rect(5 % 10 * 32, 5 // 10 * 64, 32, 64)))
        self.images.append(self.image1.subsurface(pygame.Rect(6 % 10 * 32, 6 // 10 * 64, 32, 64)))
        self.images.append(self.image1.subsurface(pygame.Rect(7 % 10 * 32, 7 // 10 * 64, 32, 64)))
        self.images.append(self.image1.subsurface(pygame.Rect(8 % 10 * 32, 8 // 10 * 64, 32, 64)))
        self.images.append(self.image1.subsurface(pygame.Rect(9 % 10 * 32, 9 // 10 * 64, 32, 64)))
        self.images.append(self.image1.subsurface(pygame.Rect(10 % 10 * 32, 10 // 10 * 64, 32, 64)))
        self.images.append(self.image1.subsurface(pygame.Rect(11 % 10 * 32, 11 // 10 * 64, 32, 64)))
        self.images.append(self.image1.subsurface(pygame.Rect(12 % 10 * 32, 12 // 10 * 64, 32, 64)))
        self.rect = pygame.Rect(0, 0, 32, 64)

        
        
        
        self.image1_rect=self.image1.get_rect() 
        self.index = 0
        self.image = self.images[self.index]

        

    def update(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]




def main():
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    my_sprite = MySprite()
    my_group = pygame.sprite.Group(my_sprite)
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        print(my_sprite.image.get_rect())
        my_group.update()
        screen.fill(BACKGROUND_COLOR)
        my_group.draw(screen)
        pygame.display.update()
        clock.tick(10)

if __name__ == '__main__':
    main()