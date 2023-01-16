
import random


board = ["-", "-", "-", "-", "-" ,"-", "-", "-", "-",
        "-", "-", "-", "-", "-" ,"-", "-", "-", "-",
        "-", "-", "-", "-", "-" ,"-", "-", "-", "-", 
        "-", "-", "-", "-", "-" ,"-", "-", "-", "-",
        "-", "-", "-", "-", "-" ,"-", "-", "-", "-",
        "-", "-", "-", "-", "-" ,"-", "-", "-", "-",
        "-", "-", "-", "-", "-" ,"-", "-", "-", "-",
        "-", "-", "-", "-", "-" ,"-", "-", "-", "-",
        "-", "-", "-", "-", "-" ,"-", "-", "-", "-"]
        
currentPlayer = "S"
winner = None
gameRunning = True

# game board
def printBoard(board):
    print(" -------------------------------------")
    print(" | " + board[0] + " | " + board[1] + " | " + board[2] + " | " + board[3] + " | " + board[4] + " | " + board[5] + " | " + board[6] + " | " + board[7] + " | " + board[8] + " | ") 
    print(" -------------------------------------")
    print(" | " + board[9] + " | " + board[10] + " | " + board[11] + " | " + board[12] + " | " + board[13] + " | " + board[14] + " | " + board[15] + " | " + board[16] + " | " + board[17] + " | ")
    print(" -------------------------------------")
    print(" | " + board[18] + " | " + board[19] + " | " + board[20] + " | " + board[21] + " | " + board[22] + " | " + board[23] + " | " + board[24] + " | " + board[25] + " | " + board[26] + " | ")
    print(" -------------------------------------")
    print(" | " + board[27] + " | " + board[28] + " | " + board[29] + " | " + board[30] + " | " + board[31] + " | " + board[32] + " | " + board[33] + " | " + board[34] + " | " + board[35] + " | ")
    print(" -------------------------------------")
    print(" | " + board[36] + " | " + board[37] + " | " + board[38] + " | " + board[39] + " | " + board[40] + " | " + board[41] + " | " + board[42] + " | " + board[43] + " | " + board[44] + " | ")
    print(" -------------------------------------")
    print(" | " + board[45] + " | " + board[46] + " | " + board[47] + " | " + board[48] + " | " + board[49] + " | " + board[50] + " | " + board[51] + " | " + board[52] + " | " + board[53] + " | ")
    print(" -------------------------------------")
    print(" | " + board[54] + " | " + board[55] + " | " + board[56] + " | " + board[57] + " | " + board[58] + " | " + board[59] + " | " + board[60] + " | " + board[61] + " | " + board[62] + " | ")
    print(" -------------------------------------")
    print(" | " + board[63] + " | " + board[64] + " | " + board[65] + " | " + board[66] + " | " + board[67] + " | " + board[68] + " | " + board[69] + " | " + board[70] + " | " + board[71] + " | ")
    print(" -------------------------------------")
    print(" | " + board[72] + " | " + board[73] + " | " + board[74] + " | " + board[75] + " | " + board[76] + " | " + board[77] + " | " + board[78] + " | " + board[79] + " | " + board[80] + " | ")
    print(" -------------------------------------")

# take player input
def playerInput(board):
    inp = int(input("Select a spot 1-81: "))
    if board[inp-1] == "-":
        board[inp-1] = currentPlayer
    else:
        print("Oops player is already at that spot.")


# check for win or tie
def checkHorizontle(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-" + board[1] == board[2] == board[3] and board[1] != "-" + board[2] == board[3] == board[4] and board[2] != "-" + board[3] == board[4] == board[5] and board[3] != "-" + board[4] == board[5] == board[6] and board[4] != "-" + board[5] == board[6] == board[7] and board[5] != "-" + board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[0]
        winner = board[1]
        winner = board[2]
        winner = board[3]
        winner = board[4]
        winner = board[5]
        winner = board[6]
    
        return True

    elif board[9] == board[10] == board[11] and board[9] != "-" + board[10] == board[11] == board[12] and board[10] != "-" + board[11] == board[12] == board[13] and board[11] != "-" + board[12] == board[13] == board[14] and board[12] != "-" + board[13] == board[14] == board[15] and board[13] != "-" + board[14] == board[15] == board[16] and board[14] != "-" + board[15] == board[16] == board[17] and board[15]!= "-":
        winner = board[9]
        winner = board[10]
        winner = board[11]
        winner = board[12]
        winner = board[13]
        winner = board[14]
        winner = board[15]
        return True

    elif board[18] == board[19] == board[20] and board[18] != "-" + board[19] == board[20] == board[21] and board[19] != "-" + board[20] == board[21] == board[22] and board[20] != "-" + board[21] == board[22] == board[23] and board[21] != "-" + board[22] == board[23] == board[24] and board[22] != "-" + board[23] == board[24] == board[25] and board[23] != "-" + board[24] == board[25] == board[26] and board[24]!= "-":
        winner = board[18]
        winner = board[19]
        winner = board[20]
        winner = board[21]
        winner = board[22]
        winner = board[23]
        winner = board[24]
        return True


    elif board[27] == board[28] == board[29] and board[27] != "-" + board[28] == board[29] == board[30] and board[28] != "-" + board[29] == board[30] == board[31] and board[29] != "-" + board[30] == board[31] == board[32] and board[30] != "-" + board[31] == board[32] == board[33] and board[34] != "-" + board[32] == board[33] == board[34] and board[32] != "-" + board[33] == board[34] == board[35] and board[33]!= "-":
        winner = board[27]
        winner = board[28]
        winner = board[29]
        winner = board[30]
        winner = board[31]
        winner = board[32]
        winner = board[33]
        return True

    elif board[36] == board[37] == board[38] and board[36] != "-" + board[37] == board[38] == board[39] and board[37] != "-" + board[38] == board[39] == board[40] and board[38] != "-" + board[39] == board[40] == board[41] and board[39] != "-" + board[40] == board[41] == board[42] and board[40] != "-" + board[41] == board[42] == board[43] and board[41] != "-" + board[42] == board[43] == board[44] and board[42]!= "-":
        winner = board[36]
        winner = board[37]
        winner = board[38]
        winner = board[39]
        winner = board[40]
        winner = board[41]
        winner = board[42]
        return True

    elif board[45] == board[46] == board[47] and board[45] != "-" + board[46] == board[47] == board[48] and board[46] != "-" + board[47] == board[48] == board[49] and board[47] != "-" + board[48] == board[49] == board[50] and board[48] != "-" + board[49] == board[50] == board[51] and board[49] != "-" + board[50] == board[51] == board[52] and board[50] != "-" + board[51] == board[52] == board[53] and board[51]!= "-":
        winner = board[45]
        winner = board[46]
        winner = board[47]
        winner = board[48]
        winner = board[49]
        winner = board[50]
        winner = board[51]
        return True
      
    elif board[54] == board[55] == board[56] and board[54] != "-" + board[55] == board[56] == board[57] and board[55] != "-" + board[56] == board[57] == board[58] and board[56] != "-" + board[57] == board[58] == board[59] and board[57] != "-" + board[58] == board[59] == board[60] and board[58] != "-" + board[59] == board[60] == board[61] and board[59] != "-" + board[60] == board[61] == board[62] and board[60]!= "-":
        winner = board[54]
        winner = board[55]
        winner = board[56]
        winner = board[57]
        winner = board[58]
        winner = board[59]
        winner = board[60]
        return True

    elif board[63] == board[64] == board[65] and board[63] != "-" + board[64] == board[65] == board[66] and board[64] != "-" + board[65] == board[66] == board[67] and board[65] != "-" + board[66] == board[67] == board[68] and board[66] != "-" + board[67] == board[68] == board[69] and board[67] != "-" + board[68] == board[69] == board[70] and board[68] != "-" + board[69] == board[70] == board[71] and board[69]!= "-":
        winner = board[63]
        winner = board[64]
        winner = board[65]
        winner = board[66]
        winner = board[67]
        winner = board[68]
        winner = board[69]
        return True

    elif board[72] == board[73] == board[74] and board[72] != "-" + board[73] == board[74] == board[75] and board[73] != "-" + board[74] == board[75] == board[76] and board[74] != "-" + board[75] == board[76] == board[77] and board[75] != "-" + board[76] == board[77] == board[78] and board[76] != "-" + board[77] == board[78] == board[79] and board[77] != "-" + board[78] == board[79] == board[80] and board[78]!= "-":
        winner = board[72]
        winner = board[73]
        winner = board[74]
        winner = board[75]
        winner = board[76]
        winner = board[77]
        winner = board[78]

        return True
    

def checkRow(board):
    global winner
if board[0] == board[9] == board[18] and board[0] != "-" + board[9] == board[18] == board[27] and board[9] != "-" + board[18] == board[27] == board[36] and board[18] != "-" + board[27] == board[36] == board[45] and board[27] != "-" + board[36] == board[45] == board[54] and board[36] != "-" + board[45] == board[54] == board[63] and board[45] != "-" + board[54] == board[63] == board[72] and board[54]!= "-":
        winner = board[0] 
        winner = board[9] 
        winner = board[18] 
        winner = board[27] 
        winner = board[36] 
        winner = board[45] 
        winner = board[54]

        
elif board[1] == board[10] == board[19] and board[1] != "-" + board[10] == board[19] == board[28] and board[10] != "-" + board[19] == board[28] == board[37] and board[19] != "-" + board[28] == board[37] == board[46] and board[28] != "-" + board[37] == board[46] == board[55] and board[37] != "-" + board[46] == board[55] == board[64] and board[46] != "-" + board[55] == board[64] == board[73] and board[55]!= "-":
        winner = board[1] 
        winner = board[10] 
        winner = board[19] 
        winner = board[28] 
        winner = board[37] 
        winner = board[46] 
        winner = board[55]
        
elif board[2] == board[11] == board[20] and board[2] != "-" + board[11] == board[20] == board[29] and board[11] != "-" + board[20] == board[29] == board[38] and board[20] != "-" + board[29] == board[38] == board[47] and board[29] != "-" + board[38] == board[47] == board[56] and board[38] != "-" + board[47] == board[56] == board[65] and board[47] != "-" + board[56] == board[65] == board[74] and board[56]!= "-":
        winner = board[2] 
        winner = board[11] 
        winner = board[20] 
        winner = board[29] 
        winner = board[38] 
        winner = board[47] 
        winner = board[56] 

elif board[3] == board[12] == board[21] and board[3] != "-" + board[12] == board[21] == board[30] and board[12] != "-" + board[21] == board[30] == board[39] and board[21] != "-" + board[30] == board[39] == board[48] and board[30] != "-" + board[39] == board[48] == board[57] and board[39] != "-" + board[48] == board[57] == board[66] and board[48] != "-" + board[57] == board[66] == board[75] and board[57]!= "-":
        winner = board[3] 
        winner = board[12] 
        winner = board[21] 
        winner = board[30] 
        winner = board[39] 
        winner = board[48] 
        winner = board[57]

        
elif board[4] == board[13] == board[22] and board[4] != "-" + board[13] == board[22] == board[31] and board[12] != "-" + board[22] == board[31] == board[40] and board[22] != "-" + board[31] == board[40] == board[49] and board[31] != "-" + board[40] == board[49] == board[58] and board[40] != "-" + board[49] == board[58] == board[67] and board[49] != "-" + board[58] == board[67] == board[76] and board[58] != "-":
        winner = board[4] 
        winner = board[13] 
        winner = board[22] 
        winner = board[31] 
        winner = board[40] 
        winner = board[49] 
        winner = board[58] 


        
elif board[5] == board[14] == board[23] and board[5] != "-" + board[14] == board[23] == board[32] and board[13] != "-" + board[23] == board[32] == board[41] and board[23] != "-" + board[32] == board[41] == board[50] and board[32] != "-" + board[41] == board[50] == board[59] and board[41] != "-" + board[50] == board[59] == board[68] and board[50] != "-" + board[59] == board[68] == board[77] and board[59] != "-":
        winner = board[5] 
        winner = board[14] 
        winner = board[23] 
        winner = board[32] 
        winner = board[41] 
        winner = board[50] 
        winner = board[59] 

        
elif board[6] == board[15] == board[24] and board[6] != "-" + board[15] == board[24] == board[33] and board[14] != "-" + board[24] == board[33] == board[42] and board[24] != "-" + board[33] == board[42] == board[51] and board[33] != "-" + board[42] == board[51] == board[60] and board[42] != "-" + board[51] == board[60] == board[69] and board[51] != "-" + board[60] == board[69] == board[78] and board[60] != "-":
        winner = board[6] 
        winner = board[15] 
        winner = board[24] 
        winner = board[33] 
        winner = board[42] 
        winner = board[51] 
        winner = board[60]
       
elif board[7] == board[16] == board[25] and board[7] != "-" + board[16] == board[25] == board[34] and board[15] != "-" + board[25] == board[34] == board[43] and board[25] != "-" + board[34] == board[43] == board[52] and board[34] != "-" + board[43] == board[52] == board[61] and board[43] != "-" + board[52] == board[61] == board[70] and board[52] != "-" + board[61] == board[70] == board[79] and board[61] != "-":
        winner = board[7] 
        winner = board[16] 
        winner = board[25] 
        winner = board[34] 
        winner = board[43] 
        winner = board[52] 
        winner = board[61]

         
elif board[8] == board[17] == board[26] and board[8] != "-" + board[17] == board[26] == board[35] and board[16] != "-" + board[26] == board[35] == board[44] and board[26] != "-" + board[35] == board[44] == board[53] and board[35] != "-" + board[44] == board[53] == board[62] and board[44] != "-" + board[53] == board[62] == board[71] and board[53] != "-" + board[62] == board[71] == board[80] and board[62]!= "-":
        winner = board[8] 
        winner = board[17] 
        winner = board[26] 
        winner = board[35] 
        winner = board[44] 
        winner = board[53] 
        winner = board[62]


def checkDiag(board):
    global winner
    if board[0] == board[10] == board[20] and board[0] != "-" + board[10] == board[20] == board[30] and board[10] != "-" + board[20] == board[30] == board[40] and board[20] != "-" + board[30] == board[40] == board[50] and board[30] != "-" + board[40] == board[50] == board[60] and board[40] != "-" + board[50] == board[60] == board[70] and board[50] != "-" + board[60] == board[70] == board[80] and board[60] != "-":
        winner = board[0]
        winner = board[10]
        winner = board[20]
        winner = board[30]
        winner = board[40]
        winner = board[50]
        winner = board[60]
        return True

    elif board[1] == board[11] == board[21] and board[1] != "-" + board[11] == board[21] == board[31] and board[11] != "-" + board[21] == board[31] == board[41] and board[21] != "-" + board[31] == board[41] == board[51] and board[31] != "-" + board[41] == board[51] == board[61] and board[41] != "-" + board[51] == board[61] == board[71] and board[51] != "-":
        winner = board[0]
        winner = board[11]
        winner = board[21]
        winner = board[31]
        winner = board[41]
        winner = board[51]  
        return True
        
    elif board[2] == board[12] == board[22] and board[2] != "-" + board[12] == board[22] == board[32] and board[12] != "-" + board[22] == board[32] == board[42] and board[22] != "-" + board[32] == board[42] == board[52] and board[32] != "-" + board[42] == board[52] == board[62] and board[42] != "-":
        winner = board[2]
        winner = board[12]
        winner = board[22]
        winner = board[32]
        winner = board[42]
        return True

    elif board[3] == board[13] == board[23] and board[3] != "-" + board[13] == board[23] == board[33] and board[13] != "-" + board[23] == board[33] == board[43] and board[23] != "-" + board[33] == board[43] == board[53] and board[33] != "-":
        winner = board[3]
        winner = board[13]
        winner = board[23]
        winner = board[33]
        return True

    elif board[4] == board[14] == board[24] and board[4] != "-" + board[14] == board[24] == board[34] and board[14] != "-" + board[24] == board[34] == board[44] and board[24] != "-":
        winner = board[4]
        winner = board[14]
        winner = board[24]
        return True

    elif board[5] == board[15] == board[25] and board[5] != "-" + board[15] == board[25] == board[35] and board[15] != "-":
        winner = board[5]
        winner = board[15]
        return True

    elif board[6] == board[16] == board[26] and board[6] != "-":
        winner = board[6]
        return True

    elif board[9] == board[19] == board[29] and board[9] != "-" + board[19] == board[29] == board[39] and board[19] != "-" + board[29] == board[39] == board[49] and board[29] != "-" + board[39] == board[49] == board[59] and board[39] != "-" + board[49] == board[59] == board[69] and board[49] != "-" + board[59] == board[69] == board[79] and board[59] != "-":
        winner = board[9]
        winner = board[19]
        winner = board[29]
        winner = board[39]
        winner = board[49]
        winner = board[59]
        return True
     

    elif board[18] == board[28] == board[38] and board[18] != "-" + board[28] == board[38] == board[48] and board[28] != "-" + board[38] == board[48] == board[58] and board[38] != "-" + board[48] == board[58] == board[68] and board[48] != "-" + board[58] == board[68] == board[78] and board[58] != "-":
        winner = board[18]
        winner = board[28]
        winner = board[38]
        winner = board[48]
        winner = board[58]
        return True
       
      
    elif board[27] == board[37] == board[47] and board[27] != "-" + board[37] == board[47] == board[57] and board[17] != "-" + board[47] == board[57] == board[67] and board[47] != "-" + board[57] == board[67] == board[77] and board[57] != "-":
        winner = board[27]
        winner = board[37]
        winner = board[47]
        winner = board[57]
        return True
       
    elif board[36] == board[46] == board[56] and board[36] != "-" + board[46] == board[56] == board[66] and board[46] != "-" + board[56] == board[66] == board[76] and board[56] != "-":
        winner = board[36]
        winner = board[46]
        winner = board[56]
        return True
       
    elif board[45] == board[55] == board[65] and board[45] != "-" + board[55] == board[65] == board[75] and board[55] != "-":
        winner = board[45]
        winner = board[55]
        
        return True
    elif board[54] == board[64] == board[74] and board[54] != "-":
        winner = board[54]
       
        return True
    elif board[8] == board[16] == board[24] and board[8] != "-" + board[16] == board[24] == board[32] and board[16] != "-" + board[24] == board[32] == board[40] and board[24] != "-" + board[32] == board[40] == board[48] and board[32] != "-" + board[40] == board[48] == board[56] and board[40] != "-" + board[48] == board[56] == board[64] and board[48] != "-" + board[56] == board[64] == board[72] and board[56] != "-":
        winner = board[8]
        winner = board[16]
        winner = board[24]
        winner = board[32]
        winner = board[40]
        winner = board[56]  
        return True

    elif board[7] == board[15] == board[23] and board[7] != "-" + board[15] == board[23] == board[31] and board[15] != "-" + board[23] == board[31] == board[39] and board[23] != "-" + board[31] == board[39] == board[47] and board[31] != "-" + board[39] == board[47] == board[55] and board[39] != "-" + board[47] == board[55] == board[63] and board[47] != "-":
        winner = board[7]
        winner = board[15]
        winner = board[23]
        winner = board[31]
        winner = board[39]
        winner = board[47]
        return True

    elif board[6] == board[14] == board[22] and board[6] != "-" + board[14] == board[22] == board[30] and board[14] != "-" + board[22] == board[30] == board[38] and board[22] != "-" + board[30] == board[38] == board[46] and board[30] != "-" + board[38] == board[46] == board[54] and board[38] != "-":
        winner = board[6]
        winner = board[14]
        winner = board[22]
        winner = board[30]
        winner = board[38]
        return True
        
    elif board[5] == board[13] == board[21] and board[5] != "-" + board[13] == board[21] == board[29] and board[13] != "-" + board[21] == board[29] == board[37] and board[21] != "-" + board[29] == board[37] == board[45] and board[29] != "-":
        winner = board[5]
        winner = board[13]
        winner = board[21]
        winner = board[29]
        return True

    elif board[4] == board[12] == board[20] and board[4] != "-" + board[12] == board[20] == board[28] and board[12] != "-" + board[20] == board[28] == board[36] and board[20] != "-":
        winner = board[4]
        winner = board[12]
        winner = board[20]
        return True

    elif board[3] == board[11] == board[19] and board[3] != "-" + board[11] == board[19] == board[27] and board[11] != "-" :
        winner = board[3]
        winner = board[11]
        return True

    elif board[2] == board[10] == board[18] and board[2] != "-":
        winner = board[2]
        return True


def checkIfWin(board):
    global gameRunning
    if checkHorizontle(board):
        printBoard(board)
        print(f"The winner is {winner}!")
        gameRunning = False

    elif checkRow(board):
        printBoard(board)
        print(f"The winner is {winner}!")
        gameRunning = False

    elif checkDiag(board):
        printBoard(board)
        print(f"The winner is {winner}!")
        gameRunning = False


def checkIfTie(board):
    global gameRunning
    winner = None
    if winner is None:
        winner = []

    if "-" not in board + [winner] == [winner]:
        printBoard(board)
        print("It is a tie!")
        gameRunning = False
    



# switch player
def switchPlayer():
    global currentPlayer
    if currentPlayer == "S":
        currentPlayer = "O"
    else:
        currentPlayer = "S"


def computer(board):
    while currentPlayer == "O":
        position = random.randint(0, 80)
        if board[position] == "-":
            board[position] = "O"
            switchPlayer()


while gameRunning:
    printBoard(board)
    playerInput(board)
    checkIfWin(board)
    checkIfTie(board)
    switchPlayer()
    computer(board)
    checkIfWin(board)
    checkIfTie(board)
