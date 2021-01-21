
class Ship:
    '''Tworzy statki o atrybutach size, direction,
    location(lista krotek/koordynatów)'''
    def __init__(self, size, direction=None, location):
        self._size = int(size)
        self._direction = direction
        self._location = location

    def get_location(self):
        return self._location

    def set_location(self, new_location):
        self._location = new_location

    def remove_cord(self, cord):
        '''Usuwa dany koordynat z listy koordynatów statku'''
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
        '''Odejmuje jeden punkt życia/jedną jednostkę z size'''
        self._size -= 1


class Fleet:
    '''Przechowuje listę obiektów klasy Ship '''
    def __init__(self, ships_list):
        self._ships_list = ships_list

    def get_ships_list(self):
        return self._ships_list

    def set_ships_list(self, new_list):
        self._ships_list = new_list

    def get_ship(self, cords):
        '''Zwraca statek znajdujący się na danych koordynatach.;
        *ISTOTNE* Kwestia, czy statek jest we flocie musi
        zostać uprzednio sprawdzona!'''
        list_of_cords = self.get_list_of_cords()
        for element in list_of_cords:
            if cords in element:
                return self._ships_list[list_of_cords.index(element)]

    def get_list_of_cords(self):
        '''Zwraca listę wszystkich koordynatów, gdzie znajdują się statki'''
        list_of_cords = []
        ships_list = self.get_ships_list()
        for ship in ships_list:
            list_of_cords.append(ship.get_location())
        return list_of_cords

    def remove_ship_from_fleet(self, ship_object):
        self._ships_list.remove(ship_object)

    def if_fleet_is(self):
        if self._ships_list:
            return True
        else:
            return False


class Matrix:
    '''Przetrzymuje dane o tablicy 01'''
    def __init__(self, matrix):
        self._matrix = matrix

    def get_matrix(self):
        return self._matrix

    def set_matrix(self, new_matrix):
        self._matrix = new_matrix

    def change_element_value(self, cord, value):
        '''Zmienia wartość pola o podanych koordynatach na daną wartość'''
        first, second = cord[0], cord[1]
        self._matrix[first, second] = value
