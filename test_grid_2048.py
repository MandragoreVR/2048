from grid_2048 import *
from random import *
import coverage 



def test_create_grid():
    assert create_grid(4) == [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '],
                             [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]


def test_grid_add_new_tile_at_position():
    game_grid=create_grid(4)
    game_grid=add_new_tile(game_grid,[1,1])
    assert game_grid in [[[' ',' ',' ', ' '],[' ', 2 ,' ', ' '],[' ',' ',' ', ' '],[' ',' ',' ', ' ']],[[' ',' ',' ', ' '],[' ', 4 ,' ', ' '],[' ',' ',' ', ' '],[' ',' ',' ', ' ']]]

test_grid_add_new_tile_at_position()

def test_get_value_new_tile():
    for i in range(10):
        assert get_value_new_tile() in {2, 4}

def test_get_empty_tiles_positions():
    assert get_empty_tiles_positions([[0, 16, 32, 0], [64, 0, 32, 2], [2, 2, 8, 4], [512, 8, 16, 0]])==[(0,0),(0,3),(1,1),(3,3)]
    assert get_empty_tiles_positions([[' ', 16, 32, 0], [64, 0, 32, 2], [2, 2, 8, 4], [512, 8, 16, 0]])==[(0,0),(0,3),(1,1),(3,3)]
    assert get_empty_tiles_positions(create_grid(2))==[(0,0),(0,1),(1,0),(1,1)]
    assert get_empty_tiles_positions([[16,4,8,2], [2,4,2,128], [4,512,32,64], [1024,2048,512,2]])==[]
def test_get_new_position():
    grid = [[0, 16, 32, 0], [64, 0, 32, 2], [2, 2, 8, 4], [512, 8, 16, 0]]
    x,y=position_de_new_tile(grid)
    assert(grid[x][y]) == 0
    grid = [[' ',4,8,2], [' ',' ',' ',' '], [' ',512,32,64], [1024,2048,512, ' ']]
    x,y=position_de_new_tile(grid)
    assert(grid[x][y]) == ' '


