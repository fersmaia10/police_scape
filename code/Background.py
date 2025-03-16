from code.Const import WIN_WIDTH
from code.Entity import Entity

class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        self.rect.centery -= 1
        if self.rect.left <= 0:
            self.rect.right = WIN_WIDTH