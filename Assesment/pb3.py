import pygame as pg
import sys
import time
from pygame.locals import *

# initialize variables
current_player = 'x'
current_winner = None
is_draw = None


WIDTH = 400
HEIGHT = 500 # Add 100 later for the 
GRID_SIZE = 400
BACKGROUND = (255, 255, 255)
LINE_COLOR = (0, 0, 0)


grid = [[None]*3, [None]*3, [None]*3]

pg.init()
FPS = 30
clock = pg.time.Clock()

screen = pg.display.set_mode((WIDTH, HEIGHT), 0, 32) # 400 x 500 display
pg.display.set_caption("Tic Tac Toe")

font = pg.font.Font(None, 30)
size = GRID_SIZE // 6 - 20 # size of the X / O marks

def game_initiating_window():
    """initializes game window"""
    screen.fill(BACKGROUND)
    for i in range (1,3):
        pg.draw.line(screen, LINE_COLOR, (i * GRID_SIZE // 3, 0), (i * GRID_SIZE // 3, GRID_SIZE), 7)
        pg.draw.line(screen, LINE_COLOR, (0, i * GRID_SIZE // 3), (GRID_SIZE, i * GRID_SIZE // 3), 7)
    draw_status()

def draw_status():
    """draws the status bar"""
    global is_draw, current_winner
    status_message = f"{current_player}'s Turn" if not current_winner and not is_draw else \
        (f"{current_winner} Wins!" if current_winner else "It's a Draw!")
    status_loca = font.render(status_message, True, LINE_COLOR)
    screen.fill(BACKGROUND, (0, GRID_SIZE, WIDTH, HEIGHT - GRID_SIZE))
    screen.blit(status_loca, (WIDTH // 2 - status_loca.get_width() // 2, GRID_SIZE + 25))
    pg.display.update()


def check_win():
    """checks game grid for wins or draws"""
    global grid, current_winner, is_draw
    for row in range(0, 3):
        if (grid[row][0] == grid[row][1] == grid[row][2]) and (grid[row][0] is not None):
            current_winner = grid[row][0]
            pg.draw.line(screen, (255, 0, 0),
                         (0, (row + 0.5) * GRID_SIZE // 3),
                         (GRID_SIZE, (row + 0.5) * GRID_SIZE // 3), 7)
            break
        
    for col in range(0, 3):
        if (grid[0][col] == grid[1][col] == grid[2][col]) and (grid[0][col] is not None):
            current_winner = grid[0][col]
            pg.draw.line(screen, (255, 0, 0),
                         ((col + 0.5) * GRID_SIZE // 3, 0),
                         ((col + 0.5) * GRID_SIZE // 3, GRID_SIZE), 7)
            break

    if (grid[0][0] == grid[1][1] == grid[2][2]) and (grid[0][0] is not None):
        current_winner = grid[0][0]
        pg.draw.line(screen, (255, 0, 0), (0, 0), (GRID_SIZE, GRID_SIZE), 7)
        
    if (grid[0][2] == grid[1][1] == grid[2][0]) and (grid[0][2] is not None):
        current_winner = grid[0][2]
        pg.draw.line(screen, (255, 0, 0), (GRID_SIZE, 0), (0, GRID_SIZE), 7)

    if (all([all(row) for row in grid]) and current_winner is None):
        is_draw = True
    draw_status()



def drawXO(row, col):
    """draws the X's and O's on the board"""
    global grid, current_player
    x, y = col * GRID_SIZE // 3 + GRID_SIZE // 6, row * GRID_SIZE // 3 + GRID_SIZE // 6
    
    if current_player == 'x':
        pg.draw.line(screen, LINE_COLOR, (x - size, y - size), (x + size, y + size), 5)
        pg.draw.line(screen, LINE_COLOR, (x - size, y + size), (x + size, y - size), 5)
    
    else:
        pg.draw.circle(screen, LINE_COLOR, (x,y), size, 5)

    grid[row][col] = current_player
    current_player = 'O' if current_player == 'X' else 'X'
    pg.display.update()



def user_click():
    """finds the position of the user's click"""
    x,y = pg.mouse.get_pos()
    row, col = y // (GRID_SIZE // 3), x // (GRID_SIZE // 3)
    if (row < 3 and col < 3 and grid[row][col] is None):
        drawXO(row, col)
        check_win()



def reset_game():
    """restarts game on win or draw"""
    global grid, current_winner, current_player, is_draw
    time.sleep(10)
    current_player = 'x'
    current_winner = None
    is_draw = False
    grid = [[None]*3, [None]*3, [None]*3]
    game_initiating_window()

game_initiating_window()

while True: # continue loop until user closes the window
    for event in pg.event.get(): # check for new events
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            user_click()
            if (current_winner or is_draw):
                reset_game()
clock.tick(FPS)




