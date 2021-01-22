from matrix_generation import (
    count_minimal_dimension,
    count_list_of_sizes,
    check_if_making_is_possible,
    show_actual_board,
    make_empty_board,
    choose_direction,
    make_list_of_ships,
    create_random_cords,
    generate_empty_matrix
)
import numpy as np
from classes import Ship


def test_generate_empty_matrix1():
    array = np.zeros((10, 10), dtype=int)
    assert (generate_empty_matrix(10) == array).all()


def test_generate_empty_matrix2():
    array = np.zeros((3, 3), dtype=int)
    assert (generate_empty_matrix(3) == array).all()


def test_create_cords1():
    cords = create_random_cords(12)
    f_cord, s_cord = cords
    assert f_cord in range(12)
    assert s_cord in range(12)


def test_create_cords2():
    dim = 16
    cords = create_random_cords(dim)
    f_cord, s_cord = cords
    assert f_cord in range(dim)
    assert s_cord in range(dim)


def test_choose_direction():
    direction = choose_direction()
    assert direction in ['pion', 'poziom']


def test_make_list_of_ships():
    info1 = [4, 'poziom', [(3, 2), (3, 3), (3, 4), (3, 5)]]
    info2 = [3, 'pion', [(2, 6), (3, 6)]]
    list_of_infos = [info1, info2]
    list_of_ships = make_list_of_ships(list_of_infos)
    ship = list_of_ships[1]
    assert isinstance(ship, Ship)


def test_make_empty_board():
    board = make_empty_board(7)
    assert board[0, 4] == 'D'
    assert board[0, 0] == ' 0'
    assert board[5, 0] == ' 5'
    assert board[2, 6] == ' '


def test_show_actual_board_not_bot():
    dim = 12
    array = np.zeros((dim, dim), dtype=int)
    array[2, 6] = 1
    array[3, 6] = 2
    array[4, 6] = 3
    board = show_actual_board(array, dim)
    assert board[3, 7] == '□'
    assert board[4, 7] == '⊠'
    assert board[5, 7] == '○'
    assert board[2, 6] == ' '


def test_check_if_making_is_possible_false_one():
    dim = 8
    array = np.zeros((dim, dim), dtype=int)
    direction = 'pion'
    size = 4
    cords = (2, 5)
    array[1, 6] = 1
    assert not check_if_making_is_possible(size, cords, array, dim, direction)


def test_check_if_making_is_possible_false_two():
    array = np.zeros((10, 10), dtype=int)
    direction = 'poziom'
    size = 2
    cords = (2, 5)
    array[3, 7] = 1
    assert not check_if_making_is_possible(size, cords, array, 10, direction)


def test_check_if_making_is_possible_false_three():
    array = np.zeros((10, 10), dtype=int)
    size = 1
    cords = (2, 5)
    array[1, 6] = 1
    assert not check_if_making_is_possible(size, cords, array, 10)


def test_check_if_making_is_possible_true_one():
    dim = 16
    array = np.zeros((dim, dim), dtype=int)
    direction = 'poziom'
    size = 2
    cords = (2, 5)
    array[2, 8] = 1
    assert check_if_making_is_possible(size, cords, array, dim, direction)


def test_check_if_making_is_possible_true_two():
    dim = 8
    array = np.zeros((dim, dim), dtype=int)
    direction = 'pion'
    size = 4
    cords = (2, 5)
    array[0, 5] = 1
    array[7, 5] = 1
    array[2, 7] = 1
    assert check_if_making_is_possible(size, cords, array, dim, direction)


def test_check_if_making_is_possible_true_three():
    array = np.zeros((10, 10), dtype=int)
    size = 1
    cords = (2, 5)
    array[2, 7] = 1
    array[0, 5] = 1
    array[4, 7] = 1
    assert check_if_making_is_possible(size, cords, array, 10)


def test_count_list_of_sizes1():
    tmp_list = count_list_of_sizes(5)
    assert len(tmp_list) == 15
    assert tmp_list == [1, 1, 1, 1, 1, 2, 2,
                        2, 2, 3, 3, 3, 4, 4, 5]


def test_count_list_of_sizes2():
    tmp_list = count_list_of_sizes(4)
    assert len(tmp_list) == 10
    assert tmp_list == [1, 1, 1, 1, 2, 2,
                        2, 3, 3, 4]


def test_count_list_of_sizes3():
    tmp_list = count_list_of_sizes(6)
    assert len(tmp_list) == 21


def test_count_minimal_dimension1():
    ans = count_minimal_dimension(5)
    assert ans == 11
