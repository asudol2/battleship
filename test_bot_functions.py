from bot_functions import *
import numpy as np

def test_first_bot_shoot():
    array = np.zeros((10,10), dtype=int)
    array[2, 7] = 1
    array[0, 5] = 1
    array[4, 7] = 1
    f_cord, s_cord = first_bot_shoot(array)
    assert f_cord in range(10)
    assert s_cord in range(10)

def test_check_possibility_of_shoot():
    array = np.zeros((10, 10), dtype = int)
    cords = (2, 5)
    additional_cords_list = [(2, 4), (2, 6), (1, 5),
    (3, 5), (2, 5), (2, 7), (2,2)]
    array[2, 4] = 1
    array[2, 3] = 1
    array[2, 7] = 1
    list_of_shot_cords = [(2, 4), (2, 3)]
    given_list = check_possibility_of_shoot(additional_cords_list,
    array, list_of_shot_cords)
    assert len(given_list) == 6

def test_check_first_shoot():
    array = np.zeros((10, 10), dtype=int)
    cords_list = [(2, 4), (2, 6), (1, 5),
    (3, 5), (2, 5), (2, 7), (2,2), (2, 3)]
    for cords in cords_list:
        f, s = cords
        array[f, s] = 2
    cords = (4, 9)
    assert check_first_shoot(array, cords)

def test_check_first_shoot_2():
    array = np.zeros((10, 10), dtype=int)
    cords_list = [(2, 4), (2, 6), (1, 5),
    (3, 5), (2, 5), (2, 7), (2,2), (2, 3)]
    for cords in cords_list:
        f, s = cords
        array[f, s] = 1
    cords = (3, 6)
    assert check_first_shoot(array, cords)

def test_check_if_score_true():
    array = np.zeros((10, 10), dtype=int)
    cords_list = [(2, 4), (2, 6), (1, 5),
    (3, 5), (2, 5), (2, 7), (2,2), (2, 3)]
    for cords in cords_list:
        f, s = cords
        array[f, s] = 1
    assert check_if_score(array, (2, 4))

def test_check_if_score_false():
    array = np.zeros((10, 10), dtype=int)
    cords_list = [(2, 4), (2, 6), (1, 5),
    (3, 5), (2, 5), (2, 7), (2,2), (2, 3)]
    for cords in cords_list:
        f, s = cords
        array[f, s] = 1
    assert not check_if_score(array, (7, 8))

def test_check_direction_and_turn_one():
    f_cords = (2, 6)
    s_cords = (2, 7)
    direction, turn = check_direction_and_turn(f_cords, s_cords)
    assert direction == 'poziom'
    assert turn == 'prawo'

def test_check_direction_and_turn_two():
    f_cords = (2, 7)
    s_cords = (2, 6)
    direction, turn = check_direction_and_turn(f_cords, s_cords)
    assert direction == 'poziom'
    assert turn == 'lewo'

def test_check_direction_and_turn_three():
    f_cords = (2, 6)
    s_cords = (3, 6)
    direction, turn = check_direction_and_turn(f_cords, s_cords)
    assert direction == 'pion'
    assert turn == 'dół'

def test_check_direction_and_turn_four():
    f_cords = (2, 6)
    s_cords = (1, 6)
    direction, turn = check_direction_and_turn(f_cords, s_cords)
    assert direction == 'pion'
    assert turn == 'góra'

