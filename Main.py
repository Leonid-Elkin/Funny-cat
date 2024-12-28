import random
import math

def generateRandomMines(fieldNumber,mineNumber):    

    remainingFileds = fieldNumber
    remainingMines = mineNumber
    mines = []

    for rows in range (int(math.sqrt(fieldNumber))):
        mineRow = []
        for field in range (int(math.sqrt(fieldNumber))):
            mine = (random.randint(0,fieldNumber))  
            print(mine,remainingMines)
            if mine > remainingMines:
                mineRow.append("0")
            else:
                mineRow.append("M")
                mineNumber -= 1
        mines.append(mineRow)
    
    return mines


mines = generateRandomMines(9,1)

for items in mines:
    print(mines,end = '\n')

