
from queue import PriorityQueue
class PuzzleState:
    def __init__(self, board, moves=0, parent=None):
        self.board = board
        self.moves = moves
        self.parent = parent
        self.goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    def __eq__(self, other):
        return self.board == other.board
    def __lt__(self, other):
        return self.moves + self.heuristic() < other.moves + other.heuristic()
    def __hash__(self):
        return hash(str(self.board))
    def __str__(self):
        return str(self.board)
    def heuristic(self):
        distance = 0
        for i in range(3):
            for j in range(3):
                if self.board[i][j] != 0:
                    row = (self.board[i][j] - 1) // 3
                    col = (self.board[i][j] - 1) % 3
                    distance += abs(i - row) + abs(j - col)
        return distance

    def generate_states(self):
        states = []
        i, j = self.get_zero_index()
        if i > 0:
            states.append(self.get_state_after_move(i, j, i - 1, j))
        if i < 2:
            states.append(self.get_state_after_move(i, j, i + 1, j))
        if j > 0:
            states.append(self.get_state_after_move(i, j, i, j - 1))
        if j < 2:
            states.append(self.get_state_after_move(i, j, i, j + 1))
        return states
    def get_zero_index(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return i, j
    def get_state_after_move(self, i, j, new_i, new_j):
        new_board = [row[:] for row in self.board]
        new_board[i][j], new_board[new_i][new_j] = new_board[new_i][new_j], new_board[i][j]
        return PuzzleState(new_board, self.moves + 1, self)
def solve_puzzle(initial_state):
    visited = set()
    queue = PriorityQueue()
    queue.put(initial_state)
    while not queue.empty():
        state = queue.get()
        if state.board == state.goal:
            return state.moves
        visited.add(state)
        for neighbor in state.generate_states():
            if neighbor not in visited:
                queue.put(neighbor)

    return None
initial_board = [[1, 2, 3], [0, 4, 6], [7, 5, 8]]
initial_state = PuzzleState(initial_board)
solution_moves = solve_puzzle(initial_state)
print("The number of moves required to find the goal state is:")
print(solution_moves)
