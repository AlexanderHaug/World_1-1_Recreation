import pygame
import global_constants.global_constants as gc
import global_constants.Player as Player
import level_collection.Level11 as Lc11


def initialization(screen):
    screen_rct = screen.get_rect()

    player = Player.Player()

    level_list = create_level_list(player)

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

    return screen_rct, player, level_list, current_level, active_sprite_list, done, clock, screen_tracker


def start_music():
    pygame.mixer.init()
    pygame.mixer.music.load(gc.overworld_music)
    pygame.mixer.music.play(-1)


def setup_screen(screen_title):

    size = [gc.screen_width, gc.screen_height]
    pygame.display.set_caption(screen_title)
    return pygame.display.set_mode(size)


def create_level_list(player):

    level_1_1 = Lc11.Level11(player)
    level_list = [level_1_1]
    return level_list


def handle_event(player, event):

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


def handle_player_movement(player, current_level, screen_tracker):

    if player.rect.y == 570:
        player.rect.x = 0
        player.rect.y = gc.screen_height - (gc.block_size * 3)
        current_level.move_screen(screen_tracker)
        return 0

    if player.rect.right >= 500:
        diff = player.rect.right - 500
        player.rect.right = 500
        current_level.move_screen(-diff)
        screen_tracker += diff
        return screen_tracker

    else:
        return screen_tracker


def update_screen(player, screen_rct, active_sprite_list, current_level, screen_tracker, screen, clock):
    player.rect.clamp_ip(screen_rct)
    active_sprite_list.update()
    current_level.update()

    screen_tracker = handle_player_movement(player, current_level, screen_tracker)

    current_level.draw(screen)
    active_sprite_list.draw(screen)

    clock.tick(60)

    pygame.display.flip()

    return screen_tracker


def main():

    pygame.init()

    screen = setup_screen("HAUUUUG Mario Recreation")

    screen_rct, player, level_list, current_level, active_sprite_list, done, clock, screen_tracker = initialization(screen)

    start_music()

    while not done:

        for event in pygame.event.get():

            handle_event(player, event)

            if event.type == pygame.QUIT:
                done = True

        screen_tracker = update_screen(player, screen_rct, active_sprite_list, current_level, screen_tracker, screen, clock)

    pygame.quit()


if __name__ == "__main__":
    main()

