from objects.drawer import Drawer
import pygame
import objects.logic as logic
import objects.init as init

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((480*2.5, 360*2.5))
        self.drawer = Drawer(self.screen)
        self.background_color = (0, 0, 0)

    def run(self):
        self.running = True
        self.logic = logic.Logic()
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
    pygame.quit()