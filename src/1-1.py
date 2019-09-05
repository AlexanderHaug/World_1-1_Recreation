import pygame
import global_constants.global_constants as gc
import global_constants.Player as Player
import global_constants.Block as Block
import global_constants.Level as Level


# Create platforms for the level
class Level01(Level.Level):
    """ Definition for level 1."""

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.Level.__init__(self, player)

        self.level_limit = -6000

        firstLand = gc.block_size * 69
        firstBlock = gc.block_size * 17
        firstLandGap = firstLand + (gc.block_size * 2)

        secondLand = gc.block_size * 16
        secondLandFirstBlock = firstLandGap + (gc.block_size * 7)
        secondLandGap = firstLandGap + secondLand + (gc.block_size * 3)

        thirdLand = gc.block_size * 65
        thirdLandFirstBlock = secondLandGap + (gc.block_size * 3)
        thirdLandGap = secondLandGap + thirdLand + (gc.block_size * 2)

        fourthLand = gc.block_size * 57
        fourthLandFirstBlock = thirdLandGap





        # Array with width, height, x, and y of platform
        levelBlocks = [

                    # First Patch of Ground
                    [firstLand, gc.block_size, 0, gc.screen_height - (gc.block_size), gc.ground],  # The Bottom
                    [firstLand, gc.block_size, 0, gc.screen_height - (gc.block_size * 2), gc.ground],  # The Top

                    #         ?
                    #    ?  B?B?B   P   P   P   P   
                    [gc.block_size, gc.block_size, firstBlock, (gc.screen_height - (gc.block_size * 6)), gc.gold_block],

                    [gc.block_size, gc.block_size, firstBlock + (gc.block_size * 4), gc.screen_height - (gc.block_size * 6), gc.block],
                    [gc.block_size, gc.block_size, firstBlock + (gc.block_size * 5), gc.screen_height - (gc.block_size * 6), gc.gold_block],
                    [gc.block_size, gc.block_size, firstBlock + (gc.block_size * 6), gc.screen_height - (gc.block_size * 6), gc.block],
                    [gc.block_size, gc.block_size, firstBlock + (gc.block_size * 7), gc.screen_height - (gc.block_size * 6), gc.gold_block],  # Mushroom Block
                    [gc.block_size, gc.block_size, firstBlock + (gc.block_size * 8), gc.screen_height - (gc.block_size * 6), gc.block],
                    [gc.block_size, gc.block_size, firstBlock + (gc.block_size * 6), gc.screen_height - (gc.block_size * 10), gc.gold_block],  # Top Block

                    [gc.block_size * 2, gc.block_size * 2, firstBlock + (gc.block_size * 12), gc.screen_height - (gc.block_size * 4), gc.pipe],  # First Pipe
                    [gc.block_size * 2, gc.block_size * 3, firstBlock + (gc.block_size * 22), gc.screen_height - (gc.block_size * 5), gc.pipe],  # Second Pipe
                    [gc.block_size * 2, gc.block_size * 4, firstBlock + (gc.block_size * 30), gc.screen_height - (gc.block_size * 6), gc.pipe],  # Third Pipe
                    [gc.block_size * 2, gc.block_size * 4, firstBlock + (gc.block_size * 41), gc.screen_height - (gc.block_size * 6), gc.pipe],  # Fourth Pipe


                    # Second Patch of Ground
                    [secondLand, gc.block_size, firstLandGap, gc.screen_height - (gc.block_size), gc.ground],  # The Bottom Fist Patch Ground
                    [secondLand, gc.block_size, firstLandGap, gc.screen_height - (gc.block_size * 2), gc.ground],  # The Top First Patch Ground

                    #      BBBBBBBB
                    #   B?B
                    [gc.block_size, gc.block_size, secondLandFirstBlock, gc.screen_height - (gc.block_size * 6), gc.block],
                    [gc.block_size, gc.block_size, secondLandFirstBlock + (gc.block_size), gc.screen_height - (gc.block_size * 6), gc.gold_block], # Mushroom/Fire Flower Block
                    [gc.block_size, gc.block_size, secondLandFirstBlock + (gc.block_size * 2), gc.screen_height - (gc.block_size * 6), gc.block],

                    [gc.block_size, gc.block_size, secondLandFirstBlock + (gc.block_size * 3), gc.screen_height - (gc.block_size * 10), gc.block],
                    [gc.block_size, gc.block_size, secondLandFirstBlock + (gc.block_size * 4), gc.screen_height - (gc.block_size * 10), gc.block],
                    [gc.block_size, gc.block_size, secondLandFirstBlock + (gc.block_size * 5), gc.screen_height - (gc.block_size * 10), gc.block],
                    [gc.block_size, gc.block_size, secondLandFirstBlock + (gc.block_size * 6), gc.screen_height - (gc.block_size * 10), gc.block],
                    [gc.block_size, gc.block_size, secondLandFirstBlock + (gc.block_size * 7), gc.screen_height - (gc.block_size * 10), gc.block],
                    [gc.block_size, gc.block_size, secondLandFirstBlock + (gc.block_size * 8), gc.screen_height - (gc.block_size * 10), gc.block],
                    [gc.block_size, gc.block_size, secondLandFirstBlock + (gc.block_size * 9), gc.screen_height - (gc.block_size * 10), gc.block],
                    [gc.block_size, gc.block_size, secondLandFirstBlock + (gc.block_size * 10), gc.screen_height - (gc.block_size * 10), gc.block],


                    # Third Patch of Ground
                    [thirdLand, gc.block_size, secondLandGap, gc.screen_height - gc.block_size, gc.ground],  # The Bottom Fist Patch Ground
                    [thirdLand, gc.block_size, secondLandGap, gc.screen_height - (gc.block_size * 2), gc.ground],  # The Top First Patch Ground

                    #   BBB?              ?           BBB   B??B
                    #      B    BB     ?  ?  ?     B         BB     H   H   H
                    [gc.block_size, gc.block_size, thirdLandFirstBlock, gc.screen_height - (gc.block_size * 10), gc.block],
                    [gc.block_size, gc.block_size, thirdLandFirstBlock + (gc.block_size), gc.screen_height - (gc.block_size * 10), gc.block],
                    [gc.block_size, gc.block_size, thirdLandFirstBlock + (gc.block_size * 2), gc.screen_height - (gc.block_size * 10), gc.block],
                    [gc.block_size, gc.block_size, thirdLandFirstBlock + (gc.block_size * 3), gc.screen_height - (gc.block_size * 10), gc.gold_block],
                    [gc.block_size, gc.block_size, thirdLandFirstBlock + (gc.block_size * 3), gc.screen_height - (gc.block_size * 6), gc.block], # Coin Block

                    [gc.block_size, gc.block_size, thirdLandFirstBlock + (gc.block_size * 9), gc.screen_height - (gc.block_size * 6), gc.block],
                    [gc.block_size, gc.block_size, thirdLandFirstBlock + (gc.block_size * 10), gc.screen_height - (gc.block_size * 6), gc.block], # Star Block

                    [gc.block_size, gc.block_size, thirdLandFirstBlock + (gc.block_size * 15), gc.screen_height - (gc.block_size * 6), gc.gold_block],
                    [gc.block_size, gc.block_size, thirdLandFirstBlock + (gc.block_size * 18), gc.screen_height - (gc.block_size * 6), gc.gold_block],
                    [gc.block_size, gc.block_size, thirdLandFirstBlock + (gc.block_size * 21), gc.screen_height - (gc.block_size * 6), gc.gold_block],
                    [gc.block_size, gc.block_size, thirdLandFirstBlock + (gc.block_size * 18), gc.screen_height - (gc.block_size * 10), gc.gold_block], # Fire Flower

                    [gc.block_size, gc.block_size, thirdLandFirstBlock + (gc.block_size * 27), gc.screen_height - (gc.block_size * 6), gc.block],
                    [gc.block_size, gc.block_size, thirdLandFirstBlock + (gc.block_size * 30), gc.screen_height - (gc.block_size * 10), gc.block],
                    [gc.block_size, gc.block_size, thirdLandFirstBlock + (gc.block_size * 31), gc.screen_height - (gc.block_size * 10), gc.block],
                    [gc.block_size, gc.block_size, thirdLandFirstBlock + (gc.block_size * 32), gc.screen_height - (gc.block_size * 10), gc.block],

                    [gc.block_size, gc.block_size, thirdLandFirstBlock + (gc.block_size * 37), gc.screen_height - (gc.block_size * 10), gc.block],
                    [gc.block_size, gc.block_size, thirdLandFirstBlock + (gc.block_size * 38), gc.screen_height - (gc.block_size * 10), gc.gold_block],
                    [gc.block_size, gc.block_size, thirdLandFirstBlock + (gc.block_size * 39), gc.screen_height - (gc.block_size * 10), gc.gold_block],
                    [gc.block_size, gc.block_size, thirdLandFirstBlock + (gc.block_size * 40), gc.screen_height - (gc.block_size * 10), gc.block],

                    [gc.block_size, gc.block_size, thirdLandFirstBlock + (gc.block_size * 38), gc.screen_height - (gc.block_size * 10), gc.block],
                    [gc.block_size, gc.block_size, thirdLandFirstBlock + (gc.block_size * 39), gc.screen_height - (gc.block_size * 10), gc.block],


                    [gc.block_size, gc.block_size, thirdLandFirstBlock + (gc.block_size * 43), gc.screen_height - (gc.block_size * 3), gc.hard_block],
                    [gc.block_size, gc.block_size, thirdLandFirstBlock + (gc.block_size * 44), gc.screen_height - (gc.block_size * 3), gc.hard_block],
                    [gc.block_size, gc.block_size, thirdLandFirstBlock + (gc.block_size * 45), gc.screen_height - (gc.block_size * 3), gc.hard_block],
                    [gc.block_size, gc.block_size, thirdLandFirstBlock + (gc.block_size * 46), gc.screen_height - (gc.block_size * 3), gc.hard_block],
                    [gc.block_size, gc.block_size, thirdLandFirstBlock + (gc.block_size * 44), gc.screen_height - (gc.block_size * 4), gc.hard_block],
                    [gc.block_size, gc.block_size, thirdLandFirstBlock + (gc.block_size * 45), gc.screen_height - (gc.block_size * 4), gc.hard_block],
                    [gc.block_size, gc.block_size, thirdLandFirstBlock + (gc.block_size * 46), gc.screen_height - (gc.block_size * 4), gc.hard_block],
                    [gc.block_size, gc.block_size, thirdLandFirstBlock + (gc.block_size * 45), gc.screen_height - (gc.block_size * 5), gc.hard_block],
                    [gc.block_size, gc.block_size, thirdLandFirstBlock + (gc.block_size * 46), gc.screen_height - (gc.block_size * 5), gc.hard_block],
                    [gc.block_size, gc.block_size, thirdLandFirstBlock + (gc.block_size * 46), gc.screen_height - (gc.block_size * 6), gc.hard_block],

                    [gc.block_size, gc.block_size, thirdLandFirstBlock + (gc.block_size * 49), gc.screen_height - (gc.block_size * 6), gc.hard_block],
                    [gc.block_size, gc.block_size, thirdLandFirstBlock + (gc.block_size * 49), gc.screen_height - (gc.block_size * 5), gc.hard_block],
                    [gc.block_size, gc.block_size, thirdLandFirstBlock + (gc.block_size * 50), gc.screen_height - (gc.block_size * 5), gc.hard_block],
                    [gc.block_size, gc.block_size, thirdLandFirstBlock + (gc.block_size * 49), gc.screen_height - (gc.block_size * 4), gc.hard_block],
                    [gc.block_size, gc.block_size, thirdLandFirstBlock + (gc.block_size * 50), gc.screen_height - (gc.block_size * 4), gc.hard_block],
                    [gc.block_size, gc.block_size, thirdLandFirstBlock + (gc.block_size * 51), gc.screen_height - (gc.block_size * 4), gc.hard_block],
                    [gc.block_size, gc.block_size, thirdLandFirstBlock + (gc.block_size * 49), gc.screen_height - (gc.block_size * 3), gc.hard_block],
                    [gc.block_size, gc.block_size, thirdLandFirstBlock + (gc.block_size * 50), gc.screen_height - (gc.block_size * 3), gc.hard_block],
                    [gc.block_size, gc.block_size, thirdLandFirstBlock + (gc.block_size * 51), gc.screen_height - (gc.block_size * 3), gc.hard_block],
                    [gc.block_size, gc.block_size, thirdLandFirstBlock + (gc.block_size * 52), gc.screen_height - (gc.block_size * 3), gc.hard_block],

                    [gc.block_size, gc.block_size, thirdLandFirstBlock + (gc.block_size * 57), gc.screen_height - (gc.block_size * 3), gc.hard_block],
                    [gc.block_size, gc.block_size, thirdLandFirstBlock + (gc.block_size * 58), gc.screen_height - (gc.block_size * 3), gc.hard_block],
                    [gc.block_size, gc.block_size, thirdLandFirstBlock + (gc.block_size * 59), gc.screen_height - (gc.block_size * 3), gc.hard_block],
                    [gc.block_size, gc.block_size, thirdLandFirstBlock + (gc.block_size * 60), gc.screen_height - (gc.block_size * 3), gc.hard_block],
                    [gc.block_size, gc.block_size, thirdLandFirstBlock + (gc.block_size * 61), gc.screen_height - (gc.block_size * 3), gc.hard_block],
                    [gc.block_size, gc.block_size, thirdLandFirstBlock + (gc.block_size * 58), gc.screen_height - (gc.block_size * 4), gc.hard_block],
                    [gc.block_size, gc.block_size, thirdLandFirstBlock + (gc.block_size * 59), gc.screen_height - (gc.block_size * 4), gc.hard_block],
                    [gc.block_size, gc.block_size, thirdLandFirstBlock + (gc.block_size * 60), gc.screen_height - (gc.block_size * 4), gc.hard_block],
                    [gc.block_size, gc.block_size, thirdLandFirstBlock + (gc.block_size * 61), gc.screen_height - (gc.block_size * 4), gc.hard_block],
                    [gc.block_size, gc.block_size, thirdLandFirstBlock + (gc.block_size * 59), gc.screen_height - (gc.block_size * 5), gc.hard_block],
                    [gc.block_size, gc.block_size, thirdLandFirstBlock + (gc.block_size * 60), gc.screen_height - (gc.block_size * 5), gc.hard_block],
                    [gc.block_size, gc.block_size, thirdLandFirstBlock + (gc.block_size * 61), gc.screen_height - (gc.block_size * 5), gc.hard_block],
                    [gc.block_size, gc.block_size, thirdLandFirstBlock + (gc.block_size * 60), gc.screen_height - (gc.block_size * 6), gc.hard_block],
                    [gc.block_size, gc.block_size, thirdLandFirstBlock + (gc.block_size * 61), gc.screen_height - (gc.block_size * 6), gc.hard_block],

                    # Fourth Patch of Ground
                    [fourthLand, gc.block_size, thirdLandGap, gc.screen_height - gc.block_size, gc.ground], # The Bottom Fist Patch Ground
                    [fourthLand, gc.block_size, thirdLandGap, gc.screen_height - (gc.block_size * 2), gc.ground], # The Top First Patch Ground

                    #         BB?B
                    #  S   P          PS   F
                    [gc.block_size, gc.block_size, fourthLandFirstBlock, gc.screen_height - (gc.block_size * 6), gc.hard_block],
                    [gc.block_size, gc.block_size, fourthLandFirstBlock, gc.screen_height - (gc.block_size * 5), gc.hard_block],
                    [gc.block_size, gc.block_size, fourthLandFirstBlock + (gc.block_size), gc.screen_height - (gc.block_size * 5), gc.hard_block],
                    [gc.block_size, gc.block_size, fourthLandFirstBlock, gc.screen_height - (gc.block_size * 4), gc.hard_block],
                    [gc.block_size, gc.block_size, fourthLandFirstBlock + (gc.block_size), gc.screen_height - (gc.block_size * 4), gc.hard_block],
                    [gc.block_size, gc.block_size, fourthLandFirstBlock + (gc.block_size * 2), gc.screen_height - (gc.block_size * 4), gc.hard_block],
                    [gc.block_size, gc.block_size, fourthLandFirstBlock, gc.screen_height - (gc.block_size * 3), gc.hard_block],
                    [gc.block_size, gc.block_size, fourthLandFirstBlock + (gc.block_size), gc.screen_height - (gc.block_size * 3), gc.hard_block],
                    [gc.block_size, gc.block_size, fourthLandFirstBlock + (gc.block_size * 2), gc.screen_height - (gc.block_size * 3), gc.hard_block],
                    [gc.block_size, gc.block_size, fourthLandFirstBlock + (gc.block_size * 3), gc.screen_height - (gc.block_size * 3), gc.hard_block],

                    [gc.block_size * 2, gc.block_size * 2, fourthLandFirstBlock + (gc.block_size * 8), gc.screen_height - (gc.block_size * 4), gc.pipe],

                    [gc.block_size, gc.block_size, fourthLandFirstBlock + (gc.block_size * 13), gc.screen_height - (gc.block_size * 6), gc.block],
                    [gc.block_size, gc.block_size, fourthLandFirstBlock + (gc.block_size * 14), gc.screen_height - (gc.block_size * 6), gc.block],
                    [gc.block_size, gc.block_size, fourthLandFirstBlock + (gc.block_size * 15), gc.screen_height - (gc.block_size * 6), gc.gold_block],
                    [gc.block_size, gc.block_size, fourthLandFirstBlock + (gc.block_size * 16), gc.screen_height - (gc.block_size * 6), gc.block],

                    [gc.block_size * 2, gc.block_size * 2, fourthLandFirstBlock + (gc.block_size * 24), gc.screen_height - (gc.block_size * 4), gc.pipe],

                    [gc.block_size, gc.block_size, fourthLandFirstBlock + (gc.block_size * 26), gc.screen_height - (gc.block_size * 3), gc.hard_block],
                    [gc.block_size, gc.block_size, fourthLandFirstBlock + (gc.block_size * 27), gc.screen_height - (gc.block_size * 3), gc.hard_block],
                    [gc.block_size, gc.block_size, fourthLandFirstBlock + (gc.block_size * 28), gc.screen_height - (gc.block_size * 3), gc.hard_block],
                    [gc.block_size, gc.block_size, fourthLandFirstBlock + (gc.block_size * 29), gc.screen_height - (gc.block_size * 3), gc.hard_block],
                    [gc.block_size, gc.block_size, fourthLandFirstBlock + (gc.block_size * 30), gc.screen_height - (gc.block_size * 3), gc.hard_block],
                    [gc.block_size, gc.block_size, fourthLandFirstBlock + (gc.block_size * 31), gc.screen_height - (gc.block_size * 3), gc.hard_block],
                    [gc.block_size, gc.block_size, fourthLandFirstBlock + (gc.block_size * 32), gc.screen_height - (gc.block_size * 3), gc.hard_block],
                    [gc.block_size, gc.block_size, fourthLandFirstBlock + (gc.block_size * 33), gc.screen_height - (gc.block_size * 3), gc.hard_block],
                    [gc.block_size, gc.block_size, fourthLandFirstBlock + (gc.block_size * 34), gc.screen_height - (gc.block_size * 3), gc.hard_block],

                    [gc.block_size, gc.block_size, fourthLandFirstBlock + (gc.block_size * 27), gc.screen_height - (gc.block_size * 4), gc.hard_block],
                    [gc.block_size, gc.block_size, fourthLandFirstBlock + (gc.block_size * 28), gc.screen_height - (gc.block_size * 4), gc.hard_block],
                    [gc.block_size, gc.block_size, fourthLandFirstBlock + (gc.block_size * 29), gc.screen_height - (gc.block_size * 4), gc.hard_block],
                    [gc.block_size, gc.block_size, fourthLandFirstBlock + (gc.block_size * 30), gc.screen_height - (gc.block_size * 4), gc.hard_block],
                    [gc.block_size, gc.block_size, fourthLandFirstBlock + (gc.block_size * 31), gc.screen_height - (gc.block_size * 4), gc.hard_block],
                    [gc.block_size, gc.block_size, fourthLandFirstBlock + (gc.block_size * 32), gc.screen_height - (gc.block_size * 4), gc.hard_block],
                    [gc.block_size, gc.block_size, fourthLandFirstBlock + (gc.block_size * 33), gc.screen_height - (gc.block_size * 4), gc.hard_block],
                    [gc.block_size, gc.block_size, fourthLandFirstBlock + (gc.block_size * 34), gc.screen_height - (gc.block_size * 4), gc.hard_block],

                    [gc.block_size, gc.block_size, fourthLandFirstBlock + (gc.block_size * 28), gc.screen_height - (gc.block_size * 5), gc.hard_block],
                    [gc.block_size, gc.block_size, fourthLandFirstBlock + (gc.block_size * 29), gc.screen_height - (gc.block_size * 5), gc.hard_block],
                    [gc.block_size, gc.block_size, fourthLandFirstBlock + (gc.block_size * 30), gc.screen_height - (gc.block_size * 5), gc.hard_block],
                    [gc.block_size, gc.block_size, fourthLandFirstBlock + (gc.block_size * 31), gc.screen_height - (gc.block_size * 5), gc.hard_block],
                    [gc.block_size, gc.block_size, fourthLandFirstBlock + (gc.block_size * 32), gc.screen_height - (gc.block_size * 5), gc.hard_block],
                    [gc.block_size, gc.block_size, fourthLandFirstBlock + (gc.block_size * 33), gc.screen_height - (gc.block_size * 5), gc.hard_block],
                    [gc.block_size, gc.block_size, fourthLandFirstBlock + (gc.block_size * 34), gc.screen_height - (gc.block_size * 5), gc.hard_block],

                    [gc.block_size, gc.block_size, fourthLandFirstBlock + (gc.block_size * 29), gc.screen_height - (gc.block_size * 6), gc.hard_block],
                    [gc.block_size, gc.block_size, fourthLandFirstBlock + (gc.block_size * 30), gc.screen_height - (gc.block_size * 6), gc.hard_block],
                    [gc.block_size, gc.block_size, fourthLandFirstBlock + (gc.block_size * 31), gc.screen_height - (gc.block_size * 6), gc.hard_block],
                    [gc.block_size, gc.block_size, fourthLandFirstBlock + (gc.block_size * 32), gc.screen_height - (gc.block_size * 6), gc.hard_block],
                    [gc.block_size, gc.block_size, fourthLandFirstBlock + (gc.block_size * 33), gc.screen_height - (gc.block_size * 6), gc.hard_block],
                    [gc.block_size, gc.block_size, fourthLandFirstBlock + (gc.block_size * 34), gc.screen_height - (gc.block_size * 6), gc.hard_block],

                    [gc.block_size, gc.block_size, fourthLandFirstBlock + (gc.block_size * 30), gc.screen_height - (gc.block_size * 7), gc.hard_block],
                    [gc.block_size, gc.block_size, fourthLandFirstBlock + (gc.block_size * 31), gc.screen_height - (gc.block_size * 7), gc.hard_block],
                    [gc.block_size, gc.block_size, fourthLandFirstBlock + (gc.block_size * 32), gc.screen_height - (gc.block_size * 7), gc.hard_block],
                    [gc.block_size, gc.block_size, fourthLandFirstBlock + (gc.block_size * 33), gc.screen_height - (gc.block_size * 7), gc.hard_block],
                    [gc.block_size, gc.block_size, fourthLandFirstBlock + (gc.block_size * 34), gc.screen_height - (gc.block_size * 7), gc.hard_block],

                    [gc.block_size, gc.block_size, fourthLandFirstBlock + (gc.block_size * 31), gc.screen_height - (gc.block_size * 8), gc.hard_block],
                    [gc.block_size, gc.block_size, fourthLandFirstBlock + (gc.block_size * 32), gc.screen_height - (gc.block_size * 8), gc.hard_block],
                    [gc.block_size, gc.block_size, fourthLandFirstBlock + (gc.block_size * 33), gc.screen_height - (gc.block_size * 8), gc.hard_block],
                    [gc.block_size, gc.block_size, fourthLandFirstBlock + (gc.block_size * 34), gc.screen_height - (gc.block_size * 8), gc.hard_block],

                    [gc.block_size, gc.block_size, fourthLandFirstBlock + (gc.block_size * 32), gc.screen_height - (gc.block_size * 9), gc.hard_block],
                    [gc.block_size, gc.block_size, fourthLandFirstBlock + (gc.block_size * 33), gc.screen_height - (gc.block_size * 9), gc.hard_block],
                    [gc.block_size, gc.block_size, fourthLandFirstBlock + (gc.block_size * 34), gc.screen_height - (gc.block_size * 9), gc.hard_block],

                    [gc.block_size, gc.block_size, fourthLandFirstBlock + (gc.block_size * 33), gc.screen_height - (gc.block_size * 10), gc.hard_block],
                    [gc.block_size, gc.block_size, fourthLandFirstBlock + (gc.block_size * 34), gc.screen_height - (gc.block_size * 10), gc.hard_block],

                    [gc.block_size, gc.block_size * 13, fourthLandFirstBlock + (gc.block_size * 43), gc.screen_height - (gc.block_size * 15), gc.flag],
                 ]

        # Go through the array above and add platforms
        for platform in levelBlocks:
            block = Block.Block(platform[0], platform[1], platform[4])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)


def main():
    """ Main Program """
    pygame.init()

    # Set the height and width of the screen
    size = [gc.screen_width, gc.screen_height]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("HAUUUUG 1-1")

    # Create the player
    player = Player.Player()

    # Create all the levels
    level_list = []
    level_list.append(Level01(player))

    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]

    active_sprite_list = pygame.sprite.Group()
    player.level = current_level

    player.rect.x = 0
    player.rect.y = gc.screen_height - (gc.block_size * 3)
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
    pygame.mixer.music.load(gc.overworld_music)
    pygame.mixer.music.play(-1)
    main()

