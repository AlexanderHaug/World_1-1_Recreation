import pygame
import global_constants.global_constants as gc


class Level():
    def __init__(self, player):
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player
        self.world_shift = 0

    def update(self):
        self.platform_list.update()
        self.enemy_list.update()

    def draw(self, screen):

        screen.fill(gc.sky_blue)

        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)

    def move_screen(self, shift_x):

        self.world_shift += shift_x

        for platform in self.platform_list:
            platform.rect.x += shift_x

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x
