import pygame

COLOR_ORANGE = (255, 128, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW = (255, 255, 128)
COLOR_GREEN = (2, 224, 6)

MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'SCORE',
               'EXIT')

MENU_SPACE = (175 + 25,
              175 + 50,
              175 + 75,
              175 + 100,
              175 + 125)

WIN_WIDTH = 576
WIN_HEIGHT = 324

ENTITY_SPEED = {'Level1Bg0': 0,
                'Level1Bg1': 1,
                'Level1Bg2': 2,
                'Level1Bg3': 3,
                'Level1Bg4': 4,
                'Level1Bg5': 5,
                'Level2Bg0': 0,
                'Level2Bg1': 1,
                'Level2Bg2': 2,
                'Level2Bg3': 3,
                'Level2Bg4': 4,
                'Level1Bg6': 6,
                'Player1': 3,
                'Player1Shot': 3,
                'Player2': 3,
                'Player2Shot': 2,
                'Enemy1': 1,
                'Enemy1Shot': 2,
                'Enemy2': 1,
                'Enemy2Shot': 2
                }

PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w}

SCORE_POS = {
    'Title': (WIN_WIDTH / 2, 50),
    'EnterName': (WIN_WIDTH / 2, 80),
    'Label': (WIN_WIDTH / 2, 90),
    'Name': (WIN_WIDTH / 2, 110),
    0: (WIN_WIDTH / 2, 130),
    1: (WIN_WIDTH / 2, 150),
    2: (WIN_WIDTH / 2, 170),
    3: (WIN_WIDTH / 2, 190),
    4: (WIN_WIDTH / 2, 210),
    5: (WIN_WIDTH / 2, 230),
    6: (WIN_WIDTH / 2, 350),
    7: (WIN_WIDTH / 2, 270),
    8: (WIN_WIDTH / 2, 290),
    9: (WIN_WIDTH / 2, 310),
}

PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                   'Player2': pygame.K_s}

PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                   'Player2': pygame.K_a}

PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                    'Player2': pygame.K_d}

EVENT_ENEMY = pygame.USEREVENT + 1

ENTITY_HEALTH = {'Level1Bg0': 999,
                 'Level1Bg1': 999,
                 'Level1Bg2': 999,
                 'Level1Bg3': 999,
                 'Level1Bg4': 999,
                 'Level1Bg5': 999,
                 'Level2Bg0': 999,
                 'Level2Bg1': 999,
                 'Level2Bg2': 999,
                 'Level2Bg3': 999,
                 'Level2Bg4': 999,
                 'Level1Bg6': 999,
                 'Player1': 300,
                 'Player1Shot': 2,
                 'Player2': 300,
                 'Player2Shot': 1,
                 'Enemy1': 50,
                 'Enemy1Shot': 1,
                 'Enemy2': 60,
                 'Enemy2Shot': 1
                 }
ENTITY_DAMAGE = {'Level1Bg0': 0,
                 'Level1Bg1': 0,
                 'Level1Bg2': 0,
                 'Level1Bg3': 0,
                 'Level1Bg4': 0,
                 'Level1Bg5': 0,
                 'Level2Bg0': 0,
                 'Level2Bg1': 0,
                 'Level2Bg2': 0,
                 'Level2Bg3': 0,
                 'Level2Bg4': 0,
                 'Level1Bg6': 0,
                 'Player1': 1,
                 'Player1Shot': 25,
                 'Player2': 1,
                 'Player2Shot': 20,
                 'Enemy1': 1,
                 'Enemy1Shot': 20,
                 'Enemy2': 1,
                 'Enemy2Shot': 15
                 }
ENTITY_SCORE = {'Level1Bg0': 0,
                'Level1Bg1': 0,
                'Level1Bg2': 0,
                'Level1Bg3': 0,
                'Level1Bg4': 0,
                'Level1Bg5': 0,
                'Level2Bg0': 0,
                'Level2Bg1': 0,
                'Level2Bg2': 0,
                'Level2Bg3': 0,
                'Level2Bg4': 0,
                'Level1Bg6': 0,
                'Player1': 0,
                'Player1Shot': 0,
                'Player2': 0,
                'Player2Shot': 0,
                'Enemy1': 100,
                'Enemy1Shot': 0,
                'Enemy2': 125,
                'Enemy2Shot': 0
                }
EVENT_TIMEOUT = pygame.USEREVENT + 2

ENTITY_SHOT_DELAY = {
    'Player1': 25,
    'Player2': 50,
    'Enemy2': 100,
    'Enemy1': 100
}

PLAYER_SHOT = {'Player1': pygame.K_LCTRL,
               'Player2': pygame.K_RCTRL}
