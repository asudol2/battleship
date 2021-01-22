from bot_functions import (
    hit,
    f_continue,
    sinked,
    missed,
    check_if_score,
    check_direction_and_turn,
    check_first_shoot
)
import numpy as np
from classes import Matrix, Fleet, Ship


def test_check_if_score_true():
    array = np.zeros((10, 10), dtype=int)
    cords_list = [(2, 4), (2, 6), (1, 5),
                  (3, 5), (2, 5), (2, 7), (2, 2), (2, 3)]
    for cords in cords_list:
        f, s = cords
        array[f, s] = 1
    assert check_if_score(array, (2, 4))


def test_check_if_score_false():
    array = np.zeros((10, 10), dtype=int)
    cords_list = [(2, 4), (2, 6), (1, 5),
                  (3, 5), (2, 5), (2, 7), (2, 2), (2, 3)]
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


def test_check_first_shoot_true():
    dim = 8
    matrix = np.zeros((dim, dim), dtype=int)
    cords = (7, 7)
    assert check_first_shoot(matrix, cords, dim)


def test_check_first_shoot_false():
    dim = 8
    matrix = np.zeros((dim, dim), dtype=int)
    cords = (7, 7)
    matrix[6, 7] = 2
    assert not check_first_shoot(matrix, cords, dim)


def test_missed1():
    dim = 8
    matrix = np.zeros((dim, dim), dtype=int)
    obj = Matrix(matrix)
    matrix[2, 6] = 2
    cords = (2, 6)
    new = missed(obj, cords).get_matrix()
    assert (new == matrix).all()


def test_hit():
    dim = 8
    matrix = np.zeros((dim, dim), dtype=int)
    m_obj = Matrix(matrix)
    ship1 = Ship(4, [(3, 2), (3, 3), (3, 4), (3, 5)], 'poziom')
    size = ship1.get_size()
    ship2 = Ship(3, [(2, 6)], 'pion')
    fleet = Fleet([ship1, ship2])
    cords = (3, 2)
    lifes, m_obj, fleet = hit(m_obj, cords, fleet, dim)
    assert lifes < size


def test_sinked():
    ship1 = Ship(4, [(3, 2), (3, 3), (3, 4), (3, 5)], 'poziom')
    ship2 = Ship(3, [(2, 6)], 'pion')
    fleet = Fleet([ship1, ship2])
    cords = (2, 6)
    fleet = sinked(fleet, cords)
    assert not fleet.get_ship(cords)


def test_f_continue():
    ship1 = Ship(4, [(3, 2), (3, 3), (3, 4), (3, 5)], 'poziom')
    ship2 = Ship(1, [(2, 6)], 'pion')
    fleet = Fleet([ship1, ship2])
    cords = (2, 6)
    shot_list = [(2, 2)]
    shot_list, fleet_object = f_continue(fleet, cords, shot_list)
    assert shot_list[1] == cords
