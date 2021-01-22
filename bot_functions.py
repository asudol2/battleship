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


def check_bot_shoot_result(matrix, cords_list, shot_list, direction=None):
    '''Losuje koordynaty z listy, usuwa niepotrzebne i sprawdza rezultat strzału.'''
    new_list = check_possibility_of_shoot(cords_list, matrix, shot_list, direction)
    chosen_cords = choice(new_list)
    if matrix[chosen_cords[0], chosen_cords[1]] == 1:
        return True, chosen_cords
    if matrix[chosen_cords[0], chosen_cords[1]] == 0:
        return False, chosen_cords


def check_possibility_of_shoot(cords_list, matrix, shot_list, direction=None):
    '''Usuwa koordynaty niemożliwe do wykonania'''
    to_remove = []
    saize = range(0, 10)
    for cords in cords_list:
        if cords in shot_list:
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
    return cords_list


def another_bot_shoot(matrix, shot_list, direction=None, turn=None):
    '''Zwraca rezultat i nowe kordy'''
    shot_list.sort()
    f_cords = shot_list[0]
    s_cords = shot_list[-1]
    if f_cords == s_cords:
        cords_list = [(f_cords[0], f_cords[1]+1), (f_cords[0], f_cords[1]-1),
        (f_cords[0]-1, f_cords[1]), (f_cords[0]+1, f_cords[1])]
    elif f_cords[0] == s_cords[0]: #poziom
        cords_list = [(f_cords[0], f_cords[1]+1), (f_cords[0], f_cords[1]-1),
        (f_cords[0], s_cords[1]-1), (f_cords[0], s_cords[1]+1)]
    elif f_cords[1] == f_cords[1]: #pion
        cords_list = [(f_cords[0]-1, f_cords[1]), (f_cords[0]+1, f_cords[1]),
        (s_cords[0]-1, f_cords[1]), (s_cords[0]+1, f_cords[1])]
    cords_list = list(set(cords_list))
    return check_bot_shoot_result(matrix, cords_list, shot_list)

def conduct_bot_shot(matrix_object, fleet_object, shot_list, cords, result):
    if not result:
        matrix_object = missed(matrix_object, cords)
        return matrix_object, fleet_object, shot_list
    else:
        lifes, matrix_object, fleet_object = hit(matrix_object, cords, fleet_object)
        if lifes == 0:
            return matrix_object, sinked(fleet_object, cords), []
        else:
            shot_list, fleet_object = f_continue(fleet_object, cords, shot_list)
            return matrix_object, fleet_object, shot_list

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

def f_continue(fleet_object, cords, shot_list=None, is_bot=True):
    fleet_object.get_ship(cords).remove_cord(cords)
    if not shot_list is None:
        shot_list.append(cords)
    ###sleep(1.)
    if is_bot:
        print('Ostrzał będzie kontynuowany')
    else:
        print('Kontynuuj ostrzał!')
    ###sleep(2.5)
    return shot_list, fleet_object