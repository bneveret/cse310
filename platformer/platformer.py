# -- Set Up -- #
import pygame, sys

clock = pygame.time.Clock()

from pygame.locals import *
pygame.init()

# Game Name
pygame.display.set_caption('Platform Draft')

#Create Display
WINDOW_SIZE = (600, 400)

screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)

display = pygame.Surface((450, 300))

# Setup Score Display
font = pygame.font.Font('freesansbold.ttf', 16)
textX = 375
textY = 10

def show_score(x,y):
    score = font.render('Score: ' + str(coin_int), True, (255, 255, 255))
    display.blit(score, (x, y))

# -- Game Images -- #
# Clembod
player_image = pygame.image.load('warrior/Individual_Sprite/idle/Warrior_Idle_1.png')

# IconArchive
coin_image = pygame.image.load('tiles/coin.png')

# Dafluffy Potato
grass_image = pygame.image.load('tiles/grass.png')
dirt_image = pygame.image.load('tiles/dirt.png')
TILE_SIZE = dirt_image.get_width()

# Creating the Map
def load_map(path):
    f = open(path + '.txt', 'r')
    data = f.read()
    f.close()
    data = data.split('\n')
    game_map = []
    for row in data:
        game_map.append(list(row))
    return game_map

game_map = load_map('map')

def collision_test(rect, tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list

# Player Movement
def move(rect, movement, tiles):
    collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}
    rect.x += movement[0]
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if movement[0] > 0:
            rect.right = tile.left
            collision_types['right'] = True
        elif movement[0] < 0:
            rect.left = tile.right
            collision_types['left'] = True
    rect.y += movement[1]
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if movement[1] > 0:
            rect.bottom = tile.top
            collision_types['bottom'] = True
        elif movement[1] < 0:
            rect.top = tile.bottom
            collision_types['top'] = True
    return rect, collision_types

moving_right = False
moving_left = False

# Physics and display scroll effect
player_velocity = 0
air_timer = 0

scroll = [0,0]

player_rect = pygame.Rect(50, 50, player_image.get_width(), player_image.get_height())

# create coins
coins = []
coin_int = 0

y=0
for row in game_map:
        x = 0
        for tile in row:
            if tile == 'C':
                coins.append([x*TILE_SIZE,y*TILE_SIZE])
            x+=1
        y+=1

# -- Game Loop -- #
while True:
    # Setting the Screen
    display.fill((146,244,255))

    scroll[0] += (player_rect.x-scroll[0]-197)/20
    scroll[1] += (player_rect.y-scroll[1]-150)/20

    tile_rects = []
    y = 0
    for row in game_map:
        x = 0
        for tile in row:
            if tile == '1':
                display.blit(dirt_image, (x*TILE_SIZE-scroll[0], y*TILE_SIZE-scroll[1]))
            if tile == '2':
                display.blit(grass_image, (x*TILE_SIZE-scroll[0], y*TILE_SIZE-scroll[1]))
            if tile != '0' and tile !='C':
                tile_rects.append(pygame.Rect(x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE))
            x += 1
        y += 1
    # Coin set up and collection
    for coin in coins:
        display.blit(coin_image, (coin[0]-scroll[0], coin[1]-scroll[1]))
        coin_rect = pygame.Rect((coin[0], coin[1],TILE_SIZE,TILE_SIZE))
        if player_rect.colliderect(coin_rect):
            coins.remove(coin)
            pygame.mixer.Sound('pickupCoin.wav').play()
            coin_int += 1

    # Movement 
    player_movement = [0, 0]
    if moving_right:
        player_movement[0] += 2
    if moving_left:
        player_movement[0] -= 2
    player_movement[1] += player_velocity
    player_velocity += 0.2
    if player_velocity > 3:
        player_velocity = 3

    # Physics checks
    player_rect, collisions = move(player_rect, player_movement, tile_rects)
    if collisions['top'] and player_velocity < 0:
        player_velocity = 1
    if collisions['bottom']:
        player_velocity = 0
        air_timer = 0
    else:
        air_timer += 1

    # Show Score
    display.blit(player_image, (player_rect.x-scroll[0], player_rect.y-scroll[1]))
    show_score(textX, textY)

    # Pygame Events
    for event in pygame.event.get():
        # Quit Event
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        # Keyboard Events
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                moving_right = True
            if event.key == K_LEFT:
                moving_left = True
            if event.key == K_UP:
                if air_timer < 6:
                    player_velocity = -6
        if event.type == KEYUP:
            if event.key == K_RIGHT:
                moving_right = False
            if event.key == K_LEFT:
                moving_left = False

    # Scaled Screen
    surf = pygame.transform.scale(display, WINDOW_SIZE)
    screen.blit(surf, (0, 0))
    pygame.display.update()
    clock.tick(60)