from random import choice
from matrix_generation import create_random_cords, show_actual_board
from time import sleep


def first_bot_shoot(matrix):
    '''Wybiera koordynaty do pierwszego strzału bota oraz je zwraca'''
    check = False
    while not check:
        cords = create_random_cords()
        check = check_first_shoot(matrix, cords)
    else:
        return cords


def check_bot_shoot_result(matrix, cords_list, list_of_shot_cords, direction=None):
    '''Losuje koordynaty z listy, usuwa niepotrzebne i sprawdza rezultat strzału.'''
    cords_list = check_possibility_of_shoot(cords_list, matrix, list_of_shot_cords, direction)
    chosen_cords = choice(cords_list)
    if matrix[chosen_cords[0], chosen_cords[1]] == 1:
        return True, chosen_cords
    if matrix[chosen_cords[0], chosen_cords[1]] == 0:
        return False, chosen_cords


def check_possibility_of_shoot(cords_list, matrix, list_of_shot_cords, direction=None):
    '''Usuwa koordynaty niemożliwe do wykonania'''
    to_remove = []
    saize = range(0, 10)
    for cords in cords_list:
        if cords in list_of_shot_cords:
            to_remove.append(cords)
    for cords in to_remove:
        cords_list.remove(cords)
    to_remove = []
    for cords in cords_list:
        if not cords[0] in saize or not cords[1] in saize:
            to_remove.append(cords)
    for cords in to_remove:
        cords_list.remove(cords)
    to_remove = []
    for cords in cords_list:
        if matrix[cords[0], cords[1]] in [2, 3]:
            to_remove.append(cords)
    for cords in to_remove:
        cords_list.remove(cords)
    to_remove = []
    if direction:
        for cords in cords_list:
            for num in [-1, 1]:
                if direction == 'poziom' and (cords[0] + num) in saize:
                    if matrix[cords[0] + num, cords[1]] == 2:
                        to_remove.append(cords)
                if direction == 'pion' and (cords[1] + num) in saize:
                    if matrix[cords[0], cords[1] + num] == 2:
                        to_remove.append(cords)
        to_remove = list(set(to_remove))
        for cords in to_remove:
            cords_list.remove(cords)
        return cords_list
    else:
        return cords_list


def second_bot_shoot(matrix, cords, list_of_shot_cords):
    '''Dokonuje strzału w okoliczne miejsce. Jeżeli trafia, zwraca True oraz koordynaty;
    jeżeli nie, zwraca False oraz koordynaty.'''
    additional_cords_list = [(cords[0]-1, cords[1]), (cords[0]+1, cords[1]),
    (cords[0], cords[1]-1), (cords[0], cords[1]+1)]
    return check_bot_shoot_result(matrix, additional_cords_list, list_of_shot_cords)


def third_bot_shoot(matrix, f_cords, s_cords, direction, turn, list_of_shot_cords):
    '''Strzela w kolejne wylosowane pole, zgodnie z kierunkiem.
    Jeżeli trafia, zwraca True oraz koordynaty;
    jeżeli nie, zwraca False i koordynaty.'''
    if direction == 'poziom':
        if turn == 'prawo':
            additional_cords_list = [(s_cords[0], s_cords[1]-2),
            (s_cords[0], s_cords[1]+1)]
        if turn == 'lewo':
            additional_cords_list = [(s_cords[0], s_cords[1]-1),
            (s_cords[0], s_cords[1]+2)]
    else:
        if turn == 'dół':
            additional_cords_list = [(s_cords[0]-2, s_cords[1]),
            (s_cords[0]+1, s_cords[1])]
        if turn == 'góra':
            additional_cords_list = [(s_cords[0]-1, s_cords[1]),
            (s_cords[0]+2, s_cords[1])]
    return check_bot_shoot_result(matrix, additional_cords_list, list_of_shot_cords, direction)


def fourth_bot_shoot(matrix, list_of_shot_cords, direction):
    '''Strzela w wylosowane ostatnie pole, zgodnie z kierunkiem. Jeżeli trafia,
    zwraca True oraz koordynaty; jeżeli nie, zwraca False i koordynaty.'''
    f_cords = list_of_shot_cords[0]
    s_cords = list_of_shot_cords[1]
    t_cords = list_of_shot_cords[2]
    if direction == 'poziom':
        additional_cords_list = [(f_cords[0], f_cords[1]+1), (f_cords[0], f_cords[1]-1),
        (f_cords[0], s_cords[1]-1), (f_cords[0], s_cords[1]+1),
        (f_cords[0], t_cords[1]-1), (f_cords[0], t_cords[1]+1)]
    if direction == 'pion':
        additional_cords_list = [(f_cords[0]-1, f_cords[1]), (f_cords[0]+1, f_cords[1]),
        (s_cords[0]-1, f_cords[1]), (s_cords[0]+1, f_cords[1]),
        (t_cords[0]-1, f_cords[1]), (t_cords[0]+1, f_cords[1])]
    additional_cords_list = list(set(additional_cords_list))
    return check_bot_shoot_result(matrix, additional_cords_list, list_of_shot_cords, direction)



def check_first_shoot(matrix, cords):
    '''Sprawdza czy w dane miejsce można strzelać'''
    list_of_cords = []
    to_remove =[]
    for element in range(-1, 2):
        list_of_cords.append((cords[0] -1, cords[1] + element))
        list_of_cords.append((cords[0], cords[1] + element))
        list_of_cords.append((cords[0] +1, cords[1] + element))
    for m_cords in list_of_cords:
        if not m_cords[0] in range(10) or not m_cords[1] in range(10):
            to_remove.append(m_cords)
    for l_cords in to_remove:
        list_of_cords.remove(l_cords)
    to_remove = []
    for s_cords in list_of_cords:
        if matrix[s_cords[0], s_cords[1]] in [2, 3]:
            to_remove.append(s_cords)
    for elem in to_remove:
        list_of_cords.remove(elem)
    if not cords in list_of_cords:
        return False
    return True


def check_if_score(matrix, cords):
    '''Sprawdza, czy strzał był udany'''
    if matrix[cords[0], cords[1]] == 1:
        return True
    else:
        return False


def check_direction_and_turn(first_cords, second_cords):
    '''Sprawdza w jakim kierunku ustawiony jest statek, żeby sensownie oddawać
    następne strzały oraz jaki ma zwrot i zwraca ten kierunek
    oraz zwrot (string)'''
    f_x, s_x = first_cords[0], second_cords[0]
    f_y, s_y = first_cords[1], second_cords[1]
    if f_x-s_x == 0:
        direction = 'poziom'
        if s_y > f_y:
            turn = 'prawo'
        else:
            turn = 'lewo'
    else:
        direction = 'pion'
        if f_x > s_x:
            turn = 'góra'
        else:
            turn = 'dół'
    return direction, turn


def missed(matrix_object, cords, is_bot=True):
    ###sleep(1.)
    if is_bot:
        print('BOT CHYBIŁ')
    else:
        print('Pudło!')
    matrix_object.change_element_value(cords, 3)
    return matrix_object

def hit(matrix_object, cords, fleet_object, is_bot=True):
    ###sleep(1.)
    if is_bot:
        print('BOT TRAFIŁ')
    else:
        print('Trafiony!')
    matrix_object.change_element_value(cords, 2)
    print(show_actual_board(matrix_object.get_matrix()))
    fleet_object.get_ship(cords).hurt()
    return fleet_object.get_ship(cords).get_size(), matrix_object, fleet_object

def sinked(fleet_object, cords, is_bot=True):
    ###sleep(1.)
    if is_bot:
        print('BOT ZATOPIŁ STATEK!')
    else:
        print('Statek został zatopiony!')
    fleet_object.remove_ship_from_fleet(fleet_object.get_ship(cords))
    return fleet_object

def f_continue(fleet_object, cords, list_of_shot_cords=None, is_bot=True):
    fleet_object.get_ship(cords).remove_cord(cords)
    if not list_of_shot_cords is None:
        list_of_shot_cords.append(cords)
    ###sleep(1.)
    if is_bot:
        print('Ostrzał będzie kontynuowany')
    else:
        print('Kontynuuj ostrzał!')
    ###sleep(2.5)
    return list_of_shot_cords, fleet_object