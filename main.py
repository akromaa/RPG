# coding:utf-8

import pygame
from Player import Player
from game import *
from dialogue import *
from projectiles import Projectiles

# initilisation de la fenetre:
pygame.init()
window_resolution = (1200, 1000)
window_surface = pygame.display.set_mode(window_resolution)
blue_color = (0, 0, 255)

# titre du jeu
pygame.display.set_caption("VIDOC")  # titre de la fenetre

# importation des images de fond :
image_village1 = pygame.image.load("images/map_debut.png").convert()
image_village1 = pygame.transform.scale(image_village1, (window_resolution)) # callage de l'image du fond sur la résolution de l'ecran(window_resolution)

arial_font = pygame.font.Font("images/DUNGRG__.TTF", 100)
hello_texte_surface = arial_font.render("hello world", True, blue_color)  # texte, affiner le texte, couleur du texte

# creation des objets :
game = Game()




# délimitation de la vitesse du jeu
fps = pygame.time.Clock()


launched = True
while launched:
    fps.tick(60)

    # recuperation des projectiles
    for projectile in game.hero.all_projectile:
        projectile.mouvement()
        projectile.update()

    for projectile in game.hero.all_spell:
        projectile.update_spell()




    # application de l'imga de fond
    window_surface.blit(image_village1, (0, 0))
    window_surface.blit(hello_texte_surface, [10, 10])



    game.hero.all_projectile.draw(window_surface)
    game.hero.all_spell.draw(window_surface)


    # blue_bird.move_bird()
    # window_surface.blit(blue_bird.frame[blue_bird.direction][blue_bird.index_img], (blue_bird.rect.x, blue_bird.rect.y))

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
    window_surface.blit(game.squellette.frame[game.squellette.direction][game.squellette.index_img], (game.squellette.rect.x, game.squellette.rect.y))

    game.hero.frame.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            if event.key == pygame.K_SPACE:
                game.hero.launch_projectile(1)
            elif event.key == pygame.K_1:
                game.hero.launch_projectile(2)
            elif event.key == pygame.K_2:
                game.hero.launch_spell(1)
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                launched = False




    pygame.time.wait(60)
    pygame.display.flip()
