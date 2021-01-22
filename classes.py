
class Ship:
    '''
    A class to represent a ship

    ...

    Attributes
    ----------
    size : int
        number of ship's element
    location : list
        list of tuples containing cords
    direction : str
        default None
        describes composition of ship
        'pion' or 'poziom
    '''
    def __init__(self, size, location, direction=None):
        self._size = int(size)
        self._direction = direction
        self._location = location

    def get_location(self):
        return self._location

    def set_location(self, new_location):
        self._location = new_location

    def remove_cord(self, cord):
        '''Removes particular cord
            from ship location'''
        self._location.remove(cord)

    def get_size(self):
        return self._size

    def set_size(self, new_size):
        self._size = new_size

    def get_direction(self):
        return self._direction

    def set_direction(self, new_direction):
        self._direction = new_direction

    def hurt(self):
        '''Removes one hp point/size unit'''
        self._size -= 1


class Fleet:
    '''
    A class to represent fleet of ships.

    ...

    Attributes
    ----------
    ships_list : list
        list of Ship class objects
    '''
    def __init__(self, ships_list):
        self._ships_list = ships_list

    def get_ships_list(self):
        return self._ships_list

    def set_ships_list(self, new_list):
        self._ships_list = new_list

    def get_ship(self, cords):
        '''Returns ship which has given cords
            in location'''
        list_of_cords = self.get_list_of_cords()
        for element in list_of_cords:
            if cords in element:
                return self._ships_list[list_of_cords.index(element)]

    def get_list_of_cords(self):
        '''Returns list of whole cords used by fleet'''
        list_of_cords = []
        ships_list = self.get_ships_list()
        for ship in ships_list:
            list_of_cords.append(ship.get_location())
        return list_of_cords

    def remove_ship_from_fleet(self, ship_object):
        '''Removes particular ship from fleet list'''
        self._ships_list.remove(ship_object)

    def if_fleet_is(self):
        '''Checks if fleet has any ships'''
        if self._ships_list:
            return True
        else:
            return False


class Matrix:
    '''
    A class containing matrix/array.

    ...

    Attributes
    ----------
    matrix : array
        numpy array with proper values
        in 0-3 range
        0 - place is empty
        1 - there's a ship's element
        2 - ship's element was drowned
        3 - missed shot

    '''
    def __init__(self, matrix):
        self._matrix = matrix

    def get_matrix(self):
        return self._matrix

    def set_matrix(self, new_matrix):
        self._matrix = new_matrix

    def change_element_value(self, cord, value):
        '''Changes value of cord in matrix for
            given value'''
        first, second = cord[0], cord[1]
        self._matrix[first, second] = value
