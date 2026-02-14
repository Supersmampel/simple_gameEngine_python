import pygame
from objects.drawer import DrawableRect
import random

class Logic:
    def __init__(self, screen):
        self.screen = screen
        self.rect_list = []
        self.colors = {
            "rock": (128, 128, 128),
            "grass": (0, 255, 0),
            "water": (0, 0, 255),
            "tree": (34, 139, 34)
        }
        self.generate_grid(100, 100, 64)
        self.key_state = {}

    def update(self):
        self.input_handler()
        return {"rects": self.rect_list}
    
    def input_handler(self):
        self.keys = pygame.key.get_pressed()
        if self.key_down(pygame.K_r):
            self.generate_grid(100, 100, 64)

    
    def key_down(self, key):
        if self.keys[key] and not self.key_state[key]:
            self.generate_grid(100, 100, 64)
            self.key_state.setdefault(key, True)
            return True
        else:
            self.key_state.setdefault(key, False)
            return False

    
    def add_tile(self, color:object, rect):
        if len(color) == 1:
            self.rect_list.append(DrawableRect(color[0][1], rect))
        else:
            self.random = random.randint(0, color[0][0] + color[1][0] + color[2][0] - 1)
            for key in color:
                if self.random < color[key][0]:
                    break
                self.random -= color[key][0]
            self.rect_list.append(DrawableRect(color[key][1], rect))
    
    def generate_grid(self, width, height, size=64):
        self.rect_list = []
        self.seed = random.randint(0, 1000000)
        random.seed(self.seed)
        self.draw_state = random.getstate()
        self.color = (255, 0, 0)
        for i in range(width):
            self.add_tile({0: [1, self.colors["rock"]]}, (i*size, 0, size, size))
        
        for i in range(height - 2):
            self.add_tile({0: [1, self.colors["rock"]]}, (0, (i+1)*size, size, size))
            for j in range(width - 2):
                self.add_tile(
                    {
                        0: [90, self.colors["grass"]],
                        1: [2, self.colors["water"]],
                        2: [8, self.colors["tree"]]
                    },

                     ((j+1)*size,(i+1)*size, size, size)
                )
            self.add_tile({0: [1, self.colors["rock"]]}, ((width-1)*size, (i+1)*size, size, size))
        
        for i in range(width):
            self.add_tile({0: [1, self.colors["rock"]]}, (i*size, (height-1)*size, size, size))