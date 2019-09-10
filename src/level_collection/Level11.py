import global_constants.global_constants as gc
import global_constants.Block as Block
import global_constants.Level as Level


class Level11(Level.Level):
    def __init__(self, player):
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
                    [firstLand, gc.block_size * 2, 0, gc.screen_height - (gc.block_size * 2), gc.ground],

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
                    [secondLand, gc.block_size * 2, firstLandGap, gc.screen_height - (gc.block_size * 2), gc.ground],

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
                    [thirdLand, gc.block_size * 2, secondLandGap, gc.screen_height - (gc.block_size * 2), gc.ground],

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
                    [fourthLand, gc.block_size * 2, thirdLandGap, gc.screen_height - (gc.block_size * 2), gc.ground],

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

        # Go through the array above and add platforms to create the level
        for platform in levelBlocks:
            block = Block.Block(platform[0], platform[1], platform[4])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)
