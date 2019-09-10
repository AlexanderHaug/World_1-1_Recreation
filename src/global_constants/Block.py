import pygame


class Block(pygame.sprite.Sprite):
    def __init__(self, width, height, im):
        super().__init__()

        self.image = pygame.transform.scale(im, (width, height))
        self.rect = self.image.get_rect()
