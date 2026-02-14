"""
description: Main game loop and initialization.
author: Samuel Franken
date created: 14-02-2026
"""

from objects.drawer import Drawer
import pygame
import objects.logic as logic
#rimport objects.init as init

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((480*2.8, 360*2.8))
        self.drawer = Drawer(self.screen)
        self.background_color = (0, 0, 0)
        self.logic = logic.Logic(self.screen)
        self.running = False

    def run(self):
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.drawer.clear(self.background_color)
            self.objects = self.logic.update()
            self.drawer.draw(self.objects)
            self.drawer.flip()





if __name__ == "__main__":
    game = Game() 
    game.run()