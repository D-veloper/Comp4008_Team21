# Lets create our Rummikub Game:
import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
BLUE = (0, 0, 180)
RED = (180, 0, 0)
GREEN = (0,180,0)
YELLOW = (250,250,0)
WHITE = (255,255,255)
PURPLE = (128,0,128)

# Classes
class Tile:
    def __init__(self, value, color):
        self.value = value
        self.color = color
        self.width, self.height = 50, 70
        self.image = pygame.image.load('tile.png')

    def draw(self, x, y):
        # pygame.draw.rect(screen, self.color, (x, y, self.width, self.height))
        font = pygame.font.Font(None, 36)
        text = font.render(str(self.value), True, BLUE)
        screen.blit(self.image, (x, y))
    
    # Create tiles with values 1-15 and F

# The racks holds tiles for each player
class Rack:
    def __init__(self):
        # start with an empty rack
        self.tiles = []

    def draw(self, x, y):
        font = pygame.font.Font(None, 36)
        text = font.render(str(self.value), True, BLUE)
        screen.blit(text, (x, y))

    def add_tile(self,tile):
        pass
    
    # get total value of tiles in the rack
    def get_total_value(self):
        value = 0
        for tile in self.tiles:
            value += tile.value
        return value
    
class Pool:
    def __init__(self):
        self.tiles = [Tile(i % 15 + 1, t) for t in tile_colors for i in range(15)]

    def remove_picked_tiles(self):
        self.tiles.pop() # to be improved

        

class Player:
    def __init__(self,rack):
        self.rack = rack
    









# Initialize Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rummikub")

# Create tiles
tile_colors = [RED,BLUE,GREEN,YELLOW,PURPLE]


# Shuffle tiles
# random.shuffle(tiles)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw tiles
    screen.fill(WHITE)
    x, y = 50, 50
    for tile in tiles:
        print(tile.value,tile.color)
        tile.draw(x, y)
        x += 70  # Spacing between tiles

    pygame.display.flip()
    pygame.time.Clock().tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()