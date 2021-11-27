# KENNESAW STATE UNIVERSITY
# COLLEGE OF COMPUTING AND SOFTWARE ENGINEERING
# DEPARTMENT OF COMPUTER SCIENCE
# Adele Noumbo

class State_of_puzzle:
    def __init__(self, numbers):
        # This method is to create the goal based puzzle.
        # This puzzle contains just numbers

        self.cells = []
        self.blankLocation = 0, 0  # this represent the normal empty space inside the puzzle
        # [0,1,2,3,4,5,6,7,8]
        k = 0
        for i in range(3):  # range number 3 by by with '0' representing the empty space of our puzzle
            row = []
            for j in range(3):

                row.append(numbers[k])
                if numbers[k] == 0:
                    self.blankLocation = i, j
                k += 1
            self.cells.append(row)  # appends the goal puzzle into the cells

    def current_state(self):
        # This methos actually print the input you enter inthe form of our puzzle
        # it respects the way you enter the value
        lines = []
        horizontalline = ("_" * 13)  # trying to shape the 8 puzzle board
        print(horizontalline)
        for row in self.cells:

            rowline = "|"
            for col in row:
                if col == 0:
                    col = "."
                rowline = rowline + " " + col.__str__() + "|"
            print(rowline)
            print(horizontalline)

    def goal(self):  # To check if the current puzzle match the goal puzzle
        # print("Hello Word")
        current = 0
        for i in range(3):
            for j in range(3):
                if current != self.cells[i][j]:
                    # print("Hi")
                    return False
                current += 1
        return True

    def legal_moves(self):  # This return all the legal moves allowed in our game

        row, col = self.blankLocation  # initializing row and column to 0
        legal_moves = []
        if row != 0:  # if the blanc location is not at the first row,
            # a legal move is up
            legal_moves.append("up")
        if row != 2:
            legal_moves.append("down")
        if col != 0:
            legal_moves.append("left")
        if col != 2:
            legal_moves.append("right")
        return legal_moves

    def new_state(self, move):

        # return the next state based on the move
        row, col = self.blankLocation
        if move == "up":  # if
            new_row = row - 1
            new_col = col
        elif move == "down":
            new_row = row + 1
            new_col = col
        elif move == "left":
            new_row = row
            new_col = col - 1
        elif move == "right":
            new_row = row
            new_col = col + 1
        else:
            raise ("illegal move")

        new_puzzle = State_of_puzzle([0, 0, 0, 0, 0, 0, 0, 0, 0])  # initialize the new puzzle
        new_puzzle.cells = [value[:] for value in self.cells]

        # print new_puzzle cells
        new_puzzle.cells[row][col] = self.cells[new_row][new_col]
        new_puzzle.cells[new_row][new_col] = self.cells[row][col]
        new_puzzle.blankLocation = new_row, new_col
        return new_puzzle

    def __eq__(self, other):  # Overrides the default implementation
        # __eq__() is a build in method used to compare two string objects
        for row in range(3):
            if self.cells[row] != other.cells[row]:
                return False

        return True


class Algorithm:
    def __init__(self, state):
        # initialize the search problem"
        self.puzzle = state

    def initial_state(self):
        # return the start state"
        return self.puzzle

    def state_child(self, state):
        # return all the child states
        result = []

        # state = self.puzzle.initial_state()
        # moves = state.legal_moves()

        for move in state.legal_moves():
            cur_state = state.new_state(move)
            result.append((cur_state, move))
        return result

    def goal_state(self, state):
        # return information that state is goal state or not
        return state.goal()


class Queue:  # since i am using bfs for this agent, i need to implement a Queue class

    def __init__(self):
        self.list = []

    def push(self, item):
        self.list.insert(0, item)

    def pop(self):
        return self.list.pop()

    def isEmpty(self):
        return len(self.list) == 0


import copy


def breath_first_search(request):
    state = request.initial_state() # i passed the problem or the initial puzzle
    queue = Queue()  # create an instance of the class Queue
    action = ""  # different action taken to reach the goal state
    final_path = []  # keep track of a path from initial to the goal state
    visited = []  # different state of puzzle visited
    queue.push(((state, action), final_path))  # push the initial problem, the action it take
                                               # and the array to keep track of the path.
    counter = 0

    while not queue.isEmpty():  # as far as the queue is not empty
        # print counter
        current = queue.pop()  #
        # print current
        cur_state_with_action = current[0] # keep track of the state and action of the puzzle
        cur_path = current[1]              # keep track of the current path
        cur_state = cur_state_with_action[0]
        # cur_action = cur_state_with_action[1]
        if cur_state in visited:
            continue
        else:
            visited.append(cur_state) # add all the states that have been already been process

        counter += 1
        # print type(cState)
        if request.goal_state(cur_state): # if we reach the goal state we print it and we have done
            # print "Goal found"
            # print cPath
            return cur_path
        else:
            result = request.state_child(cur_state)  #  In the other case, we passed all the children of the current state inside the queue and proceed
            for succ in result:  # for every children of the current state

                child_path = copy.deepcopy(cur_path) # make a copy of the path of their ancestors
                if succ[0] in visited:  # if a specific children or state of the puzzle is already visited, we skip it, and passed to the other child

                    # print "already present"
                    continue
                else:
                    child_path.append(succ[1])  # add the state of the puzzle that have not yet been visited
                    queue.push((succ, child_path))  #


puzzle = State_of_puzzle([5, 1, 2, 3, 0, 4, 6, 7, 8])  # Here is the sample puzzle
p = Algorithm(puzzle)   # passed the puzzle to the search Problem
path = breath_first_search(p) # passed the puzzle to our bfs algorithm
print(path) # print the different path to the goal state
for p in path:
    puzzle = puzzle.new_state(p) # return the different state of the puzzle to reach the goal state
    puzzle.current_state()       # print the different state
    input(str("Press Enter"))    # every time we press the enter tab, the next state of our puzzle appear until we reach the goal state
