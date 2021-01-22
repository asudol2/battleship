import numpy as np
from random import randint, choice
from classes import Ship, Fleet, Matrix
from math import isqrt


def generate_empty_matrix(dim):
    '''
    Creates empty array of given dimension
    '''
    return np.zeros((dim, dim), dtype=int)


def create_random_cords(dim):
    '''
    Draws random cords from given range
    '''
    return (randint(0, dim-1), randint(0, dim-1))


def choose_direction():
    '''
    Draws direction of shoot
    '''
    return choice(['poziom', 'pion'])


def get_basic_info():
    '''
    Gets info about number of ships
    and dimension of board
    '''
    eh = True
    while eh:
        print('Ilość kadłubów największego statku powinna zawierać się')
        print('w przedziale od 1 do 5')
        big = input('Podaj ile kadłubów ma mieć największy statek.   ')
        if not big.isdigit():
            print('Podałeś złe dane. ')
        else:
            big = int(big)
            if big not in range(1, 6):
                print('Podałeś złe dane. ')
            else:
                eh = False
    eh = True
    m_dim = count_minimal_dimension(big)
    while eh:
        print(f'Wymiary planszy to co najmniej {m_dim}x{m_dim}. ')
        print('Największy dopuszczalny wymiar to 16')
        dim = input('Jakie wymiary ma mieć plansza? (Podaj długość boku)')
        if not dim.isdigit():
            print('Podałeś złe dane. ')
        else:
            dim = int(dim)
            if dim not in range(m_dim, 17):
                print('Podałeś złe dane. ')
            else:
                eh = False
        sizes_list = count_list_of_sizes(big)
        sizes_list.reverse()
    return dim, sizes_list


def count_list_of_sizes(big):
    '''
    Prepares list of ships' sizes
    '''
    list_of_sizes = []
    mom = 1
    while big > 0:
        temp = 1
        while temp <= big:
            list_of_sizes.append(mom)
            temp += 1
        big -= 1
        mom += 1
    return list_of_sizes


def count_minimal_dimension(big):
    '''
    Calculate minimal needed dimension
    '''
    x = big
    ins = int(x*(x**2 + 6*x + 5)/3)
    min_dim = isqrt(ins) + 1
    return min_dim


def generate_computer_matrix(list_of_sizes, dim):
    '''
    Creates matrix and fleet for bot.
    '''
    matrix = generate_empty_matrix(dim)
    list_of_infos = []
    for size in list_of_sizes:
        list_of_cords = []
        check = False
        while not check:
            cords = create_random_cords(dim)
            direction = choose_direction()
            check = check_if_making_is_possible(size, cords,
                                                matrix, dim,
                                                direction)
            if check:
                first, second = cords[0], cords[1]
                if direction == 'poziom':
                    for number in range(size):
                        matrix[first, second + number] = 1
                        list_of_cords.append((first, second+number))
                if direction == 'pion':
                    for number in range(size):
                        matrix[first + number, second] = 1
                        list_of_cords.append((first + number, second))
                list_of_infos.append((size, list_of_cords, direction))
    Bot_Matrix = Matrix(matrix)
    Bot_Fleet = Fleet(make_list_of_ships(list_of_infos))
    return Bot_Matrix, Bot_Fleet


def make_player_matrix(list_of_sizes, dim):
    '''
    Conducts creating player's matrix and fleet
    '''
    list_of_infos = []
    matrix = np.zeros((dim, dim), dtype=int)
    print(make_empty_board(dim))
    while list_of_sizes:
        size = list_of_sizes[0]
        direction, location = get_info_about_ship(size, matrix, dim)
        for cord in location:
            first, second = cord
            matrix[first, second] = 1
        list_of_infos.append((size, location, direction))
        list_of_sizes.pop(0)
        print(show_actual_board(matrix, dim))
    Player_Matrix = Matrix(matrix)
    Player_Fleet = Fleet(make_list_of_ships(list_of_infos))
    print('Twoja finalna tablica')
    return Player_Matrix, Player_Fleet


def make_empty_board(dim):
    '''
    Creates empty pattern of visible board
    '''
    board = np.zeros((dim+1, dim+1), dtype=object)
    start = 0
    for row in board:
        for column in row:
            row[start] = ' '
            start += 1
        start = 0
    hlp = 0
    while hlp <= dim:
        if hlp < 10:
            temp = ' ' + str(hlp)
            board[hlp, 0] = temp
        else:
            board[hlp, 0] = str(hlp)
        hlp += 1
    letters = dictionary()
    hlp = 0
    while hlp <= dim:
        board[0, hlp] = letters[str(hlp)]
        hlp += 1
    return board


def show_actual_board(matrix, dim, is_bot=False):
    '''
    Returns actual board (with signs
    of ship, sinked and missed)
    '''
    board = make_empty_board(dim)
    r_index = 0
    for row in matrix:
        r_index += 1
        c_index = 0
        for column in row:
            c_index += 1
            if column == 1:
                if not is_bot:
                    board[r_index, c_index] = '□'
            if column == 2:
                board[r_index, c_index] = '⊠'
            if column == 3:
                board[r_index, c_index] = '○'
    return board


def get_info_about_ship(size, matrix, dim):
    '''
    Collects info about ship from player.
    Asks for ship's direction and location
    Returns directions and location (list of cords).
    '''
    direction = None
    print(f'Tworzysz {size}-masztowiec.')
    check = False
    if size != 1:
        direction = ask_for_direction()
        if direction == 'poziom':
            composition = 'prawo'
        else:
            composition = 'dół'
        while not check:
            print('Gdzie znajdzie się ten statek?')
            print('Podaj koordynat, od którego będzie budowany statek')
            print(f'UWAGA! Następnie statek będzie budowany w {composition}')
            location = []
            check, first, second = get_and_check_cords(size, matrix,
                                                       dim,
                                                       direction)
            cords = (first, second)
            if not check:
                wrong_cords()
        else:
            location.append(cords)
            while size > 1:
                if direction == 'poziom':
                    second += 1
                    location.append((first, second))
                if direction == 'pion':
                    first += 1
                    location.append((first, second))
                size -= 1
    else:
        while not check:
            print('Gdzie znajdzie się ten statek?')
            print('Podaj koordynaty statku.')
            location = []
            check, first, second = get_and_check_cords(1, matrix,
                                                       dim)
            if not check:
                wrong_cords()
            location = [(first, second)]
    return direction, location


def wrong_cords():
    '''
    Print info about wrong cords
    '''
    print('Podane koordynaty są nieodpowiednie.')
    print('Podaj poprawne dane.')


def get_and_check_cords(size, matrix, dim, direction=None):
    '''
    Condutcs getting cords. If are correct, returns
    True and cords, else False and cords.
    '''
    first, second = ask_for_cords(dim)
    cords = (first, second)
    check = check_if_making_is_possible(size, cords,
                                        matrix, dim,
                                        direction)
    return check, first, second


def ask_for_direction():
    '''
    Asks player about direction of creating ship
    '''
    print('Jeżeli ma być ustawiony poziomo, podaj poziom.')
    print('Jeżeli ma być ustawiony pionowo, podaj pion.')
    print('Zależnie od wyboru, będzie on rysowany w prawo lub w dół.')
    meanwhile = False
    little_list = ['poziom', 'pion']
    while not meanwhile:
        direction = input('Wpisz kierunek.   ')
        if direction in little_list:
            meanwhile = True
            return direction
        else:
            print('Podany został zły argument. Podaj poprawne słowo.')


def ask_for_cords(dim):
    '''
    Collects data about first cords of ships.
    '''
    changers = rev_dictionary()
    list_of_keys = [key for key in changers]
    meanwhile = False
    while not meanwhile:
        row = input(f'Podaj wiersz od 1 do {dim}.   ')
        if row.isdigit():
            if int(row) in range(1, dim+1):
                temp_dict = dictionary()
                last = temp_dict[str(dim)]
                given = input(f'Podaj kolumnę od A do {last}.   ')
                column = given.upper()
                if column in list_of_keys:
                    second = changers[column] - 1
                    first = int(row) - 1
                    meanwhile = True
                    return first, second
                else:
                    print('Zły argument. Podaj poprawne wielkości.')
            else:
                print('Został podany zły argument. Podaj poprawne wielkości.')
        else:
            print('Został podany zły argument. Podaj poprawne wielkości.')


def make_list_of_ships(list_of_infos):
    '''
    Creates and returns list of ships
    to make fleet (list of ships is basic
    fleet object attribute).
    '''
    list_of_ships = []
    infos = list_of_infos
    i = 0
    for items in infos:
        ship = Ship(infos[i][0], infos[i][1], infos[i][2])
        list_of_ships.append(ship)
        i += 1
    return list_of_ships


def check_if_making_is_possible(size, cords,  matrix, dim, direction=None):
    '''
    Checks if it's possible to place ship in given place
    (basing on actual matrix)
    If it's possible, returns True,
    else returns False.
    '''
    list_of_cords = []
    to_remove = []
    if direction == 'poziom':
        m_cords = (cords[0], cords[1] + size - 1)
    elif direction == 'pion':
        m_cords = ((cords[0] + size - 1), cords[1])
    else:
        m_cords = cords
    if (not m_cords[0] in range(dim)) or (not m_cords[1] in range(dim)):
        return False
    for number in range(-1, size + 1):
        if direction == 'poziom':
            list_of_cords.append((cords[0], cords[1] + number))
            list_of_cords.append((cords[0] + 1, cords[1] + number))
            list_of_cords.append((cords[0] - 1, cords[1] + number))
        elif direction == 'pion':
            list_of_cords.append((cords[0] + number, cords[1]))
            list_of_cords.append((cords[0] + number, cords[1] - 1))
            list_of_cords.append((cords[0] + number, cords[1] + 1))
        else:
            list_of_cords.append((cords[0], cords[1] + number))
            list_of_cords.append((cords[0] + 1, cords[1] + number))
            list_of_cords.append((cords[0] - 1, cords[1] + number))
    for loc in list_of_cords:
        if not loc[0] in range(dim) or not loc[1] in range(dim):
            to_remove.append(loc)
    for sth in to_remove:
        if sth in list_of_cords:
            list_of_cords.remove(sth)
    for place in list_of_cords:
        if matrix[place[0], place[1]] == 1:
            return False
    return True


def dictionary():
    '''
    Dict of replecable values
    for use of other functions.
    '''
    letters = {
        '0': ' 0',
        '1': 'A',
        '2': 'B',
        '3': 'C',
        '4': 'D',
        '5': 'E',
        '6': 'F',
        '7': 'G',
        '8': 'H',
        '9': 'I',
        '10': 'J',
        '11': 'K',
        '12': 'L',
        '13': 'M',
        '14': 'N',
        '15': 'O',
        '16': 'P',
        '17': 'Q',
    }
    return letters


def rev_dictionary():
    '''
    Reversed dict of values
    for use of other functions
    '''
    letters = dictionary()
    letters['0'] = '0'
    rev_letters = {v: int(k) for k, v in letters.items()}
    return rev_letters
