import pygame


class Block(pygame.sprite.Sprite):
    """ Platform the user can jump on """

    def __init__(self, width, height, im):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this code.
            """

        super().__init__()

        self.image = pygame.transform.scale(im, (width, height))

        self.rect = self.image.get_rect()
