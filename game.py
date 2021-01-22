from matrix_generation import show_actual_board, make_player_matrix, generate_computer_matrix
from game_functions import show_actual_state, better_bot_shoot, player_shoot, introduction


def main():
    # introduction()
    Bot_Matrix, Bot_Fleet = generate_computer_matrix()
    Player_Matrix, Player_Fleet = make_player_matrix()
    print('Grajmy!')
    show_actual_state(show_actual_board(Player_Matrix.get_matrix()), show_actual_board(Bot_Matrix.get_matrix(), True))
    shot_list = []
    while Player_Fleet.if_fleet_is() and Bot_Fleet.if_fleet_is():
        result_b, result_p = True, True
        while result_p:
            Bot_Matrix, Bot_Fleet, result_p = player_shoot(Bot_Matrix, Bot_Fleet)
            if not Bot_Fleet.if_fleet_is():
                print('Wygrałeś!')
                print('Koniec gry :)')
                return
            else:
                print(show_actual_board(Bot_Matrix.get_matrix()))
                print('Gramy dalej')
        else:
            show_actual_state(show_actual_board(Player_Matrix.get_matrix()), show_actual_board(Bot_Matrix.get_matrix(), True))
        while result_b:
            Player_Matrix, result_b, Player_Fleet, shot_list = better_bot_shoot(Player_Matrix, Player_Fleet, shot_list)
            if not Player_Fleet.if_fleet_is():
                print('Przegrałeś!')
                print('Koniec gry :)')
                return
            else:
                show_actual_state(show_actual_board(Player_Matrix.get_matrix()), show_actual_board(Bot_Matrix.get_matrix(), True))
        else:
            show_actual_board(Player_Matrix.get_matrix())
            print('Gramy dalej')


if __name__ == '__main__':
    main()
