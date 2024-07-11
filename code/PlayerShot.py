from code.Const import ENTITY_SPEED
from code.Entity import Entity


class PlayerShot(Entity):
    def __init__(self, name: str, position: tuple, path: str):
        super().__init__(name, position, path)

    def move(self):
        self.rect.centerx += ENTITY_SPEED[self.name]
        pass
