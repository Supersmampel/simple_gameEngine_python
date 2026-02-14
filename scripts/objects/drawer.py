import pygame


class Drawer:
    def __init__(self, screen):
        self.screen = screen

    def draw(self, obj):
        for rect in obj["rects"]:
            pygame.draw.rect(self.screen, rect.color, rect.rect)

    def clear(self, color=(0, 0, 0)):
        self.screen.fill(color)
    
    def flip(self):
        pygame.display.flip()


class DrawableRect(Drawer):
    def __init__(self, color, rect):
        #super().__init__(screen)
        self.color = color
        self.rect = rect