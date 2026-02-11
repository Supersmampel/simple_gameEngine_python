import objects.drawer as draw
import pygame
import objects.logic as logic
import objects.init as init

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((480*2.5, 360*2.5))
        self.drawer_functions = draw
        self.drawer = draw.Drawer(self.screen)

    def run(self):
        running = True
        self.logic = logic.Logic(self.drawer_functions)
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            self.logic.update()




if __name__ == "__main__":
    game = Game()
    game.run()
    pygame.quit()