import numpy as np
from random import randint, choice
from classes import Ship, Fleet, Matrix
from time import sleep


def generate_empty_matrix():
    return np.zeros((10, 10), dtype=int)


def create_random_cords():
    '''Losuje przypadkowe koordynaty w zakresie 0-9'''
    return (randint(0, 9), randint(0, 9))


def choose_direction():
    '''Losuje kierunek ustawienia statku'''
    return choice(['poziom', 'pion'])


def check_if_possible(actual_matrix, cords, direction, size):
    '''Dla bota;
    Sprawdza czy możliwe jest dane ustawienie statku/strzelenie ma sens'''
    matrix = actual_matrix
    f, s = cords[0], cords[1]
    for el in range(-1, 2):
        for nu in range(-1, size+1):
            if direction == 'poziom':
                if (f+el) in range(10) and (s+nu) in range(10):
                    if matrix[f+el, s+nu] != 0:
                        return False
                else:
                    return False
            elif direction == 'pion':
                if (f+nu) in range(10) and (s+el) in range(10):
                    if matrix[f+nu, s+el] != 0:
                        return False
                else:
                    return False
    return True



def generate_computer_matrix():
    '''Tworzy macierz i flotę dla bota'''
    matrix = generate_empty_matrix()
    list_of_sizes = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    list_of_infos = []
    for size in list_of_sizes:
        list_of_cords = []
        check = False
        while not check:
            cords = create_random_cords()
            direction = choose_direction()
            check = check_if_possible(matrix, cords, direction, size)
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
                list_of_infos.append((size, direction, list_of_cords))
    Bot_Matrix = Matrix(matrix)
    Bot_Fleet = Fleet(make_list_of_ships(list_of_infos))
    return Bot_Matrix, Bot_Fleet


def make_player_matrix():
    '''DLA GRACZA: Najpierw generuje macierz zer (tą dla komputera),
    potem zmienia je na jedynki w miejscach, gdzie występuje statek.; '''
    list_of_sizes = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    list_of_infos = []
    matrix = np.zeros((10, 10), dtype=int)
    print(make_empty_board())
    while list_of_sizes:
        size = list_of_sizes[0]
        direction, location = get_info_about_ship(size, matrix)
        for cord in location:
            first, second = cord
            matrix[first, second] = 1
        list_of_infos.append((size, direction, location))
        list_of_sizes.pop(0)
        print(show_actual_board(matrix))
    Player_Matrix = Matrix(matrix)
    Player_Fleet = Fleet(make_list_of_ships(list_of_infos))
    print('Twoja finalna tablica')
    return Player_Matrix, Player_Fleet


def make_empty_board():
    '''Tworzy pusty szablon planszy widocznej planszy '''
    board = np.zeros((11, 11), dtype=object)
    start = 0
    for row in board:
        for column in row:
            row[start] = ' '
            start += 1
        start = 0
    board[:, 0] = [' 0', ' 1', ' 2', ' 3', ' 4', ' 5',
    ' 6', ' 7', ' 8', ' 9', '10']
    board[0] = [' O', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J']
    return board


def show_actual_board(matrix, is_bot=False):
    '''Zwraca aktualną planszę'''
    board = make_empty_board()
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


def get_info_about_ship(size, matrix):
    '''Zbiera informacje na temat statku, przy czym rozmiar będzie
    podawany jako argument z listy w funkcji make_player_matrix()ISTOTNE:
    zakładamy, że gracz poprawnie wprowadza statki;
    do ewentualnej zmiany później'''
    direction = None
    print(f'Tworzysz {size}-masztowiec.')
    sleep(1.)
    check = False
    if size != 1:
        direction = ask_for_direction()
        if direction == 'poziom':
            composition = 'prawo'
        if direction == 'pion':
            composition = 'dół'
        while not check:
            print('Gdzie znajdzie się ten statek?')
            sleep(1.)
            print('Podaj początkowy koordynat, od którego będzie budowany statek')
            sleep(1.)
            print(f'UWAGA! W następnych krokach statek będzie budowany w {composition}')
            location = []
            first, second = ask_for_cords()
            cords = (first, second)
            check = check_if_making_is_possible(size, cords, matrix, direction)
            if not check:
                print('Podane koordynaty są nieodpowiednie.')
                print('Podaj poprawne dane.')
                sleep(1.)
            location.append((first, second))
        else:
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
            sleep(1.)
            print('Podaj koordynaty statku.')
            location = []
            first, second = ask_for_cords()
            cords = (first, second)
            check = check_if_making_is_possible(1, cords, matrix)
            if not check:
                print('Podane koordynaty są nieodpowiednie.')
                print('Podaj poprawne dane.')
            location = [(first, second)]
    return direction, location


def ask_for_direction():
    '''Zbiera dane nt. ustawienia statku'''
    sleep(1.)
    print('Jeżeli ma być ustawiony poziomo, podaj poziom.')
    sleep(1.)
    print('Jeżeli ma być ustawiony pionowo, podaj pion.')
    sleep(1.)
    print('Zależnie od wyboru, będzie on rysowany w prawo lub w dół.')
    meanwhile = False
    little_list = ['poziom', 'pion']
    while not meanwhile:
        direction = get_input('Wpisz kierunek.   ')
        if direction in little_list:
            meanwhile = True
            return direction
        else:
            sleep(1.)
            print('Podany został zły argument. Podaj poprawne słowo.')


def ask_for_cords():
    '''Zbiera dane nt. koordynatów pierwszego elementu statku'''
    dict_of_changers = {
        'A': 0,
        'B': 1,
        'C': 2,
        'D': 3,
        'E': 4,
        'F': 5,
        'G': 6,
        'H': 7,
        'I': 8,
        'J': 9}
    list_of_keys = [key for key in dict_of_changers]
    meanwhile = False
    while not meanwhile:
        sleep(1.)
        row = get_input('Podaj wiersz od 1 do 10.   ')
        sleep(1.)
        if row.isdigit():
            if int(row) in range(1, 11):
                given = get_input('Podaj kolumnę od A do J.   ')
                column = given.upper()
                if column in list_of_keys:
                    second = dict_of_changers[column]
                    first = int(row) - 1
                    meanwhile = True
                    return first, second
                else:
                    sleep(1.)
                    print('Został podany zły argument. Podaj poprawne wielkości.')
            else:
                sleep(1.)
                print('Został podany zły argument. Podaj poprawne wielkości.')
        else:
            sleep(1.)
            print('Został podany zły argument. Podaj poprawne wielkości.')


def make_list_of_ships(list_of_infos):
    '''Tworzy i zwraca obiekt klasy Fleet korzystając z listy
    informacji o statkach'''
    list_of_ships = []
    infos = list_of_infos
    for items in infos:
        ship = Ship(infos[0][0], infos[0][1], infos[0][2])
        list_of_ships.append(ship)
    # FourMast = Ship(infos[0][0], infos[0][1], infos[0][2])
    # ThreeMast1 = Ship(infos[1][0], infos[1][1], infos[1][2])
    # ThreeMast2 = Ship(infos[2][0], infos[2][1], infos[2][2])
    # TwoMast1 = Ship(infos[3][0], infos[3][1], infos[3][2])
    # TwoMast2 = Ship(infos[4][0], infos[4][1], infos[4][2])
    # TwoMast3 = Ship(infos[5][0], infos[5][1], infos[5][2])
    # OneMast1 = Ship(infos[6][0], infos[6][1], infos[6][2])
    # OneMast2 = Ship(infos[7][0], infos[7][1], infos[7][2])
    # OneMast3 = Ship(infos[8][0], infos[8][1], infos[8][2])
    # OneMast4 = Ship(infos[9][0], infos[9][1], infos[9][2])
    # list_of_ships = [FourMast, ThreeMast1, ThreeMast2, TwoMast1, TwoMast2,
    #                 TwoMast3, OneMast1, OneMast2, OneMast3, OneMast4]
    return list_of_ships


def check_if_making_is_possible(size, cords,  matrix, direction=None):
    '''Dla gracza;
    Sprawdza czy w danym miejscu da się postawić statek.'''
    list_of_cords = []
    to_remove = []
    if direction == 'poziom':
        m_cords = (cords[0], cords[1] + size - 1)
    elif direction == 'pion':
        m_cords = ((cords[0] + size - 1), cords[1])
    else:
        m_cords = cords
    if not m_cords[0] in range(10) or not m_cords[1] in range(10):
        return False
    for number in range(-1, size +1):
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
        if not loc[0] in range(10) or not loc[1] in range(10):
            to_remove.append(loc)
    for sth in to_remove:
        if sth in list_of_cords:
            list_of_cords.remove(sth)
    for place in list_of_cords:
        if matrix[place[0], place[1]] == 1:
            return False
    return True


def get_input(message):
    return input(message)
