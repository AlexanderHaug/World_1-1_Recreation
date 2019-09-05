import pygame
import os

PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                    '../../Assets/')

# Global constants

# Background Color
sky_blue = (135, 206, 250)

# The width and height of an individual block, as well as small Mario, in pixels
block_size = 30

# Screen dimensions
screen_width = 800
screen_height = 600

# Mario Images for the Sprites
# Cannot change sprite because, not using a Sprite map.
mario_still = pygame.image.load(PATH + 'MarioStill.png')
block = pygame.image.load(PATH + 'MarioBlock.gif')
gold_block = pygame.image.load(PATH + 'MarioGoldBlock.png')
pipe = pygame.image.load(PATH + 'MarioPipe.png')
ground = pygame.image.load(PATH + 'MarioGround.png')
hard_block = pygame.image.load(PATH + 'MarioHardBlock.png')
flag = pygame.image.load(PATH + 'MarioFlag.png')
overworld_music = PATH + "OverWorld.wav"