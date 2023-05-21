class Node:
    def __init__(self, data, level, fval):
        # Initialize the node with the data ,level of the node and the calculated fvalue
        self.data = data
        self.level = level
        self.fval = fval
    def generate_child(self):
        # Generate hild nodes from the given node by moving the blank space
        # either in the four direction {up,down,left,right}
        x, y = self.find(self.data, '_')
        # val_list contains position values for moving the blank space in either of
        # the 4 direction [up,down,left,right] respectively.
        val_list = [[x, y - 1], [x, y + 1], [x - 1, y], [x + 1, y]]
        children = []
        for i in val_list:
            child = self.shuffle(self.data, x, y, i[0], i[1])
            if child is not None:
                child_node = Node(child, self.level + 1, 0)
                children.append(child_node)
        return children
    def shuffle(self, puz, x1, y1, x2, y2):
        # Move the blank space in the given direction and if the position value are out
        # of limits the return None
        if x2 >= 0 and x2 < len(self.data) and y2 >= 0 and y2 < len(self.data):
            temp_puz = []
            temp_puz = self.copy(puz)
            temp = temp_puz[x2][y2]
            temp_puz[x2][y2] = temp_puz[x1][y1]
            temp_puz[x1][y1] = temp
            return temp_puz
        else:
            return None
    def copy(self, root):
        # copy function to create a similar matrix of the given node
        temp = []
        for i in root:
            t = []
            for j in i:
                t.append(j)
            temp.append(t)
        return temp
    def find(self, puz, x):
        # Specifically used to find the position of the blank space
        for i in range(0, len(self.data)):
            for j in range(0, len(self.data)):
                if puz[i][j] == x:
                    return i, j
class Puzzle:
    def __init__(self, size):
        # Initialize the puzzle size by the the specified size,open and closed lists to empty
        self.n = size
        self.open = []
        self.closed = []
    def accept(self):
        # Accepts the puzzle from the user
        puz = []
        for i in range(0, self.n):
            temp = input().split(" ")
            puz.append(temp)
        return puz
    def f(self, start, goal):
        # Heuristic function to calculate Heuristic value f(x) = h(x) + g(x)
        return self.h(start.data, goal) + start.level
    def h(self, start, goal):
        # Calculates the difference between the given puzzles
        temp = 0
        for i in range(0, self.n):
            for j in range(0, self.n):
                if start[i][j] != goal[i][j] and start[i][j] != '_':
                    temp += 1
        return temp
    def process(self):
        # Accept Start and Goal Puzzle state
        print("enter the start state matrix \n")
        start = self.accept()
        print("enter the goal state matrix \n")
        goal = self.accept()
        start = Node(start, 0, 0)
        start.fval = self.f(start, goal)
        # put the start node in the open list
        self.open.append(start)
        print("\n\n")
        while True:
            cur = self.open[0]
            print("==================================================\n")
            for i in cur.data:
                for j in i:
                    print(j, end=" ")
                print("")
            # if the difference between current and goal node is 0 we have reached the goal node
            if (self.h(cur.data, goal) == 0):
                break
            for i in cur.generate_child():
                i.fval = self.f(i, goal)
                self.open.append(i)
            self.closed.append(cur)

            del self.open[0]
            # sort the open list based on f value
            self.open.sort(key=lambda x: x.fval, reverse=False)
puz = Puzzle(int(input("Enter the size:")))
puz.process()


# from queue import PriorityQueue
# class PuzzleState:
#     def __init__(self, board, moves=0, parent=None):
#         self.board = board
#         self.moves = moves
#         self.parent = parent
#         self.goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
#     def __eq__(self, other):
#         return self.board == other.board
#     def __lt__(self, other):
#         return self.moves + self.heuristic() < other.moves + other.heuristic()
#     def __hash__(self):
#         return hash(str(self.board))
#     def __str__(self):
#         return str(self.board)
#     def heuristic(self):
#         distance = 0
#         for i in range(3):
#             for j in range(3):
#                 if self.board[i][j] != 0:
#                     row = (self.board[i][j] - 1) // 3
#                     col = (self.board[i][j] - 1) % 3
#                     distance += abs(i - row) + abs(j - col)
#         return distance

#     def generate_states(self):
#         states = []
#         i, j = self.get_zero_index()
#         if i > 0:
#             states.append(self.get_state_after_move(i, j, i - 1, j))
#         if i < 2:
#             states.append(self.get_state_after_move(i, j, i + 1, j))
#         if j > 0:
#             states.append(self.get_state_after_move(i, j, i, j - 1))
#         if j < 2:
#             states.append(self.get_state_after_move(i, j, i, j + 1))
#         return states
#     def get_zero_index(self):
#         for i in range(3):
#             for j in range(3):
#                 if self.board[i][j] == 0:
#                     return i, j
#     def get_state_after_move(self, i, j, new_i, new_j):
#         new_board = [row[:] for row in self.board]
#         new_board[i][j], new_board[new_i][new_j] = new_board[new_i][new_j], new_board[i][j]
#         return PuzzleState(new_board, self.moves + 1, self)
# def solve_puzzle(initial_state):
#     visited = set()
#     queue = PriorityQueue()
#     queue.put(initial_state)
#     while not queue.empty():
#         state = queue.get()
#         if state.board == state.goal:
#             return state.moves
#         visited.add(state)
#         for neighbor in state.generate_states():
#             if neighbor not in visited:
#                 queue.put(neighbor)

#     return None
# initial_board = [[4, 1, 3], [7, 2, 5], [0, 8, 6]]
# initial_state = PuzzleState(initial_board)
# solution_moves = solve_puzzle(initial_state)
# print("The number of moves required to find the goal state is:")
# print(solution_moves)
