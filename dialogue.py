

import pygame

blue_color = (0, 0, 255)
texte1= "salut je m'appel akroma"

arial_font = pygame.font.Font("images/DUNGRG__.TTF", 100)
hello_texte_surface = arial_font.render(texte1, True, blue_color)  # texte, affiner le texte, couleur du texte
