import sys
import pygame
import random


pygame.init()
SCREEN = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Menu")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 100)


def main():

    menu()


def menu():

    img = pygame.image.load("keys.png").convert()
    pygame.display.set_caption("Menu")
    menu_items = ["Play", "Difficulty", "Quit"]
    current_selection = 0
    SCREEN.fill((0, 0, 0))

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    current_selection = (current_selection - 1) % len(menu_items)
                elif event.key == pygame.K_DOWN:
                    current_selection = (current_selection + 1) % len(menu_items)
                elif event.key == pygame.K_RETURN:
                    if current_selection == 0:
                        play()
                    elif current_selection == 1:
                        difficulty()
                    else:
                        pygame.quit()
                        sys.exit()
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        for i, item in enumerate(menu_items):

            if i == current_selection:
                text = font.render(item, True, (255, 255, 0))
                SCREEN.blit(text, (250, 160 + i * 100))

            else:
                text = font.render(item, True, (255, 255, 255))
                SCREEN.blit(text, (250, 160 + i * 100))

        SCREEN.blit(img, (368, 500))
        pygame.draw.rect(SCREEN, "grey", SCREEN.get_rect(), 20)
        pygame.draw.rect(SCREEN, "grey", (0, 20, SCREEN.get_width(), 20))
        pygame.display.flip()
        pygame.time.Clock().tick(30)


def difficulty():
    pygame.display.set_caption("Settings")
    current_selection = 0
    level_items = ["Level 1", "Level 2", "Level 3"]
    SCREEN.fill((0, 0, 0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    current_selection = (current_selection - 1) % len(level_items)
                elif event.key == pygame.K_DOWN:
                    current_selection = (current_selection + 1) % len(level_items)
                elif event.key == pygame.K_RETURN:
                    if current_selection == 0:
                        play(10)
                    elif current_selection == 1:
                        play(15)
                    else:
                        play(20)
                elif event.key == pygame.K_ESCAPE:
                    menu()

        for i, item in enumerate(level_items):

            if i == current_selection:
                text = font.render(item, True, (255, 255, 0))
                SCREEN.blit(text, (250, 160 + i * 100))

            else:
                text = font.render(item, True, (255, 255, 255))
                SCREEN.blit(text, (250, 160 + i * 100))

        pygame.draw.rect(SCREEN, "grey", SCREEN.get_rect(), 20)
        pygame.draw.rect(SCREEN, "grey", (0, 20, SCREEN.get_width(), 20))
        pygame.display.flip()
        pygame.time.Clock().tick(30)


def play(level=10):
    score = 0
    font = pygame.font.SysFont(None, 40)
    pygame.display.set_caption("Snake")
    running = True
    direction = None
    last_key = None
    key_pressed = False
    snake, rect_width, rect_height, yellow_color = snake_init()
    target_x, target_y, target_width, target_height, red_color = target_init(
        snake[0][0], snake[0][1]
    )
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN and not key_pressed:
                key_pressed = True
                last_key = event.key
                if event.key == pygame.K_LEFT and direction != "right":
                    direction = "left"
                elif event.key == pygame.K_RIGHT and direction != "left":
                    direction = "right"
                elif event.key == pygame.K_UP and direction != "down":
                    direction = "up"
                elif event.key == pygame.K_DOWN and direction != "up":
                    direction = "down"
                elif event.key == pygame.K_ESCAPE:
                    menu()

            if event.type == pygame.KEYUP:
                key_pressed = False
        # snake's movement, each segment follow one in front of him
        for i in range(len(snake) - 1, 0, -1):
            snake[i] = snake[i - 1]
        # update head placement
        snake[0] = check_direction(direction, snake[0][0], snake[0][1])
        # check if head collides segment
        for segment in snake[1:]:
            if segment == snake[0]:
                game_over(level)
        # check if head collides with screen border
        if not (
            0 < snake[0][0] < SCREEN.get_width() - rect_width
            and 20 < snake[0][1] < SCREEN.get_height() - rect_height
        ):
            game_over(level)

        if snake[0][0] == target_x and snake[0][1] == target_y:
            snake.append((target_x, target_y))
            target_x, target_y, target_width, target_height, red_color = target_init(
                snake[0][0], snake[0][1]
            )
            score += 1
        # display update
        SCREEN.fill((0, 0, 0))
        for segment in snake:
            pygame.draw.rect(SCREEN, yellow_color, (*segment, rect_width, rect_height))
        pygame.draw.rect(
            SCREEN, red_color, (target_x, target_y, target_width, target_height)
        )
        pygame.draw.rect(SCREEN, "grey", SCREEN.get_rect(), 20)
        pygame.draw.rect(SCREEN, "grey", (0, 20, SCREEN.get_width(), 20))
        text = font.render(f"Score : {score}", True, (0, 0, 0))
        SCREEN.blit(text, (20, 10))
        pygame.display.flip()

        clock.tick(level)


def snake_init():
    rect_x, rect_y = random_starting_position()
    rect_width = 20
    rect_height = 20
    yellow_color = (255, 255, 0)
    snake = [(rect_x, rect_y)]
    return snake, rect_width, rect_height, yellow_color


def target_init(rect_x, rect_y):
    while True:
        target_x, target_y = random_starting_position()
        if rect_x == target_x and rect_y == target_y:
            pass
        else:
            break
    target_width = 20
    target_height = 20
    red_color = "red"
    return target_x, target_y, target_width, target_height, red_color


def check_direction(direction, x, y):
    if direction == "left":
        return (x - 20), y
    elif direction == "right":
        return (x + 20), y
    elif direction == "up":
        return x, (y - 20)
    elif direction == "down":
        return x, (y + 20)
    else:
        return x, y


def random_starting_position():
    n1 = random.randint(40 // 20, 760 // 20) * 20
    n2 = random.randint(40 // 20, 560 // 20) * 20
    return n1, n2


def game_over(speed):
    pygame.display.set_caption("Game Over")
    game_over = ["Play again", "Menu", "Quit"]
    current_selection = 0
    font_game_over = pygame.font.SysFont(None, 150)
    font = pygame.font.SysFont(None, 50)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    menu()
                elif event.key == pygame.K_UP:
                    current_selection = (current_selection - 1) % len(game_over)
                elif event.key == pygame.K_DOWN:
                    current_selection = (current_selection + 1) % len(game_over)
                elif event.key == pygame.K_RETURN:
                    if current_selection == 0:
                        play(speed)
                    elif current_selection == 1:
                        menu()
                    else:
                        pygame.quit()
                        sys.exit()

        text = font_game_over.render("Game Over", True, (255, 255, 255))
        SCREEN.blit(text, (100, 100))
        for i, item in enumerate(game_over):

            if i == current_selection:
                text = font.render(item, True, (255, 255, 0))
                SCREEN.blit(text, (300, 350 + i * 50))

            else:
                text = font.render(item, True, (255, 255, 255))
                SCREEN.blit(text, (300, 350 + i * 50))

        pygame.display.flip()
        pygame.time.Clock().tick(30)


if __name__ == "__main__":
    main()
