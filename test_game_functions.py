from game_functions import (
    check_if_ship_is,
    check_if_ship_is_drowned
)
import numpy as np


def test_check_if_ship_is_true():
    array = np.zeros((10, 10), dtype=int)
    cords_list = [(2, 4), (2, 6), (1, 5),
                  (3, 5), (2, 5), (2, 7), (2, 2), (2, 3)]
    for cords in cords_list:
        f, s = cords
        array[f, s] = 1
    cords = (3, 5)
    assert check_if_ship_is(cords, array)


def test_check_if_ship_is_false():
    array = np.zeros((10, 10), dtype=int)
    cords_list = [(2, 4), (2, 6), (1, 5),
                  (3, 5), (2, 5), (2, 7), (2, 2), (2, 3)]
    for cords in cords_list:
        f, s = cords
        array[f, s] = 1
    cords = (6, 6)
    assert not check_if_ship_is(cords, array)


def test_check_if_ship_is_drowned_true():
    array = np.zeros((10, 10), dtype=int)
    cords_list = [(2, 4), (2, 6), (1, 5),
                  (3, 5), (2, 5), (2, 7), (2, 2), (2, 3)]
    for cords in cords_list:
        f, s = cords
        array[f, s] = 2
    cords = (2, 5)
    assert check_if_ship_is_drowned(cords, array)


def test_check_if_ship_is_drowned_false():
    array = np.zeros((10, 10), dtype=int)
    cords_list = [(2, 4), (2, 6), (1, 5),
                  (3, 5), (2, 5), (2, 7), (2, 2), (2, 3)]
    for cords in cords_list:
        f, s = cords
        array[f, s] = 1
    cords = (8, 8)
    assert not check_if_ship_is_drowned(cords, array)
