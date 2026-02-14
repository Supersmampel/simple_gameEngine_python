from objects.drawer import DrawableRect

class Logic:
    def __init__(self):
        self.rect_list = []
        self.color = (255, 0, 0)

    def update(self):
        self.generate_grid(10, 10)
        return {"rects": self.rect_list}
    
    def generate_grid(self, width, height, size=64):
        for x in range(width):
            for y in range(height):
                self.rect_list.append(DrawableRect(self.color, (x*size, y*size, size, size)))
                self.color = (self.color[0], (self.color[1]+10)%256, self.color[2])
            
                