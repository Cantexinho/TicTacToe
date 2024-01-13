from tictactoe import TicTacToe


def play(game, player1="X", player2="O", print_game=True) -> str:
    if print_game:
        game.print_board()

    letter = "X"
    while game.empty_squares():
        if letter == "O":
            square = int(input(f"{player2}({letter}), Enter your move (0-8): "))
        else:
            square = int(input(f"{player1}({letter}), Enter your move (0-8): "))
        if game.make_move(square, letter):
            if print_game:
                game.print_board()
            if game.current_winner:
                print(letter + " wins!")
                return letter
            letter = "O" if letter == "X" else "X"

    print("It's a tie!")


if __name__ == "__main__":
    size = int(input("Choose board size (3,4,5): "))
    game = TicTacToe(size)
    play(game)
