import pygame

class DrawableObject:
    def __init__(self, color, rect):
        self.color = color
        self.rect = rect

class Drawer:
    def __init__(self, screen):
        self.screen = screen

    def draw(self, obj):
        pygame.draw.rect(self.screen, obj.color, obj.rect)
