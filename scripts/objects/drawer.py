import pygame


class Drawer:
    def __init__(self, screen):
        self.screen = screen

    def draw(self, obj):
        pygame.draw.rect(self.screen, obj.color, obj.rect)

    def clear(self, color=(0, 0, 0)):
        self.screen.fill(color)
    
    def flip(self):
        pygame.display.flip()


class DrawableRect(Drawer):
    def __init__(self, color, rect):
        #super().__init__(screen)
        self.color = color
        self.rect = rect