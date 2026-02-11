

class Logic:
    def __init__(self, drawer):
        self.drawer = drawer

    def update(self):
        self.drawer.clear()
        obj_list = [self.drawer.DrawableRect((255, 0, 0), (50, 50, 100, 100))]
        for obj in obj_list:
            self.drawer.draw(obj)
        self.drawer.flip()