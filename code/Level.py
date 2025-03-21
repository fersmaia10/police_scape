import pygame
from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('level1BG'))

    def run(self):
        while True:
            for ent in self.entity_list:
                self.window.blit(ent.surf, ent.rect)
                ent.move()
            pygame.display.flip()
        pass
