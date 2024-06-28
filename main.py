from code.Game import Game

game = Game()
game.run()

# import pygamed
# from pygame import Surface, Rect
#
# W_WIDTH = 576
# W_HEIGHT = 324
# # initializer o modulo pygame
# pygame.init()
# window: Surface = pygame.display.set_mode(size=(W_WIDTH, W_HEIGHT))
#
# bg_surf: Surface = pygame.image.load('./asset/bg_menu.png').convert_alpha()
# player1_surf: Surface = pygame.image.load('./asset/player1.png').convert_alpha()
#
# bg_rect: Rect = bg_surf.get_rect(left=0, top=0)
# player1_rect: Rect = player1_surf.get_rect(left=0, top=0)
#
# window.blit(source=bg_surf, dest=bg_rect)
# window.blit(source=player1_surf, dest=player1_rect)
#
# pygame.display.flip()
#
# clock = pygame.time.Clock()
#
# while True:
#     clock.tick(140)
#     print(clock.get_fps())
#     window.blit(source=bg_surf, dest=bg_rect)
#     window.blit(source=player1_surf, dest=player1_rect)
#     pygame.display.flip()
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             quit()
#
#     pressed_key = pygame.key.get_pressed()
#     if pressed_key[pygame.K_w]:
#         player1_rect.centery -= 1
#     if pressed_key[pygame.K_a]:
#         player1_rect.centerx -= 1
#     if pressed_key[pygame.K_s]:
#         player1_rect.centery += 1
#     if pressed_key[pygame.K_d]:
#         player1_rect.centerx += 1
#
#
