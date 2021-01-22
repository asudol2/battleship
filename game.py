from matrix_generation import (
    show_actual_board,
    make_player_matrix,
    generate_computer_matrix,
    get_basic_info
)
from game_functions import (
    show_actual_state,
    better_bot_shoot,
    player_shoot,
    introduction
)


def main():
    '''
    Whole game function.
    Gets info from player. Creates bot and player fleets.
    Conducts whole game process and when needed, prints
    messages to player.
    '''
    introduction()
    dim, size_list = get_basic_info()
    Bot_Matrix, Bot_Fleet = generate_computer_matrix(size_list, dim)
    Player_Matrix, Player_Fleet = make_player_matrix(size_list, dim)
    print('Grajmy!')
    show_actual_state(Player_Matrix, Bot_Matrix, dim)
    shot_list = []
    while Player_Fleet.if_fleet_is() and Bot_Fleet.if_fleet_is():
        result_b, result_p = True, True
        while result_p:
            Bot_Matrix, Bot_Fleet, result_p = player_shoot(Bot_Matrix,
                                                           Bot_Fleet, dim)
            if not Bot_Fleet.if_fleet_is():
                show_actual_state(Player_Matrix, Bot_Matrix, dim)
                print('Wygrałeś!')
                print('Koniec gry :)')
                return
            else:
                print(show_actual_board(Bot_Matrix.get_matrix(), dim, True))
                print('Gramy dalej')
        else:
            show_actual_state(Player_Matrix, Bot_Matrix, dim)
        while result_b:
            (Player_Matrix, result_b,
             Player_Fleet, shot_list) = better_bot_shoot(Player_Matrix,
                                                         Player_Fleet,
                                                         shot_list, dim)
            if not Player_Fleet.if_fleet_is():
                show_actual_state(Player_Matrix, Bot_Matrix, dim)
                print('Przegrałeś!')
                print('Koniec gry :)')
                return
            else:
                show_actual_state(Player_Matrix, Bot_Matrix, dim)
        else:
            show_actual_board(Player_Matrix.get_matrix(), dim)
            print('Gramy dalej')


if __name__ == '__main__':
    main()
