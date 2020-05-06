#coding:utf-8


import pygame
from Player import *
from game import *
from projectiles import Projectiles

pygame.init()
window_resolution = (1200, 1000)

pygame.display.set_caption("VIDOC")  # titre de la fenetre
window_surface = pygame.display.set_mode(window_resolution, pygame.RESIZABLE)

image_village1 = pygame.image.load("images/map_debut.png").convert()



game = Game()
chat = pygame.image.load("cat.png").convert_alpha()
rectChat = chat.get_rect()




fps = pygame.time.Clock()
launched = True
while launched:
    fps.tick(60)
    for projectile in game.hero.all_projectile:
        projectile.mouvement()



    window_surface.blit(image_village1, (0, 0))
    index_img = 0
    game.hero.all_projectile.draw(window_surface)

    #blue_bird.move_bird()
    #window_surface.blit(blue_bird.frame[blue_bird.direction][blue_bird.index_img], (blue_bird.rect.x, blue_bird.rect.y))

    if game.pressed.get(pygame.K_RIGHT):  # si touche droite pressé alors Game-> Perso bouge
        game.hero.move_right()
        game.hero.direction_tir = "right"
    elif game.pressed.get(pygame.K_LEFT):
        game.hero.move_left()
        game.hero.direction_tir = "left"
    elif game.pressed.get(pygame.K_UP):
        game.hero.move_up()
        game.hero.direction_tir = "up"
    elif game.pressed.get(pygame.K_DOWN):
        game.hero.move_down()
        game.hero.direction_tir = "down"

    window_surface.blit(game.hero.frame[game.hero.direction][game.hero.index_img], (game.hero.rect.x, game.hero.rect.y))
    game.hero.frame.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            if event.key == pygame.K_SPACE:
                game.hero.launch_projectile()
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                launched = False

    pygame.time.wait(60)
    pygame.display.flip()


