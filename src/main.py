import pygame
import global_constants.global_constants as gc
import global_constants.Player as Player
import level_collection.Level11 as Lc11


def setup_screen(screen_title):
    size = [gc.screen_width, gc.screen_height]
    pygame.display.set_caption(screen_title)
    return pygame.display.set_mode(size)


def main():
    pygame.init()

    screen = setup_screen("HAUUUUG Mario Recreation")
    screen_rct = screen.get_rect()

    player = Player.Player()

    level_1_1 = Lc11.Level11(player)
    level_list = []
    level_list.append(level_1_1)

    current_level_no = 0
    current_level = level_list[current_level_no]

    active_sprite_list = pygame.sprite.Group()
    player.level = current_level

    player.rect.x = 0
    player.rect.y = gc.screen_height - (gc.block_size * 3)
    active_sprite_list.add(player)

    done = False

    clock = pygame.time.Clock()

    screen_tracker = 0

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

        player.rect.clamp_ip(screen_rct)
        active_sprite_list.update()
        current_level.update()

        if player.rect.right >= 500:
            diff = player.rect.right - 500
            player.rect.right = 500
            current_level.move_screen(-diff)
            screen_tracker += diff

        if player.rect.y == 570:
            player.rect.x = 0
            player.rect.y = gc.screen_height - (gc.block_size * 3)
            current_level.move_screen(screen_tracker)
            screen_tracker = 0

        current_level.draw(screen)
        active_sprite_list.draw(screen)

        clock.tick(60)

        pygame.display.flip()
        print(screen_tracker)

    pygame.quit()


if __name__ == "__main__":
    pygame.mixer.init()
    pygame.mixer.music.load(gc.overworld_music)
    pygame.mixer.music.play(-1)
    main()

