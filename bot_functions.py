from random import choice
from matrix_generation import create_random_cords


def first_bot_shoot(matrix, dim):
    '''
    Choose cords for first bot's shoot
    and returns them
    '''
    check = False
    while not check:
        cords = create_random_cords(dim)
        check = check_first_shoot(matrix, cords, dim)
    else:
        return cords


def check_bot_shoot_result(matrix, cords_list, shot_list,
                           dim, direction=None):
    '''
    Draws cords from list, deletes unneded
    and checks result of shoot
    '''
    new_list = check_possibility_of_shoot(cords_list, matrix,
                                          shot_list, dim, direction)
    chosen_cords = choice(new_list)
    if matrix[chosen_cords[0], chosen_cords[1]] == 1:
        return True, chosen_cords
    if matrix[chosen_cords[0], chosen_cords[1]] == 0:
        return False, chosen_cords


def check_possibility_of_shoot(cords_list, matrix,
                               shot_list, dim, direction=None):
    '''
    Delete cords which are impossible to make shot at.
    '''
    to_remove = []
    saize = range(dim)
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


def another_bot_shoot(matrix, shot_list, dim, direction=None, turn=None):
    '''
    Returns result and new cords;
    creates list of sensible-to-shoot cords
    then uses it as an argument for
    check_bot_shoot_result, which returns
    proper values
    '''
    shot_list.sort()
    f_cords = shot_list[0]
    s_cords = shot_list[-1]
    if f_cords == s_cords:
        cords_list = [(f_cords[0], f_cords[1]+1), (f_cords[0], f_cords[1]-1),
                      (f_cords[0]-1, f_cords[1]), (f_cords[0]+1, f_cords[1])]
    elif f_cords[0] == s_cords[0]:
        cords_list = [(f_cords[0], f_cords[1]+1), (f_cords[0], f_cords[1]-1),
                      (f_cords[0], s_cords[1]-1), (f_cords[0], s_cords[1]+1)]
    elif f_cords[1] == f_cords[1]:
        cords_list = [(f_cords[0]-1, f_cords[1]), (f_cords[0]+1, f_cords[1]),
                      (s_cords[0]-1, f_cords[1]), (s_cords[0]+1, f_cords[1])]
    cords_list = list(set(cords_list))
    return check_bot_shoot_result(matrix, cords_list, shot_list, dim)


def conduct_bot_shot(matrix_object, fleet_object,
                     shot_list, cords, result, dim):
    '''
    Conducts whole bot's shooting process.
    In appropriate situations leads to missed(),
    hit(), sinked() or f_continue() functions.
    '''
    if not result:
        matrix_object = missed(matrix_object, cords)
        return matrix_object, fleet_object, shot_list
    else:
        lifes, matrix_object, fleet_object = hit(matrix_object,
                                                 cords, fleet_object,
                                                 dim)
        if lifes == 0:
            return matrix_object, sinked(fleet_object, cords), []
        else:
            shot_list, fleet_object = f_continue(fleet_object,
                                                 cords, shot_list)
            return matrix_object, fleet_object, shot_list


def check_first_shoot(matrix, cords, dim):
    '''
    Checks if it's possible to shoot at
    chosen cords.
    (For use only when shoot at random place.)
    If the shoot is out of array range or
    just sensless, returns False,
    in another case returns True
    '''
    list_of_cords = []
    to_remove = []
    for element in range(-1, 2):
        list_of_cords.append((cords[0] - 1, cords[1] + element))
        list_of_cords.append((cords[0], cords[1] + element))
        list_of_cords.append((cords[0] + 1, cords[1] + element))
    for m_cords in list_of_cords:
        if not m_cords[0] in range(dim) or not m_cords[1] in range(dim):
            to_remove.append(m_cords)
    for l_cords in to_remove:
        list_of_cords.remove(l_cords)
    to_remove = []
    for s_cords in list_of_cords:
        if matrix[s_cords[0], s_cords[1]] == 3:
            to_remove.append(s_cords)
    for elem in to_remove:
        list_of_cords.remove(elem)
    for n_cords in list_of_cords:
        if matrix[n_cords[0], n_cords[1]] == 2:
            return False
    if cords not in list_of_cords:
        return False
    return True


def check_if_score(matrix, cords):
    '''
    Checks if shot was succesful
    '''
    if matrix[cords[0], cords[1]] == 1:
        return True
    else:
        return False


def check_direction_and_turn(first_cords, second_cords):
    '''
    Checks direction and turn of ship
    '''
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
    '''
    Is used when shoot was missed.
    Prints proper message and
    if it is sensible, changes value of array
    in given cords
    '''
    if is_bot:
        print('BOT CHYBIŁ')
    else:
        print('PUDŁO!')
    if matrix_object.get_matrix()[cords[0], cords[1]] != 2:
        matrix_object.change_element_value(cords, 3)
    return matrix_object


def hit(matrix_object, cords, fleet_object, dim, is_bot=True):
    '''
    Is used when shoot was succesful.
    Prints proper message, changes array value
    and hurts ship in fleet.
    '''
    if is_bot:
        print('BOT TRAFIŁ')
    else:
        print('TRAFIONY!')
    matrix_object.change_element_value(cords, 2)
    fleet_object.get_ship(cords).hurt()
    return fleet_object.get_ship(cords).get_size(), matrix_object, fleet_object


def sinked(fleet_object, cords, is_bot=True):
    '''
    Is used when ship sinks.
    Prints proper message and removes sinked
    ship from the fleet
    '''
    if is_bot:
        print('BOT ZATOPIŁ STATEK!')
    else:
        print('Statek został ZATOPIONY')
    fleet_object.remove_ship_from_fleet(fleet_object.get_ship(cords))
    return fleet_object


def f_continue(fleet_object, cords, shot_list=None, is_bot=True):
    '''
    Is used when shooting serie is continued.
    Appends list of shot ship's cords and prints
    proper message.
    '''
    fleet_object.get_ship(cords).remove_cord(cords)
    if shot_list is not None:
        shot_list.append(cords)
    if is_bot:
        print('Ostrzał będzie kontynuowany')
    else:
        print('KONTYNUUJ ostrzał!')
    return shot_list, fleet_object
