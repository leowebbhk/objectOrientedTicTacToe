import board

class Player: #each player will have one turn per game
    def __init__(self, name, symbol, ID, isTurn):
        self.id = ID #player id
        self.name = name #name for victory screen
        self.symbol = symbol #symbol to be displayed
        self.winner = False #flag will be set to true when wins tic tac toe, victory message appears
        self.isTurn = isTurn #if isTurn, move

    def move(self, boardd):
        while True:
            position = int(input("In which position (number in the square) would you like to move? "))
            if boardd.pos(position)['value'] == 0:    
                boardd.mark(self, position)
                break
            else:
                print("Invalid move. Please try again... ")

