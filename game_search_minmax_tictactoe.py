INFINITY = float('inf')
AI_PLAYER = 'X'
HUMAN_PLAYER = 'O'


def is_terminal(state):
    if check_winner(state, AI_PLAYER):
        return True, 1
    elif check_winner(state, HUMAN_PLAYER):
        return True, -1
    elif is_board_full(state):
        return True, 0
    else:
        return False, None

def get_score(state, player):
    is_terminal_state, winner = is_terminal(state)
    if is_terminal_state:
        return winner
    else:
        return 0
    
def minimax(state, player):
    is_terminal_state, score = is_terminal(state)
    if is_terminal_state:
        return score, None

    if player == AI_PLAYER:
        max_score = -INFINITY
        best_move = None
        for move in get_possible_moves(state):
            new_state = make_move(state, move, player)
            if check_winner(new_state, player):
                return INFINITY, move
            score, _ = minimax(new_state, HUMAN_PLAYER)
            if score > max_score:
                max_score = score
                best_move = move
        return max_score, best_move

    else:
        min_score = +INFINITY
        best_move = None
        for move in get_possible_moves(state):
            new_state = make_move(state, move, player)
            if check_winner(new_state, player):
                return -INFINITY, move
            score, _ = minimax(new_state, AI_PLAYER)
            if score < min_score:
                min_score = score
                best_move = move
        return min_score, best_move

def make_move(state, move, player):
    new_state = state.copy()
    new_state[move] = player
    return new_state

def get_possible_moves(state):
    return [i for i, x in enumerate(state) if x == ' ']

def check_winner(state, player):
    return (
        (state[0] == state[1] == state[2] == player) or
        (state[3] == state[4] == state[5] == player) or
        (state[6] == state[7] == state[8] == player) or
        (state[0] == state[3] == state[6] == player) or
        (state[1] == state[4] == state[7] == player) or
        (state[2] == state[5] == state[8] == player) or
        (state[0] == state[4] == state[8] == player) or
        (state[2] == state[4] == state[6] == player)
    )

def is_board_full(state):
    return all([x != ' ' for x in state])

def print_board(state):
    print(f" {state[0]} | {state[1]} | {state[2]} ")
    print("---+---+---")
    print(f" {state[3]} | {state[4]} | {state[5]} ")
    print("---+---+---")
    print(f" {state[6]} | {state[7]} | {state[8]} ")

def get_human_move(state):
    while True:
        try:
            move = int(input("Enter move (0-8): "))
            if move < 0 or move > 8:
                print("Invalid move. Please enter a number between 0 and 8.")
            elif state[move] == ' ':
                return move
            else:
                print("That cell is already taken. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 8.")


def get_ai_move(state):
    """
    Uses the alpha-beta pruning algorithm to select the best move for the AI.
    """
    _, move = minimax(state, AI_PLAYER, alpha=-INFINITY, beta=INFINITY)
    return move

def initial_state():
    return [' ' for _ in range(9)]


def play_game():
    state = [' '] * 9
    user=input("Do you want go first? y/n\n")
    if user=="y":
        current_player = HUMAN_PLAYER
    else:
        current_player= AI_PLAYER

    print("TIC TAC TOE\n")
    while True:
        
        print_board(state)
        print("\n")
        
        if current_player == HUMAN_PLAYER:
            print("Opponent, Its your turn.\n")
            move = get_human_move(state)
        else:
            print("AI Played the move.\n")
            _, move = minimax(state, AI_PLAYER)
        
        state = make_move(state, move, current_player)
        
        if check_winner(state, current_player):
            print_board(state)
            if current_player=="X":
                print("AI win")
            else:
                print("You win!")
            break
        
        if is_board_full(state):
            print_board(state)
            print("Tie!")
            break
        
        current_player = AI_PLAYER if current_player == HUMAN_PLAYER else HUMAN_PLAYER


if __name__ == '__main__':
    play_game()