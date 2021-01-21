from matrix_generation import *
import numpy as np
from classes import Ship


def test_generate_empty_matrix():
    array = np.zeros((10,10), dtype=int)
    assert (generate_empty_matrix() == array).all()

def test_create_cords():
    cords = create_random_cords()
    f_cord, s_cord = cords
    assert f_cord in range(10)
    assert s_cord in range(10)

def test_choose_direction():
    direction = choose_direction()
    assert direction in ['pion', 'poziom']

def test_make_list_of_ships():
    info1 = [4, 'poziom', [(3,2), (3,3), (3,4), (3,5)]]
    info2 = [3, 'pion', [(2,6), (3,6)]]
    list_of_infos = [info1, info2]
    list_of_ships = make_list_of_ships(list_of_infos)
    ship = list_of_ships[1]
    assert isinstance(ship, Ship)

def test_make_empty_board():
    board = make_empty_board()
    assert board[0, 4] == 'D'
    assert board[0, 0] == ' O'
    assert board[5, 0] == ' 5'
    assert board[2, 6] == ' '

def test_show_actual_board_not_bot():
    array = np.zeros((10,10), dtype=int)
    array[2, 6] = 1
    array[3, 6] = 2
    array[4, 6] = 3
    board = show_actual_board(array)
    assert board[3, 7] == '□'
    assert board[4, 7] == '⊠'
    assert board[5, 7] == '○'
    assert board[2, 6] == ' '

def test_check_if_possible_true():
    array = np.zeros((10,10), dtype=int)
    direction = 'poziom'
    size = 4
    cords = (2, 5)
    assert check_if_possible(array, cords, direction, size)

def test_check_if_possible_false_one():
    array = np.zeros((10,10), dtype=int)
    direction = 'poziom'
    size = 4
    cords = (2, 5)
    array[2, 8] = 1
    assert not check_if_possible(array, cords, direction, size)

def test_check_if_possible_false_two():
    array = np.zeros((10,10), dtype=int)
    direction = 'pion'
    size = 4
    cords = (2, 5)
    array[1, 6] = 1
    assert not check_if_possible(array, cords, direction, size)

def test_check_if_making_is_possible_false_one():
    array = np.zeros((10,10), dtype=int)
    direction = 'pion'
    size = 4
    cords = (2, 5)
    array[1, 6] = 1
    assert not check_if_making_is_possible(size, cords, array, direction)

def test_check_if_making_is_possible_false_two():
    array = np.zeros((10,10), dtype=int)
    direction = 'poziom'
    size = 2
    cords = (2, 5)
    array[3, 7] = 1
    assert not check_if_making_is_possible(size, cords, array, direction)

def test_check_if_making_is_possible_false_three():
    array = np.zeros((10,10), dtype=int)
    size = 1
    cords = (2, 5)
    array[1, 6] = 1
    assert not check_if_making_is_possible(size, cords, array)

def test_check_if_making_is_possible_true_one():
    array = np.zeros((10,10), dtype=int)
    direction = 'poziom'
    size = 2
    cords = (2, 5)
    array[2, 8] = 1
    assert check_if_making_is_possible(size, cords, array, direction)

def test_check_if_making_is_possible_true_two():
    array = np.zeros((10,10), dtype=int)
    direction = 'pion'
    size = 4
    cords = (2, 5)
    array[0, 5] = 1
    array[7, 5] = 1
    array[2, 7] = 1
    assert check_if_making_is_possible(size, cords, array, direction)

def test_check_if_making_is_possible_true_three():
    array = np.zeros((10,10), dtype=int)
    size = 1
    cords = (2, 5)
    array[2, 7] = 1
    array[0, 5] = 1
    array[4, 7] = 1
    assert check_if_making_is_possible(size, cords, array)
