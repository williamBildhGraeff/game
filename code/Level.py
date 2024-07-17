import random
import sys

import pygame.display
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import COLOR_GREEN, MENU_OPTION, EVENT_ENEMY, WIN_HEIGHT, EVENT_TIMEOUT
from code.Enemy import Enemy
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player


class Level:

    def __init__(self, window, name, menu_option, player_score):
        self.window: Surface = window
        self.name = name
        self.mode = menu_option
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'Bg'))
        player = EntityFactory.get_entity('Player1')
        player.score = player_score[0]
        self.entity_list.append(player)
        if menu_option in [MENU_OPTION[1], MENU_OPTION[2]]:
            player2 = EntityFactory.get_entity('Player2')
            player.score = player_score[1]
            self.entity_list.append(player2)
        pygame.time.set_timer(EVENT_ENEMY, 4000)
        self.timeout = 20000
        pygame.time.set_timer(EVENT_TIMEOUT, 100)

    def run(self, player_score):
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)

                if ent.name == 'Player1':
                    self.level_text(14, f'Player1 - Health  {ent.health} Score: {ent.score}', COLOR_GREEN, (10, 25))
                if ent.name == 'Player2':
                    self.level_text(14, f'Player2 - Health  {ent.health}', COLOR_GREEN, (10, 45))

            self.level_text(14, f'{self.name}: Timeout: {self.timeout / 1000:.2f}', COLOR_GREEN, (10, 5))
            self.level_text(14, f'fps: {clock.get_fps() :.0f}', COLOR_GREEN, (10, WIN_HEIGHT - 35))
            self.level_text(14, f'entidades: {len(self.entity_list) :.0f}', COLOR_GREEN, (10, WIN_HEIGHT - 20))
            pygame.display.flip()
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)
            for event in pygame.event.get():
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= 100
                    if self.timeout == 0:
                        for ent in self.entity_list:
                            if isinstance(ent, Player) and ent.name == 'Player1':
                                player_score[0] = ent.score
                            if isinstance(ent, Player) and ent.name == 'Player2':
                                player_score[1] = ent.score
                        return True

                found_player = False
                for ent in self.entity_list:
                    if isinstance(ent, Player):
                        found_player = True
                if not found_player:
                    return False

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='Lucid Sans Typewriter', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
