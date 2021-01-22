from matrix_generation import ask_for_cords, show_actual_board
from time import sleep
from bot_functions import (
    first_bot_shoot,
    check_if_score,
    missed,
    sinked,
    hit,
    f_continue,
    another_bot_shoot,
    conduct_bot_shot
)


def check_if_ship_is(cords, matrix):
    '''Checks if on given cords is any ship'''
    if matrix[cords[0], cords[1]] == 1:
        return True
    return False


def check_if_ship_is_drowned(cords, matrix):
    '''Checks if on this cords was once shot'''
    if matrix[cords[0], cords[1]] == 2:
        return True
    return False


def player_shoot(matrix_object, fleet_object, dim):
    '''Manage with player shoots'''
    print('Wybierz miejsce, w które strzelisz.')
    first, second = ask_for_cords(dim)
    cords = (first, second)
    feedback = check_if_ship_is(cords, matrix_object.get_matrix())
    if not feedback:
        return missed(matrix_object, cords, False), fleet_object, False
    else:
        lifes, matrix_object, fleet_object = hit(matrix_object,
                                                 cords, fleet_object,
                                                 dim, False)
        if lifes == 0:
            fleet_object = sinked(fleet_object, cords, False)
        else:
            temp, fleet_object = f_continue(fleet_object, cords, is_bot=False)
        return matrix_object, fleet_object, True


def show_actual_state(player_matrix_object, bot_matrix_object, dim):
    '''Print boards of player and bot'''
    player_board = show_actual_board(player_matrix_object.get_matrix(), dim)
    bot_board = show_actual_board(bot_matrix_object.get_matrix(), dim, True)
    for p_board, b_board in zip(player_board, bot_board):
        print(p_board, b_board)


def better_bot_shoot(matrix_object, fleet_object, shot_list, dim):
    '''Manage with bot shoots'''
    result = True
    while result:
        if len(shot_list) == 0:
            first_cords = first_bot_shoot(matrix_object.get_matrix(), dim)
            if not check_if_score(matrix_object.get_matrix(), first_cords):
                matrix_object = missed(matrix_object, first_cords)
                return matrix_object, False, fleet_object, shot_list
            else:
                lifes, matrix_object, fleet_object = hit(matrix_object,
                                                         first_cords,
                                                         fleet_object,
                                                         dim)
                if lifes == 0:
                    return matrix_object, True, sinked(fleet_object, first_cords), []
                else:
                    shot_list, fleet_object = f_continue(fleet_object,
                                                         first_cords,
                                                         shot_list)
        else:
            result, cords = another_bot_shoot(matrix_object.get_matrix(),
                                              shot_list, dim)
            (matrix_object, fleet_object,
             shot_list) = conduct_bot_shot(matrix_object,
                                           fleet_object, shot_list, cords,
                                           result, dim)
    else:
        return matrix_object, False, fleet_object, shot_list


def introduction():
    '''Makes introduction in polish'''
    print('Dzień dobry!')
    print('Zaczynasz grę w statki.')
    print('Na początek kilka reguł.')
    print('Statki nie mogą leżeć obok siebie ani się przecinać.')
    print('Czytaj, nie mogą się nakładać ani stykać rogami czy bokami.')
    print('Czytaj uważnie co gra do Ciebie pisze.')
    print('Ilość statków i wielkość planszy będzie zależała od Twojego wyboru')
    print('Będziesz miał do dyspozycji statek o największej ilości kadłubów')
    print('o jeden mniej statków o ilości kadłubów mniejszej o jeden etc.')
    print('W przypadku, gdy wybierzesz statek 5-kadłubowy,')
    print('ich ilość będzie niestandardowa.')
    print('W odpowiednich momentach będzie wyświetlana Twoja plansza')
    print('bądź plansza przeciwnika albo obie:')
    print('Twoja po lewej, bota po prawej stronie.')
    print('A oto oznaczenia:')
    print('□  - to oznacza, że w tym miejscu jest Twój statek')
    print('⊠  - to oznacza, że statek został trafiony.')
    print('○   - to oznacza, że w tym miejscu zostało spudłowane')
    print('Miłej gry życzę :)')
    sleep(20.)
