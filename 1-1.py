import pygame, os

PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                    'Assets/')


# Much of the base code is from a Platforming Tutorial at:
# http://programarcadegames.com/python_examples/show_file.php?file=platform_scroller.py

# Global constants

# Background Color
SKYBLUE = (135, 206, 250)

# The width and height of an individual block, as well as small Mario, in pixels
blockSize = 30

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Mario Images for the Sprites
# Cannot change sprite because, not using a Sprite map.
MarioStill = pygame.image.load(PATH + 'MarioStill.png')
MarioBlock = pygame.image.load(PATH + 'MarioBlock.gif')
MarioGoldBlock = pygame.image.load(PATH + 'MarioGoldBlock.png')
MarioPipe = pygame.image.load(PATH + 'MarioPipe.png')
MarioGround = pygame.image.load(PATH + 'MarioGround.png')
MarioHardBlock = pygame.image.load(PATH + 'MarioHardBlock.png')
MarioFlag = pygame.image.load(PATH + 'MarioFlag.png')


class Player(pygame.sprite.Sprite):
    """
    This class represents the bar at the bottom that the player controls.
    """

    # -- Methods
    def __init__(self):
        """ Constructor function"""

        # Call the parent's constructor
        super().__init__()

        # Create an image of the block, and fill it with a color
        # This could also be an image loaded from the disk.
        width = blockSize
        height = blockSize
        self.image = pygame.transform.scale(MarioStill, (width, height))

        # Set a reference to the image rect.
        self.rect = self.image.get_rect()

        # Set speed vector of player
        self.change_x = 0
        self.change_y = 0

        # List of sprites we can bump against
        self.level = None

    def update(self):
        """ Move the player. """

        # Gravity
        self.calc_grav()

        # Move left/right
        self.rect.x += self.change_x

        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

        # Move up/down
        self.rect.y += self.change_y

        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            # Stop our vertical movement
            self.change_y = 0

    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35

        # See if we are on the ground.
        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = SCREEN_HEIGHT - self.rect.height

    def jump(self):
        """ Called when user hits 'jump' button. """

        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down 1
        # when working with a platform moving down.
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2

        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.change_y = -10

    # Player-controlled movement:
    def go_left(self):
        """ Called we the user hits the left arrow. """
        self.change_x = -6

    def go_right(self):
        """ Called we the user hits the right arrow. """
        self.change_x = 6

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0


class Block(pygame.sprite.Sprite):
    """ Platform the user can jump on """

    def __init__(self, width, height, im):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this code.
            """

        super().__init__()

        self.image = pygame.transform.scale(im, (width, height))

        self.rect = self.image.get_rect()

class Level():
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """

    def __init__(self, player):
        """ Constructor. Pass in a handle to player. Needed for when moving
            platforms collide with the player."""
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player

        # How far this world has been scrolled left/right
        self.world_shift = 0

    # Update everything on this level
    def update(self):
        """ Update everything in this level."""
        self.platform_list.update()
        self.enemy_list.update()

    def draw(self, screen):
        """ Draw everything on this level."""

        # Draw the background
        screen.fill(SKYBLUE)

        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)

    def shift_world(self, shift_x):
        """ When the user moves left/right and we need to scroll everything: """

        # Keep track of the shift amount
        self.world_shift += shift_x

        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x


# Create platforms for the level
class Level_01(Level):
    """ Definition for level 1."""

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.level_limit = -6000

        firstLand = blockSize * 69
        firstBlock = blockSize * 17
        firstLandGap = firstLand + (blockSize*2)

        secondLand = blockSize * 16
        secondLandFirstBlock = firstLandGap + (blockSize*7)
        secondLandGap = firstLandGap + secondLand + (blockSize*3)

        thirdLand = blockSize * 65
        thirdLandFirstBlock = secondLandGap + (blockSize*3)
        thirdLandGap = secondLandGap + thirdLand + (blockSize*2)

        fourthLand = blockSize * 57
        fourthLandFirstBlock = thirdLandGap





        # Array with width, height, x, and y of platform
        levelBlocks = [

                    # First Patch of Ground
                    [firstLand, blockSize, 0, SCREEN_HEIGHT - (blockSize), MarioGround],  # The Bottom
                    [firstLand, blockSize, 0, SCREEN_HEIGHT - (blockSize * 2), MarioGround],  # The Top

                    #         ?
                    #    ?  B?B?B   P   P   P   P   
                    [blockSize, blockSize, firstBlock, (SCREEN_HEIGHT - (blockSize*6)), MarioGoldBlock],

                    [blockSize, blockSize, firstBlock + (blockSize * 4), SCREEN_HEIGHT - (blockSize * 6), MarioBlock],
                    [blockSize, blockSize, firstBlock + (blockSize * 5), SCREEN_HEIGHT - (blockSize * 6), MarioGoldBlock],
                    [blockSize, blockSize, firstBlock + (blockSize * 6), SCREEN_HEIGHT - (blockSize * 6), MarioBlock],
                    [blockSize, blockSize, firstBlock + (blockSize * 7), SCREEN_HEIGHT - (blockSize * 6), MarioGoldBlock],  # Mushroom Block
                    [blockSize, blockSize, firstBlock + (blockSize * 8), SCREEN_HEIGHT - (blockSize * 6), MarioBlock],
                    [blockSize, blockSize, firstBlock + (blockSize * 6), SCREEN_HEIGHT - (blockSize * 10), MarioGoldBlock],  # Top Block

                    [blockSize*2, blockSize*2, firstBlock + (blockSize * 12), SCREEN_HEIGHT - (blockSize * 4), MarioPipe],  # First Pipe
                    [blockSize*2, blockSize*3, firstBlock + (blockSize * 22), SCREEN_HEIGHT - (blockSize * 5), MarioPipe],  # Second Pipe
                    [blockSize*2, blockSize*4, firstBlock + (blockSize * 30), SCREEN_HEIGHT - (blockSize * 6), MarioPipe],  # Third Pipe
                    [blockSize*2, blockSize*4, firstBlock + (blockSize * 41), SCREEN_HEIGHT - (blockSize * 6), MarioPipe],  # Fourth Pipe


                    # Second Patch of Ground
                    [secondLand, blockSize, firstLandGap, SCREEN_HEIGHT - (blockSize), MarioGround],  # The Bottom Fist Patch Ground
                    [secondLand, blockSize, firstLandGap, SCREEN_HEIGHT - (blockSize * 2), MarioGround],  # The Top First Patch Ground

                    #      BBBBBBBB
                    #   B?B
                    [blockSize, blockSize, secondLandFirstBlock, SCREEN_HEIGHT - (blockSize*6), MarioBlock],
                    [blockSize, blockSize, secondLandFirstBlock + (blockSize), SCREEN_HEIGHT - (blockSize*6), MarioGoldBlock], # Mushroom/Fire Flower Block
                    [blockSize, blockSize, secondLandFirstBlock + (blockSize*2), SCREEN_HEIGHT - (blockSize*6), MarioBlock],

                    [blockSize, blockSize, secondLandFirstBlock + (blockSize * 3), SCREEN_HEIGHT - (blockSize * 10), MarioBlock],
                    [blockSize, blockSize, secondLandFirstBlock + (blockSize * 4), SCREEN_HEIGHT - (blockSize * 10), MarioBlock],
                    [blockSize, blockSize, secondLandFirstBlock + (blockSize * 5), SCREEN_HEIGHT - (blockSize * 10), MarioBlock],
                    [blockSize, blockSize, secondLandFirstBlock + (blockSize * 6), SCREEN_HEIGHT - (blockSize * 10), MarioBlock],
                    [blockSize, blockSize, secondLandFirstBlock + (blockSize * 7), SCREEN_HEIGHT - (blockSize * 10), MarioBlock],
                    [blockSize, blockSize, secondLandFirstBlock + (blockSize * 8), SCREEN_HEIGHT - (blockSize * 10), MarioBlock],
                    [blockSize, blockSize, secondLandFirstBlock + (blockSize * 9), SCREEN_HEIGHT - (blockSize * 10), MarioBlock],
                    [blockSize, blockSize, secondLandFirstBlock + (blockSize * 10), SCREEN_HEIGHT - (blockSize * 10), MarioBlock],


                    # Third Patch of Ground
                    [thirdLand, blockSize, secondLandGap, SCREEN_HEIGHT - blockSize, MarioGround],  # The Bottom Fist Patch Ground
                    [thirdLand, blockSize, secondLandGap, SCREEN_HEIGHT - (blockSize * 2), MarioGround],  # The Top First Patch Ground

                    #   BBB?              ?           BBB   B??B
                    #      B    BB     ?  ?  ?     B         BB     H   H   H
                    [blockSize, blockSize, thirdLandFirstBlock, SCREEN_HEIGHT - (blockSize*10), MarioBlock],
                    [blockSize, blockSize, thirdLandFirstBlock + (blockSize), SCREEN_HEIGHT - (blockSize * 10), MarioBlock],
                    [blockSize, blockSize, thirdLandFirstBlock + (blockSize*2), SCREEN_HEIGHT - (blockSize * 10), MarioBlock],
                    [blockSize, blockSize, thirdLandFirstBlock + (blockSize*3), SCREEN_HEIGHT - (blockSize * 10), MarioGoldBlock],
                    [blockSize, blockSize, thirdLandFirstBlock + (blockSize*3), SCREEN_HEIGHT - (blockSize * 6), MarioBlock], # Coin Block

                    [blockSize, blockSize, thirdLandFirstBlock + (blockSize * 9), SCREEN_HEIGHT - (blockSize * 6), MarioBlock],
                    [blockSize, blockSize, thirdLandFirstBlock + (blockSize * 10), SCREEN_HEIGHT - (blockSize * 6), MarioBlock], # Star Block

                    [blockSize, blockSize, thirdLandFirstBlock + (blockSize * 15), SCREEN_HEIGHT - (blockSize * 6), MarioGoldBlock],
                    [blockSize, blockSize, thirdLandFirstBlock + (blockSize * 18), SCREEN_HEIGHT - (blockSize * 6), MarioGoldBlock],
                    [blockSize, blockSize, thirdLandFirstBlock + (blockSize * 21), SCREEN_HEIGHT - (blockSize * 6), MarioGoldBlock],
                    [blockSize, blockSize, thirdLandFirstBlock + (blockSize * 18), SCREEN_HEIGHT - (blockSize * 10), MarioGoldBlock], # Fire Flower

                    [blockSize, blockSize, thirdLandFirstBlock + (blockSize * 27), SCREEN_HEIGHT - (blockSize * 6), MarioBlock],
                    [blockSize, blockSize, thirdLandFirstBlock + (blockSize * 30), SCREEN_HEIGHT - (blockSize * 10), MarioBlock],
                    [blockSize, blockSize, thirdLandFirstBlock + (blockSize * 31), SCREEN_HEIGHT - (blockSize * 10), MarioBlock],
                    [blockSize, blockSize, thirdLandFirstBlock + (blockSize * 32), SCREEN_HEIGHT - (blockSize * 10), MarioBlock],

                    [blockSize, blockSize, thirdLandFirstBlock + (blockSize * 37), SCREEN_HEIGHT - (blockSize * 10), MarioBlock],
                    [blockSize, blockSize, thirdLandFirstBlock + (blockSize * 38), SCREEN_HEIGHT - (blockSize * 10), MarioGoldBlock],
                    [blockSize, blockSize, thirdLandFirstBlock + (blockSize * 39), SCREEN_HEIGHT - (blockSize * 10), MarioGoldBlock],
                    [blockSize, blockSize, thirdLandFirstBlock + (blockSize * 40), SCREEN_HEIGHT - (blockSize * 10), MarioBlock],

                    [blockSize, blockSize, thirdLandFirstBlock + (blockSize * 38), SCREEN_HEIGHT - (blockSize * 10), MarioBlock],
                    [blockSize, blockSize, thirdLandFirstBlock + (blockSize * 39), SCREEN_HEIGHT - (blockSize * 10), MarioBlock],


                    [blockSize, blockSize, thirdLandFirstBlock + (blockSize * 43), SCREEN_HEIGHT - (blockSize * 3), MarioHardBlock],
                    [blockSize, blockSize, thirdLandFirstBlock + (blockSize * 44), SCREEN_HEIGHT - (blockSize * 3), MarioHardBlock],
                    [blockSize, blockSize, thirdLandFirstBlock + (blockSize * 45), SCREEN_HEIGHT - (blockSize * 3), MarioHardBlock],
                    [blockSize, blockSize, thirdLandFirstBlock + (blockSize * 46), SCREEN_HEIGHT - (blockSize * 3), MarioHardBlock],
                    [blockSize, blockSize, thirdLandFirstBlock + (blockSize * 44), SCREEN_HEIGHT - (blockSize * 4), MarioHardBlock],
                    [blockSize, blockSize, thirdLandFirstBlock + (blockSize * 45), SCREEN_HEIGHT - (blockSize * 4), MarioHardBlock],
                    [blockSize, blockSize, thirdLandFirstBlock + (blockSize * 46), SCREEN_HEIGHT - (blockSize * 4), MarioHardBlock],
                    [blockSize, blockSize, thirdLandFirstBlock + (blockSize * 45), SCREEN_HEIGHT - (blockSize * 5), MarioHardBlock],
                    [blockSize, blockSize, thirdLandFirstBlock + (blockSize * 46), SCREEN_HEIGHT - (blockSize * 5), MarioHardBlock],
                    [blockSize, blockSize, thirdLandFirstBlock + (blockSize * 46), SCREEN_HEIGHT - (blockSize * 6), MarioHardBlock],

                    [blockSize, blockSize, thirdLandFirstBlock + (blockSize * 49), SCREEN_HEIGHT - (blockSize * 6), MarioHardBlock],
                    [blockSize, blockSize, thirdLandFirstBlock + (blockSize * 49), SCREEN_HEIGHT - (blockSize * 5), MarioHardBlock],
                    [blockSize, blockSize, thirdLandFirstBlock + (blockSize * 50), SCREEN_HEIGHT - (blockSize * 5), MarioHardBlock],
                    [blockSize, blockSize, thirdLandFirstBlock + (blockSize * 49), SCREEN_HEIGHT - (blockSize * 4), MarioHardBlock],
                    [blockSize, blockSize, thirdLandFirstBlock + (blockSize * 50), SCREEN_HEIGHT - (blockSize * 4), MarioHardBlock],
                    [blockSize, blockSize, thirdLandFirstBlock + (blockSize * 51), SCREEN_HEIGHT - (blockSize * 4), MarioHardBlock],
                    [blockSize, blockSize, thirdLandFirstBlock + (blockSize * 49), SCREEN_HEIGHT - (blockSize * 3), MarioHardBlock],
                    [blockSize, blockSize, thirdLandFirstBlock + (blockSize * 50), SCREEN_HEIGHT - (blockSize * 3), MarioHardBlock],
                    [blockSize, blockSize, thirdLandFirstBlock + (blockSize * 51), SCREEN_HEIGHT - (blockSize * 3), MarioHardBlock],
                    [blockSize, blockSize, thirdLandFirstBlock + (blockSize * 52), SCREEN_HEIGHT - (blockSize * 3), MarioHardBlock],

                    [blockSize, blockSize, thirdLandFirstBlock + (blockSize * 57), SCREEN_HEIGHT - (blockSize * 3), MarioHardBlock],
                    [blockSize, blockSize, thirdLandFirstBlock + (blockSize * 58), SCREEN_HEIGHT - (blockSize * 3), MarioHardBlock],
                    [blockSize, blockSize, thirdLandFirstBlock + (blockSize * 59), SCREEN_HEIGHT - (blockSize * 3), MarioHardBlock],
                    [blockSize, blockSize, thirdLandFirstBlock + (blockSize * 60), SCREEN_HEIGHT - (blockSize * 3), MarioHardBlock],
                    [blockSize, blockSize, thirdLandFirstBlock + (blockSize * 61), SCREEN_HEIGHT - (blockSize * 3), MarioHardBlock],
                    [blockSize, blockSize, thirdLandFirstBlock + (blockSize * 58), SCREEN_HEIGHT - (blockSize * 4), MarioHardBlock],
                    [blockSize, blockSize, thirdLandFirstBlock + (blockSize * 59), SCREEN_HEIGHT - (blockSize * 4), MarioHardBlock],
                    [blockSize, blockSize, thirdLandFirstBlock + (blockSize * 60), SCREEN_HEIGHT - (blockSize * 4), MarioHardBlock],
                    [blockSize, blockSize, thirdLandFirstBlock + (blockSize * 61), SCREEN_HEIGHT - (blockSize * 4), MarioHardBlock],
                    [blockSize, blockSize, thirdLandFirstBlock + (blockSize * 59), SCREEN_HEIGHT - (blockSize * 5), MarioHardBlock],
                    [blockSize, blockSize, thirdLandFirstBlock + (blockSize * 60), SCREEN_HEIGHT - (blockSize * 5), MarioHardBlock],
                    [blockSize, blockSize, thirdLandFirstBlock + (blockSize * 61), SCREEN_HEIGHT - (blockSize * 5), MarioHardBlock],
                    [blockSize, blockSize, thirdLandFirstBlock + (blockSize * 60), SCREEN_HEIGHT - (blockSize * 6), MarioHardBlock],
                    [blockSize, blockSize, thirdLandFirstBlock + (blockSize * 61), SCREEN_HEIGHT - (blockSize * 6), MarioHardBlock],

                    # Fourth Patch of Ground
                    [fourthLand, blockSize, thirdLandGap, SCREEN_HEIGHT - blockSize, MarioGround], # The Bottom Fist Patch Ground
                    [fourthLand, blockSize, thirdLandGap, SCREEN_HEIGHT - (blockSize * 2), MarioGround], # The Top First Patch Ground

                    #         BB?B
                    #  S   P          PS   F
                    [blockSize, blockSize, fourthLandFirstBlock, SCREEN_HEIGHT - (blockSize * 6), MarioHardBlock],
                    [blockSize, blockSize, fourthLandFirstBlock, SCREEN_HEIGHT - (blockSize * 5), MarioHardBlock],
                    [blockSize, blockSize, fourthLandFirstBlock + (blockSize), SCREEN_HEIGHT - (blockSize * 5), MarioHardBlock],
                    [blockSize, blockSize, fourthLandFirstBlock, SCREEN_HEIGHT - (blockSize * 4), MarioHardBlock],
                    [blockSize, blockSize, fourthLandFirstBlock + (blockSize), SCREEN_HEIGHT - (blockSize * 4), MarioHardBlock],
                    [blockSize, blockSize, fourthLandFirstBlock + (blockSize * 2), SCREEN_HEIGHT - (blockSize * 4), MarioHardBlock],
                    [blockSize, blockSize, fourthLandFirstBlock, SCREEN_HEIGHT - (blockSize * 3), MarioHardBlock],
                    [blockSize, blockSize, fourthLandFirstBlock + (blockSize), SCREEN_HEIGHT - (blockSize * 3), MarioHardBlock],
                    [blockSize, blockSize, fourthLandFirstBlock + (blockSize * 2), SCREEN_HEIGHT - (blockSize * 3), MarioHardBlock],
                    [blockSize, blockSize, fourthLandFirstBlock + (blockSize * 3), SCREEN_HEIGHT - (blockSize * 3), MarioHardBlock],

                    [blockSize*2, blockSize*2, fourthLandFirstBlock + (blockSize * 8), SCREEN_HEIGHT - (blockSize * 4), MarioPipe],

                    [blockSize, blockSize, fourthLandFirstBlock + (blockSize * 13), SCREEN_HEIGHT - (blockSize * 6), MarioBlock],
                    [blockSize, blockSize, fourthLandFirstBlock + (blockSize * 14), SCREEN_HEIGHT - (blockSize * 6), MarioBlock],
                    [blockSize, blockSize, fourthLandFirstBlock + (blockSize * 15), SCREEN_HEIGHT - (blockSize * 6), MarioGoldBlock],
                    [blockSize, blockSize, fourthLandFirstBlock + (blockSize * 16), SCREEN_HEIGHT - (blockSize * 6), MarioBlock],

                    [blockSize*2, blockSize*2, fourthLandFirstBlock + (blockSize * 24), SCREEN_HEIGHT - (blockSize * 4), MarioPipe],

                    [blockSize, blockSize, fourthLandFirstBlock + (blockSize * 26), SCREEN_HEIGHT - (blockSize * 3), MarioHardBlock],
                    [blockSize, blockSize, fourthLandFirstBlock + (blockSize * 27), SCREEN_HEIGHT - (blockSize * 3), MarioHardBlock],
                    [blockSize, blockSize, fourthLandFirstBlock + (blockSize * 28), SCREEN_HEIGHT - (blockSize * 3), MarioHardBlock],
                    [blockSize, blockSize, fourthLandFirstBlock + (blockSize * 29), SCREEN_HEIGHT - (blockSize * 3), MarioHardBlock],
                    [blockSize, blockSize, fourthLandFirstBlock + (blockSize * 30), SCREEN_HEIGHT - (blockSize * 3), MarioHardBlock],
                    [blockSize, blockSize, fourthLandFirstBlock + (blockSize * 31), SCREEN_HEIGHT - (blockSize * 3), MarioHardBlock],
                    [blockSize, blockSize, fourthLandFirstBlock + (blockSize * 32), SCREEN_HEIGHT - (blockSize * 3), MarioHardBlock],
                    [blockSize, blockSize, fourthLandFirstBlock + (blockSize * 33), SCREEN_HEIGHT - (blockSize * 3), MarioHardBlock],
                    [blockSize, blockSize, fourthLandFirstBlock + (blockSize * 34), SCREEN_HEIGHT - (blockSize * 3), MarioHardBlock],

                    [blockSize, blockSize, fourthLandFirstBlock + (blockSize * 27), SCREEN_HEIGHT - (blockSize * 4), MarioHardBlock],
                    [blockSize, blockSize, fourthLandFirstBlock + (blockSize * 28), SCREEN_HEIGHT - (blockSize * 4), MarioHardBlock],
                    [blockSize, blockSize, fourthLandFirstBlock + (blockSize * 29), SCREEN_HEIGHT - (blockSize * 4), MarioHardBlock],
                    [blockSize, blockSize, fourthLandFirstBlock + (blockSize * 30), SCREEN_HEIGHT - (blockSize * 4), MarioHardBlock],
                    [blockSize, blockSize, fourthLandFirstBlock + (blockSize * 31), SCREEN_HEIGHT - (blockSize * 4), MarioHardBlock],
                    [blockSize, blockSize, fourthLandFirstBlock + (blockSize * 32), SCREEN_HEIGHT - (blockSize * 4), MarioHardBlock],
                    [blockSize, blockSize, fourthLandFirstBlock + (blockSize * 33), SCREEN_HEIGHT - (blockSize * 4), MarioHardBlock],
                    [blockSize, blockSize, fourthLandFirstBlock + (blockSize * 34), SCREEN_HEIGHT - (blockSize * 4), MarioHardBlock],

                    [blockSize, blockSize, fourthLandFirstBlock + (blockSize * 28), SCREEN_HEIGHT - (blockSize * 5), MarioHardBlock],
                    [blockSize, blockSize, fourthLandFirstBlock + (blockSize * 29), SCREEN_HEIGHT - (blockSize * 5), MarioHardBlock],
                    [blockSize, blockSize, fourthLandFirstBlock + (blockSize * 30), SCREEN_HEIGHT - (blockSize * 5), MarioHardBlock],
                    [blockSize, blockSize, fourthLandFirstBlock + (blockSize * 31), SCREEN_HEIGHT - (blockSize * 5), MarioHardBlock],
                    [blockSize, blockSize, fourthLandFirstBlock + (blockSize * 32), SCREEN_HEIGHT - (blockSize * 5), MarioHardBlock],
                    [blockSize, blockSize, fourthLandFirstBlock + (blockSize * 33), SCREEN_HEIGHT - (blockSize * 5), MarioHardBlock],
                    [blockSize, blockSize, fourthLandFirstBlock + (blockSize * 34), SCREEN_HEIGHT - (blockSize * 5), MarioHardBlock],

                    [blockSize, blockSize, fourthLandFirstBlock + (blockSize * 29), SCREEN_HEIGHT - (blockSize * 6), MarioHardBlock],
                    [blockSize, blockSize, fourthLandFirstBlock + (blockSize * 30), SCREEN_HEIGHT - (blockSize * 6), MarioHardBlock],
                    [blockSize, blockSize, fourthLandFirstBlock + (blockSize * 31), SCREEN_HEIGHT - (blockSize * 6), MarioHardBlock],
                    [blockSize, blockSize, fourthLandFirstBlock + (blockSize * 32), SCREEN_HEIGHT - (blockSize * 6), MarioHardBlock],
                    [blockSize, blockSize, fourthLandFirstBlock + (blockSize * 33), SCREEN_HEIGHT - (blockSize * 6), MarioHardBlock],
                    [blockSize, blockSize, fourthLandFirstBlock + (blockSize * 34), SCREEN_HEIGHT - (blockSize * 6), MarioHardBlock],

                    [blockSize, blockSize, fourthLandFirstBlock + (blockSize * 30), SCREEN_HEIGHT - (blockSize * 7), MarioHardBlock],
                    [blockSize, blockSize, fourthLandFirstBlock + (blockSize * 31), SCREEN_HEIGHT - (blockSize * 7), MarioHardBlock],
                    [blockSize, blockSize, fourthLandFirstBlock + (blockSize * 32), SCREEN_HEIGHT - (blockSize * 7), MarioHardBlock],
                    [blockSize, blockSize, fourthLandFirstBlock + (blockSize * 33), SCREEN_HEIGHT - (blockSize * 7), MarioHardBlock],
                    [blockSize, blockSize, fourthLandFirstBlock + (blockSize * 34), SCREEN_HEIGHT - (blockSize * 7), MarioHardBlock],

                    [blockSize, blockSize, fourthLandFirstBlock + (blockSize * 31), SCREEN_HEIGHT - (blockSize * 8), MarioHardBlock],
                    [blockSize, blockSize, fourthLandFirstBlock + (blockSize * 32), SCREEN_HEIGHT - (blockSize * 8), MarioHardBlock],
                    [blockSize, blockSize, fourthLandFirstBlock + (blockSize * 33), SCREEN_HEIGHT - (blockSize * 8), MarioHardBlock],
                    [blockSize, blockSize, fourthLandFirstBlock + (blockSize * 34), SCREEN_HEIGHT - (blockSize * 8), MarioHardBlock],

                    [blockSize, blockSize, fourthLandFirstBlock + (blockSize * 32), SCREEN_HEIGHT - (blockSize * 9), MarioHardBlock],
                    [blockSize, blockSize, fourthLandFirstBlock + (blockSize * 33), SCREEN_HEIGHT - (blockSize * 9), MarioHardBlock],
                    [blockSize, blockSize, fourthLandFirstBlock + (blockSize * 34), SCREEN_HEIGHT - (blockSize * 9), MarioHardBlock],

                    [blockSize, blockSize, fourthLandFirstBlock + (blockSize * 33), SCREEN_HEIGHT - (blockSize * 10), MarioHardBlock],
                    [blockSize, blockSize, fourthLandFirstBlock + (blockSize * 34), SCREEN_HEIGHT - (blockSize * 10), MarioHardBlock],

                    [blockSize, blockSize*13, fourthLandFirstBlock + (blockSize * 43), SCREEN_HEIGHT - (blockSize * 15), MarioFlag],
                 ]


        # Go through the array above and add platforms
        for platform in levelBlocks:
            block = Block(platform[0], platform[1], platform[4])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

def main():
    """ Main Program """
    pygame.init()

    # Set the height and width of the screen
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("HAUUUUG 1-1")

    # Create the player
    player = Player()

    # Create all the levels
    level_list = []
    level_list.append(Level_01(player))

    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]

    active_sprite_list = pygame.sprite.Group()
    player.level = current_level

    player.rect.x = 0
    player.rect.y = SCREEN_HEIGHT - (blockSize*3)
    active_sprite_list.add(player)

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # ---------- Main Program Loop -------------
    while not done:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.jump()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()

        # Update the player.
        active_sprite_list.update()

        # Update items in the level
        current_level.update()

        # If the player gets near the right side, shift the world left (-x)
        if player.rect.right >= 500:
            diff = player.rect.right - 500
            player.rect.right = 500
            current_level.shift_world(-diff)

        # If the player gets near the left side, shift the world right (+x)
        if player.rect.left <= 120:
            diff = 120 - player.rect.left
            player.rect.left = 120
            current_level.shift_world(diff)

        # If the player gets to the end of the level, go to the next level
        current_position = player.rect.x + current_level.world_shift
        if current_position < current_level.level_limit:
            player.rect.x = 120
            if current_level_no < len(level_list) - 1:
                current_level_no += 1
                current_level = level_list[current_level_no]
                player.level = current_level

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        current_level.draw(screen)
        active_sprite_list.draw(screen)

        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()


if __name__ == "__main__":
    pygame.mixer.init()
    pygame.mixer.music.load(PATH + "OverWorld.wav")
    pygame.mixer.music.play(-1)
    main()

