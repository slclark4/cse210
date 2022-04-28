# Tic-Tac-Toe ----- Stephanie Clark
# from colorama

def main():

    gameBoardList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    drawList = []

    game = "started"

    while game == "started":
        gameBoard(gameBoardList)
        xTurn(gameBoardList)
        game = gameOver(gameBoardList, drawList)
        print()

        if game == "started":
            gameBoard(gameBoardList)
            oTurn(gameBoardList)
            game = gameOver(gameBoardList, drawList)
            print()
            
        if game == "over":
            gameBoard(gameBoardList)

def gameBoard(gameBoardList):
    print(f" {gameBoardList[0]} | {gameBoardList[1]} | {gameBoardList[2]}")
    print("-----------")
    print(f" {gameBoardList[3]} | {gameBoardList[4]} | {gameBoardList[5]}")
    print("-----------")
    print(f" {gameBoardList[6]} | {gameBoardList[7]} | {gameBoardList[8]}")

def xTurn(gameBoardList):
    mark = int(input("x's turn: Where will you place your mark? "))

    mark -= 1

    gameBoardList[mark] = "x"

def oTurn(gameBoardList):
    mark = int(input("o's turn: Where will you place your mark? "))

    mark -= 1

    gameBoardList[mark] = "o"

def gameOver(gameBoardList, drawList):
    one = gameBoardList[0]
    two = gameBoardList[1]
    three = gameBoardList[2]
    four = gameBoardList[3]
    five = gameBoardList[4]
    six = gameBoardList[5]
    seven = gameBoardList[6]
    eight = gameBoardList[7]
    nine = gameBoardList[8]

    game = "started"

    if one == "x" and two == "x" and three == "x":
        print("X is the winner")
        game = "over"
    elif four == "x" and five == "x" and six == "x":
        print("X is the winner")
        game = "over"
    elif seven == "x" and eight == "x" and nine == "x":
        print("X is the winner")
        game = "over"
    elif one == "x" and four == "x" and seven == "x":
        print("X is the winner")
        game = "over"
    elif two == "x" and five == "x" and eight == "x":
        print("X is the winner")
        game = "over"
    elif three == "x" and six == "x" and nine == "x":
        print("X is the winner")
        game = "over"
    elif one == "x" and five == "x" and nine == "x":
        print("X is the winner")
        game = "over"
    elif three == "x" and five == "x" and seven == "x":
        print("X is the winner")
        game = "over"
    elif one == "o" and two == "o" and three == "o":
        print("O is the winner")
        game = "over"
    elif four == "o" and five == "o" and six == "o":
        print("O is the winner")
        game = "over"
    elif seven == "o" and eight == "o" and nine == "o":
        print("O is the winner")
        game = "over"
    elif one == "o" and four == "o" and seven == "o":
        print("O is the winner")
        game = "over"
    elif two == "o" and five == "o" and eight == "o":
        print("O is the winner")
        game = "over"
    elif three == "o" and six == "o" and nine == "o":
        print("O is the winner")
        game = "over"
    elif one == "o" and five == "o" and nine == "o":
        print("O is the winner")
        game = "over"
    elif three == "o" and five == "o" and seven == "o":
        print("O is the winner")
        game = "over"
    elif one != 1 and two != 2 and three != 3 and four != 4 and five != 5 and six != 6 and seven != 7 and eight != 8 and nine != 9:
        print("It's a draw")
        game = "over"

    return game
main()
