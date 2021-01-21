from matrix_generation import ask_for_cords, show_actual_board
from time import sleep
from bot_functions import (
    fourth_bot_shoot,
    third_bot_shoot,
    first_bot_shoot,
    check_direction_and_turn,
    second_bot_shoot,
    check_if_score,
    missed,
    sinked,
    hit,
    f_continue
)


def check_if_ship_is(cords, matrix):
    '''Sprawdza (NA PODSTAWIE MACIERZY) czy w danym koordynacie znajduje się statek.
    Jeżeli jest, zwraca True, w przeciwnym wypadku False'''
    if matrix[cords[0], cords[1]] == 1:
        return True
    return False


def check_if_ship_is_drowned(cords, matrix):
    '''Jeżeli w danym miejscu było strzelane, zwraca True, jeżeli nie, zwraca False'''
    if matrix[cords[0], cords[1]] == 2:
        return True
    return False


def player_shoot(matrix_object, fleet_object):
    '''Obsługuje pojedynczy strzał oddany użytkownika DO BOTA'''
    print('Wybierz miejsce, w które strzelisz.')
    first, second = ask_for_cords()
    cords = (first, second)
    feedback = check_if_ship_is(cords, matrix_object.get_matrix())
    if not feedback:
        return missed(matrix_object, cords, False), fleet_object, False
    else:
        lifes, matrix_object, fleet_object = hit(matrix_object, cords, fleet_object, False)
        if lifes == 0:
            fleet_object = sinked(fleet_object, cords, False)
        else:
            temp, fleet_object = f_continue(fleet_object, cords, is_bot=False)
        #sleep(1.)
        return matrix_object, fleet_object, True


def show_actual_state(player_board, computer_board):
    #sleep(1.)
    '''Drukuje aktualny stan bitwy (plansze gracza i bota)'''
    print('\t\tTWOJA PLANSZA\t\t\t\t    PLANSZA PRZECIWNIKA')
    for p_board, c_board in zip(player_board, computer_board):
        print(p_board, c_board)


def better_bot_shoot(matrix_object, fleet_object, list_of_shot_cords):
    if len(list_of_shot_cords) == 0:
        first_cords = first_bot_shoot(matrix_object.get_matrix())
        if not check_if_score(matrix_object.get_matrix(), first_cords):
            matrix_object = missed(matrix_object, first_cords)
            return matrix_object, False, fleet_object, list_of_shot_cords
        else:
            lifes, matrix_object, fleet_object= hit(matrix_object, first_cords, fleet_object)
            if lifes == 0:
                return matrix_object, True, sinked(fleet_object, first_cords), []
            else:
                list_of_shot_cords, fleet_object = f_continue(fleet_object, first_cords, list_of_shot_cords)


    if len(list_of_shot_cords) == 1:
        first_cords = list_of_shot_cords[0]
        result, second_cords = second_bot_shoot(matrix_object.get_matrix(), first_cords, list_of_shot_cords)
        if not result:
            matrix_object = missed(matrix_object, second_cords)
            return matrix_object, False, fleet_object, list_of_shot_cords
        else:
            lifes, matrix_object, fleet_object = hit(matrix_object, second_cords, fleet_object)
            if lifes == 0:
                return matrix_object, True, sinked(fleet_object, second_cords), []
            else:
                list_of_shot_cords, fleet_object = f_continue(fleet_object, second_cords, list_of_shot_cords)


    if len(list_of_shot_cords) == 2:
        first_cords, second_cords = list_of_shot_cords[0], list_of_shot_cords[1]
        direction, turn = check_direction_and_turn(first_cords, second_cords)
        result, third_cords = third_bot_shoot(matrix_object.get_matrix(), first_cords,
        second_cords, direction, turn, list_of_shot_cords)
        if not result:
            matrix_object = missed(matrix_object, third_cords)
            return matrix_object, False, fleet_object, list_of_shot_cords
        else:
            lifes, matrix_object, fleet_object = hit(matrix_object, third_cords, fleet_object)
            if lifes == 0:
                return matrix_object, True, sinked(fleet_object, third_cords), []
            else:
                list_of_shot_cords, fleet_object = f_continue(fleet_object, third_cords, list_of_shot_cords)


    if len(list_of_shot_cords) == 3:
        first_cords = list_of_shot_cords[0]
        second_cords = list_of_shot_cords[1]
        direction, turn = check_direction_and_turn(first_cords, second_cords)
        result, fourth_cords = fourth_bot_shoot(matrix_object.get_matrix(),
        list_of_shot_cords, direction)
        if not result:
            matrix_object = missed(matrix_object, fourth_cords)
            return matrix_object, False, fleet_object, list_of_shot_cords
        else:
            lifes, matrix_object, fleet_object = hit(matrix_object, fourth_cords, fleet_object)
            return matrix_object, True, sinked(fleet_object, fourth_cords), []


def introduction():
    print('Dzień dobry!')
    #sleep(0.5)
    print('Zaczynasz grę w statki.')
    #sleep(0.5)
    print('Na początek kilka reguł.')
    #sleep(0.5)
    print('Czytaj, nie mogą stykać się rogami ani bokami.')
    #sleep(0.5)
    print('Czytaj uważnie co gra do Ciebie pisze.')
    #sleep(3.)
    print('Ty oraz bot, z którym będziesz grać, macie do dyspozycji: ')
    #sleep(0.5)
    print('Jeden 4-kadłubowiec, dwa 3-kadłubowce, trzy 2-kadłubowce i 4 1-kadłubowce.')
    #sleep(3.)
    print('A oto oznaczenia:')
    #sleep(0.5)
    print('□  - to oznacza, że w tym miejscu jest Twój statek')
    #sleep(2.)
    print('⊠  - to oznacza, że statek został trafiony.')
    #sleep(2.)
    print('○   - to oznacza, że w tym miejscu zostało spudłowane')
    #sleep(2.)
    print('Miłej gry życzę :)')
    #sleep(1.)
