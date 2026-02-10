import pygame

class drawer:
    def clearScreen(self, color):
        self.screen.fill(color)
    
    def draw(self):
        pygame.display.flip()

    def __init__(self, screen):
        self.screen = screen
    
    def drawRect(self, color, cords, width, height):
        pygame.draw.rect(self.screen, color, (cords[0], cords[1], width, height))

    def drawCircle(self, color, cords, radius):
        pygame.draw.circle(self.screen, color, (cords[0], cords[1]), radius)