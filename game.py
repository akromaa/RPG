# coding:utf-8
import pygame
from Player import *


class Game():
    def __init__(self):
        self.pressed = {}
        # creation des personnages : image, positionnement, position de départ
        self.hero = Player(self, "images/perso_nu.png", (750, 600), pygame.K_DOWN)
