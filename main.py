import board, player


#Board Set-up Constants
WIDTH = int(input("What would you like the width of the board to be?"))
HEIGHT = int(input("What would you like the height of the board to be?"))
#width must be => height

#game tracker
moves = 0
area = WIDTH * HEIGHT

#Board Set-up
playingBoard = board.Board(WIDTH, HEIGHT)

#Player objects Set-up
#IDs must be int positive nonzeroes
#Symbols must be chars
#Names must be nonempty strings
players = []
for x in range(1, 3):
    players.append(
        player.Player(
            str(input("What is the name of player {}?".format(x))),
            str(input("What is the preferred one-character symbol of player {}?".format(x)))[0],
            x,
            x == 1
        )
    )


symbolDict = dict(zip([player.id for player in players], [player.symbol for player in players]))
symbolDict[0] = " " #default case is empty box being a space

#function to check if the game is over
def isGameOver(board):
    return board.horizontalScore() or board.verticalScore() or board.diagonalScore()

while moves < area and not isGameOver(playingBoard):
    #player makes their move
    for player in players:
        if player.isTurn:
            print("It is {}\'s turn.".format(player.name))
            playingBoard.render(symbolDict)
            player.move(playingBoard)
            moves += 1
            player.isTurn = not player.isTurn
        else:
            player.isTurn = not player.isTurn
    
    #program checks if one player is victorious
    if isGameOver(playingBoard):
        winnerID = playingBoard.winner
        for player in players:
            if player.id == winnerID:
                print("Congratulations, {}! You have won the game!".format(player.name))
                
        break
    elif moves == area:
        print("It's a tie! All spaces have been used up.")
        break
#program ends here