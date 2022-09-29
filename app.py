#Defining variables to be used in the game.

Row1 = ['.','.','.']
Row2 = ['.','.','.']
Row3 = ['.','.','.']
user1 = ""
user2 = ""

#FUNCTIONS -------------------------------------------
#Prints the board out
def printBoard():
    print("", "", "1", "2", "3")
    print("A", Row1[0], Row1[1], Row1[2])
    print("B", Row2[0], Row2[1], Row2[2])
    print("C", Row3[0], Row3[1], Row3[2])

#Sets the game up
def initialize():
    global user1
    global user2
    user1 = input("Who is the first player? ")
    user2 = input("Who is the second player? ")

    runGame(user1, user2)

#Runs the game for user one
def runGame(user1, user2):
    global Row1
    global Row2
    global Row3
    printBoard()
    
    p1MoveRow = input("Which row? ")
    p1MoveColumn = int(input("Which column? "))

    if p1MoveRow == "A":
        actualColumn = p1MoveColumn - 1
        if (Row1[actualColumn] != "X") and (Row1[actualColumn] != "O"):
            Row1[actualColumn] = "O"
    elif p1MoveRow == "B":
        actualColumn = p1MoveColumn - 1
        Row2[actualColumn] = "O"
    elif p1MoveRow == "C":
        actualColumn = p1MoveColumn - 1
        Row3[actualColumn] = "O"
    else:
        print("Invalid move")
    printBoard()
    if (Row1[0] == "O" and Row2[0] == "O" and Row3[0] == "O") or (Row1[1] == "O" and Row2[1] == "O" and Row3[1] == "O") or (Row1[2] == "O" and Row2[2] == "O" and Row3[2] == "O") or (Row1[0] == "O" and Row2[1] == "O" and Row3[2] == "O") or (Row1[2] == "O" and Row2[1] == "O" and Row3[0] == "O") or (Row1[0] == "O" and Row1[1] == "O" and Row1[2] == "O") or (Row2[0] == "O" and Row2[1] == "O" and Row2[2] == "O") or (Row3[0] == "O" and Row3[1] == "O" and Row3[2] == "O"):
        print(user1, "won!")
        exit()
    elif (Row1[0] == "X" and Row2[0] == "X" and Row3[0] == "X") or (Row1[1] == "X" and Row2[1] == "X" and Row3[1] == "X") or (Row1[2] == "X" and Row2[2] == "X" and  Row3[2] == "X") or (Row1[0] == "X" and Row2[1] == "X" and Row3[2] == "X") or (Row1[2] == "X" and Row2[1] == "X" and Row3[0] == "X") or (Row1[0] == "X" and Row1[1] == "X" and Row1[2] == "X") or (Row2[0] == "X" and Row2[1] == "X" and Row2[2] == "X") or (Row3[0] == "X" and Row3[1] == "X" and Row3[2] == "X"):
        print(user2, "won!")
        exit()
    elif (Row1[0] != "." and Row1[1] != "." and Row1[2] != ".") and (Row2[0] != "." and Row2[1] != "." and Row2[2] != ".") and (Row3[0] != "." and Row3[1] != "." and Row3[2] != "."):
        print("Its a draw!")
        exit()
    else:
        P2Move(user1, user2)

#------------------------------------PLAYER TWO--------------------------------

def P2Move(user1, user2):
    
    global Row1
    global Row2
    global Row3

    p2MoveRow = input("Which row? ")
    p2MoveColumn = int(input("Which column? "))

    if p2MoveRow == "A":
        actualColumn = p2MoveColumn - 1
        if (Row1[actualColumn] != "X") and (Row1[actualColumn] != "O"):
            Row1[actualColumn] = "X"
        else:
            print("Invalid")
            P2Move(user1, user2)
    elif p2MoveRow == "B":
        actualColumn = p2MoveColumn - 1
        if (Row2[actualColumn] != "X") and (Row2[actualColumn] != "O"):
            Row2[actualColumn] = "X"
    elif p2MoveRow == "C":
        actualColumn = p2MoveColumn - 1
        if (Row3[actualColumn] != "X") and (Row3[actualColumn] != "O"):
            Row3[actualColumn] = "X"
    else:
        print("Invalid move")
        P2Move(user1, user2)
    
    if (Row1[0] == "O" and Row2[0] == "O" and Row3[0] == "O") or (Row1[1] == "O" and Row2[1] == "O" and Row3[1] == "O") or (Row1[2] == "O" and Row2[2] == "O" and Row3[2] == "O") or (Row1[0] == "O" and Row2[1] == "O" and Row3[2] == "O") or (Row1[2] == "O" and Row2[1] == "O" and Row3[0] == "O") or (Row1[0] == "O" and Row1[1] == "O" and Row1[2] == "O") or (Row2[0] == "O" and Row2[1] == "O" and Row2[2] == "O") or (Row3[0] == "O" and Row3[1] == "O" and Row3[2] == "O"):
        print(user1, "won!")
        exit()
    elif (Row1[0] == "X" and Row2[0] == "X" and Row3[0] == "X") or (Row1[1] == "X" and Row2[1] == "X" and Row3[1] == "X") or (Row1[2] == "X" and Row2[2] == "X" and  Row3[2] == "X") or (Row1[0] == "X" and Row2[1] == "X" and Row3[2] == "X") or (Row1[2] == "X" and Row2[1] == "X" and Row3[0] == "X") or (Row1[0] == "X" and Row1[1] == "X" and Row1[2] == "X") or (Row2[0] == "X" and Row2[1] == "X" and Row2[2] == "X") or (Row3[0] == "X" and Row3[1] == "X" and Row3[2] == "X"):
        print(user2, "won!")
        exit()
    elif (Row1[0] != "." and Row1[1] != "." and Row1[2] != ".") and (Row2[0] != "." and Row2[1] != "." and Row2[2] != ".") and (Row3[0] != "." and Row3[1] != "." and Row3[2] != "."):
        print("Its a draw!")
        exit()
    else:
        runGame(user1, user2)


#Prints the board out for player two.
def printBoard():
    print("", "", "1", "2", "3")
    print("A", Row1[0], Row1[1], Row1[2])
    print("B", Row2[0], Row2[1], Row2[2])
    print("C", Row3[0], Row3[1], Row3[2])
#Runs the game
initialize()
