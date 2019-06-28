class Board: #object which houses the playing field
    def __init__(self, width, height):
        self.width = max((width, height))
        self.height = min((width, height))
        self.cells = [[0 for cell in range(self.width)] for row in range(self.height)] #the cells of the tic tac toe board
        self.winner = 0
        self.filledRows = set([])
        self.filledColumns = set([])

    def horizontalScore(self): #returns a boolean based on whether or not a horizontal row has been formed
        for row in self.cells:
            if len(set(row)) == 1 and not row[0] == 0: #len set is a way of counting the unique elements
                self.winner = row[0]
                return True
            else:
                continue
        return False

    def verticalScore(self):
        for columnIndex in range(self.width):
            if len(set([row[columnIndex] for row in self.cells])) == 1 and not self.cells[0][columnIndex] == 0:
                self.winner = self.cells[0][columnIndex]
                return True
            else:
                continue
        return False
   
    def diagonalScore(self):
        point = False
        for start in range(abs(self.width - self.height) + 1):
            #northwest to southeast
            if len(set([self.cells[x][x+start] for x in range(self.height)])) == 1 and not self.cells[0][start] == 0:
                point = True
                self.winner = self.cells[0][start]
            elif len(set([self.cells[self.height - x - 1][x+start] for x in range(self.height)])) == 1 and not self.cells[self.height - 1][start] == 0:
                point = True
                self.winner = self.cells[self.height - 1][start]
        return point

    def pos(self, position):
        x = (position - 1) % self.width
        y = (position - 1) // self.width
        value = self.cells[y][x]
        return {'x': x, 'y': y, 'value': value}
    
    def mark(self, player, position):
        #x position is the second index of the array meaning which cell in the selected row 
        #y position means which row out of the board
        x, y = self.pos(position)['x'], self.pos(position)['y']
        self.cells[y][x] = player.id

    def render(self, symbolDictionary):
        #each line
        for rowIndex in range(self.height):
            print("#---" * self.width, end="#\n")
#            print("|   " * self.width, end="|\n")
            for cellIndex in range(self.width):
                if self.cells[rowIndex][cellIndex] == 0:
                    print("|{:3d}".format((rowIndex) * self.width + cellIndex + 1), end="")
                else:
                    print("| " + symbolDictionary[self.cells[rowIndex][cellIndex]] + " ", end="")
            print("|\n", end="")
#            print("|   " * self.width, end="|\n")
        print("#---" * self.width, end="#\n\n")

