import pygame, random

pygame.init()

Window_Width = 600
Window_Height = 600
display_surface = pygame.display.set_mode((Window_Width, Window_Height))
pygame.display.set_caption("~~Snake~~")

FPS = 20
clock = pygame.time.Clock()

snake_size = 20
Head_x = Window_Width / 2
Head_y = Window_Height / 2 + 100
snake_dx = 0
snake_dy = 0
Score = 0

Green = (0, 175, 0)
Red = (175, 0, 0)
White = (255, 255, 255)
Dark_Green = (10, 50, 10)
Dark_Red = (150, 0, 0)

font = pygame.font.SysFont('gabriola', 48)

def create_text_and_rect(text, color, background_color, **locations):
    text = font.render(text, True, color, background_color)
    rect = text.get_rect()
    for location in locations.keys():
        if location == "center":
            rect.center = locations[location]
        for location in locations.keys():
            if location == "topleft":
                rect.topleft = locations[location]
    return text, rect

title_text, title_rect = create_text_and_rect("~~Snake~~", Green, Dark_Red,
                                             center=(Window_Width // 2, Window_Height // 2))
score_text, score_rect = create_text_and_rect("Score: " + str(score), Green, Dark_Red,
                                             center=(10, 10))
Game_over_text, Game_over_rect = create_text_and_rect("GAMEOVER", Red, Dark_Green,
                                             center=(Window_Width // 2, Window_Height // 2))
Continue_text, Continue_rect = create_text_and_rect("Press any ket to play again!", Red, Dark_Green,
                                             center=(Window_Width // 2, Window_Height // 2 + 64))

Pick_up_sound = pygame.mixer.Sound("pick_up_sound.wav")

apple_coord = (500, 500, snake_size, snake_size)
apple_rect = pygame.draw.rect(display_surface, Red, apple_coord)

# Set images (in this case, use simple rects...so just create their coordinates)
# For a rectangle you need (top-left x, top-left y, width, height)

head_coord = (Head_x, Head_y, snake_size, snake_size)
head_rect = pygame.draw.rect(display_surface, Green, head_coord)
body_coords = []

# The main game loop
running = True
is_paused = False

while running:

def move_snake(event):
    global snake_dx, snake_dy
    if event.type == pygame.KEYDOWN:
        key = event.key
        if key = pygame.K_LEFT:
            snake_dx = -1 * snake_size
            snake_dy = 0
        if key = pygame.K_RIGHT:
            snake_dx = snake_size
            snake_dy = 0
        if key = pygame.K_UP:
            snake_dx = 0
            snake_dy = -1 * snake_size
        if key = pygame.K_DOWN:
            snake_dx = 0
            snake_dy = snake_size


def check_quit(event):
    global running
    if event = pygame.QUIT:
        running = False

def check_events():
    global running
    # TODO: create a for loop events is the variable pygame.event.get() is the list
        check_quit()
        move_snake()
    pass  # TODO: remove this pass when done.

def handle_snake():
    global body_coords
    global head_x
    global head_y
    global head_coord
    global snake_dx, snake_dy
    # TODO: call body_coords.insert() method and pass in 0, head_coord
    # TODO: call body_coords.pop()
    # TODO: add snake_dx to head_x
    # TODO: add snake_dy to head_y
    # TODO: set head_coord to (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)

def reset_game_after_game_over(event):
    global is_paused, score, head_x, head_y, head_coord, body_coords, snake_dx, snake_dy
    if event.type = pygame.KEYDOWN:
        score = 0
        head_x = window_width / 2
        head_y = window_height / 2 + 100
        head_coord = (head_x, head_y, snake_size, snake_size)
        body_coords = []
        snake_dx = 0
        snake_dy = 0
        is_paused = False

def check_end_game_after_game_over(event):
    global is_paused
    global running
    if event.type = pygame.QUIT:
        is_paused = False
        running = False


def check_game_over():
    global head_rect
    global head_coord
    global body_coords
    global running
    global is_paused
    # TODO: if head_rect.left is negative or head_rect.right is greater than WINDOW_WIDTH or head_rect.top is negative or head_rect.bottom is greater than WINDOW_HEIGHT
    # or head_coord in body_coords
        # TODO: then do the following
        # TODO: call display_surface.blit(game_over_text, game_over_rect)
        # TODO: call display_surface.blit(continue_text, continue_rect)
        # TODO: call pygame.display.update()
        # TODO: set is_paused to True
        # TODO: while is_paused
            # TODO: for event in pygame.event.get()
                # TODO: call reset_game_after_game_over(event)
                # TODO: call check_end_game_after_game_over(event)

def check_collisions():
    global score, apple_x, apple_y, apple_coord, body_coords
    if head_rect.collidrect(apple_rect):
        score = score + 1

        apple_x = random.randint(0, window_width - snake_size)
        apple_y = random.randint(0, window_height - snake_size)
        apple_coord = (apple_x, apple_y, snake_size, snake_size)
        body_coords.append(head_coord)

def blit_hud():
    # TODO: call display_surface.blit(title_text, title_rect)
    # TODO: call display_surface.blit(score_text, score_rect)
    pass  # TODO: remove this pass when done.

def blit_assets():
    # TODO: for body in body_coords:
        # TODO: call pygame.draw.rect(display_surface, DARKGREEN, body)
    # TODO: set head_rect to pygame.draw.rect(display_surface, GREEN, head_coord)
    # TODO: set apple_rect to pygame.draw.rect(display_surface, RED, apple_coord)
    pass  # TODO: remove this pass when done.

def update_display_and_tick_clock():
    # TODO: call pygame.display.update()
    # TODO: call clock.tick(FPS)
    pass  # TODO: remove this pass when done.

while running:
    # Check pygame events
    check_events()

    # handle growing and manipulating the snake
    handle_snake()

    # Check for game over
    check_game_over()

    # Check for collisions
    check_collisions()

    score_text = font.render("Score: " + str(score), True, green, darkred)

    display_surface.fill(white)

    # Blit HUD
    blit_hud()

    # Blit assets
    blit_assets()

    # Update display and tick clock
    update_display_and_tick_clock()

# End the game
pygame.quit()
