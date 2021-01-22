from classes import Ship, Fleet, Matrix
import numpy as np


def test_ship_getters():
    ship = Ship(4, [(3, 2), (3, 3), (3, 4), (3, 5)], 'poziom')
    assert ship.get_location() == [(3, 2), (3, 3), (3, 4), (3, 5)]
    assert ship.get_size() == 4
    assert ship.get_direction() == 'poziom'


def test_ship_setters():
    ship = Ship(4, [(3, 2), (3, 3), (3, ), (3, 5)], 'poziom')
    ship.set_location([(2, 5), (2, 6), (2, 7)])
    ship.set_size(3)
    ship.set_direction('pion')
    assert ship.get_location() == [(2, 5), (2, 6), (2, 7)]
    assert ship.get_size() == 3
    assert ship.get_direction() == 'pion'


def test_ship_remove_cord():
    ship = Ship(4, [(3, 2), (3, 3), (3, 4), (3, 5)], 'poziom')
    ship.remove_cord((3, 4))
    assert ship.get_location() == [(3, 2), (3, 3), (3, 5)]


def test_ship_hurt():
    ship = Ship(4, [(3, 2), (3, 3), (3, 4), (3, 5)], 'poziom')
    ship.hurt()
    ship.hurt()
    assert ship.get_size() == 2


def test_fleet_getter():
    ship1 = Ship(4, [(3, 2), (3, 3), (3, 4), (3, 5)], 'poziom')
    ship2 = Ship(3, [(2, 6), (3, 6)], 'pion')
    fleet = Fleet([ship1, ship2])
    assert fleet.get_ships_list() == [ship1, ship2]


def test_fleet_setter():
    ship1 = Ship(4, [(3, 2), (3, 3), (3, 4), (3, 5)], 'poziom')
    ship2 = Ship(3, [(2, 6), (3, 6)], 'pion')
    fleet = Fleet([ship1, ship2])
    ship3 = Ship(3, [(5, 2), (5, 3), (5, 4)], 'poziom')
    ship4 = Ship(2, [(2, 6), (2, 7)], 'poziom')
    fleet.set_ships_list([ship3, ship4])
    assert fleet.get_ships_list() == [ship3, ship4]


def test_fleet_get_ship():
    ship1 = Ship(4, [(3, 2), (3, 3), (3, 4), (3, 5)], 'poziom')
    ship2 = Ship(3, [(2, 6), (3, 6)], 'pion')
    fleet = Fleet([ship1, ship2])
    assert fleet.get_ship((3, 2)) == ship1


def test_fleet_get_list_of_cords():
    ship1 = Ship(4, [(3, 2), (3, 3), (3, 4), (3, 5)], 'poziom',)
    ship2 = Ship(3, [(2, 6), (3, 6)], 'pion')
    fleet = Fleet([ship1, ship2])
    assert fleet.get_list_of_cords() == [[(3, 2), (3, 3),
                                         (3, 4), (3, 5)],
                                         [(2, 6), (3, 6)]]


def test_fleet_remove_ship_from_fleet():
    ship1 = Ship(4, [(3, 2), (3, 3), (3, 4), (3, 5)], 'poziom')
    ship2 = Ship(3, [(2, 6), (3, 6)], 'pion')
    fleet = Fleet([ship1, ship2])
    fleet.remove_ship_from_fleet(ship2)
    assert fleet.get_ships_list() == [ship1]


def test_fleet_fleet_is():
    ship1 = Ship(4, [(3, 2), (3, 3), (3, 4), (3, 5)], 'poziom')
    ship2 = Ship(3, [(2, 6), (3, 6)], 'pion')
    fleet = Fleet([ship1, ship2])
    assert fleet.if_fleet_is()


def test_fleet_fleet_is_not():
    ship1 = Ship(4, [(3, 2), (3, 3), (3, 4), (3, 5)], 'poziom')
    ship2 = Ship(3, [(2, 6), (3, 6)], 'pion')
    fleet = Fleet([ship1, ship2])
    fleet.remove_ship_from_fleet(ship1)
    fleet.remove_ship_from_fleet(ship2)
    assert not fleet.if_fleet_is()


def test_matrix_getter():
    array = np.zeros(10, dtype=int)
    matrix = Matrix(array)
    assert (matrix.get_matrix() == array).all()


def test_matrix_setter():
    array1 = np.zeros(10, dtype=int)
    matrix = Matrix(array1)
    array2 = np.ones(10, dtype=int)
    matrix.set_matrix(array2)
    assert (matrix.get_matrix() == array2).all()


def test_matrix_change_value():
    array = np.zeros((10, 10), dtype=int)
    matrix = Matrix(array)
    matrix.change_element_value((2, 6), 3)
    matrix.change_element_value((3, 5), 2)
    assert matrix.get_matrix()[2, 6] == 3
    assert matrix.get_matrix()[3, 5] == 2
