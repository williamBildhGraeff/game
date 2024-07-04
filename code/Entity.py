from abc import ABC

import pygame
from pygame import Surface


class Entity(ABC):
    def __init__(self, name: str, position: tuple, path: str):
        self.name = name
        self.surf: Surface = pygame.image.load(f'./asset/{path}/' + name + '.png').convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0

    def move(self):
        pass
