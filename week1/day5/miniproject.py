#Mini-Project - Tic Tac Toe

two_D_list = [['1','2','3'],
              ['4','5','6'],
              ['7','8','9']]

# list1 = ["1", "2", "3"]
# print(" ".join(list1))
# string1 = "emily"
# print(string1)

def display_board(): #create function to print how the board is now
    for row in two_D_list: # loop into each unit, which are one of the three lists
        print(" ".join(row)) # use .join to put each number out putting a space in between
        # for cell in row:
            #print(cell)
display_board()


def player_input(player):
    action = input(f"Player {player}, Where do you want to place(1-9)? ") #3
    if action not in ['1','2','3','4','5','6','7','8','9']: #（添加输入验证）
        print("Invalid input, please choose 1-9")
        return False #don't continue, return to earlier step # 告诉主函数，这次输入失败

    for row in two_D_list:
        for cell in row:
            if action == cell: #compares the string 1-9 to the spot, if the number is 1-9
                index_cell = row.index(cell) #this action gets the number of input into spot #the use of .index() 在 row 这个列表中，找到元素 cell 第一次出现的位置（索引）.index() 是 列表（list）和字符串（str）对象的方法，用来查找某个元素或子字符串第一次出现的位置（索引）。
                row[index_cell] = player #replace the number with X or O
                display_board()
                return True # 成功下棋，返回 True
    print("That spot is already taken. Try again")
    return False

# player_input("X")
# player_input("O")

def check_winner():
    for row in two_D_list:
        if row == ['X','X','X']:
            return "X"
        elif row == ['O','O','O']:
            return "O"
    for col in range(3):
        if two_D_list[0][col] == two_D_list [1][col] == two_D_list [2][col] == "X":
            return "X"
        elif two_D_list[0][col] == two_D_list [1][col] == two_D_list [2][col] == "O":
            return "O"
    
    if two_D_list [0][0] == two_D_list [1][1] == two_D_list [2][2] == "X":
        return "X"
    elif two_D_list [0][0] == two_D_list [1][1] == two_D_list [2][2] == "O":
        return "O"
    elif two_D_list [2][0] == two_D_list [1][1] == two_D_list [0][2] == "X":
        return "X"
    elif two_D_list [2][0] == two_D_list [1][1] == two_D_list [0][2] == "O":
        return "O"
    
    return None



def playing_alternatively():
    current_player = "X"
    turn = 0 
    #use a while loop instead of for loop because maybe there are invalid input that doesnt count to the 9 times
    while turn < 9:
        print(f"Turn {turn+1}")

        valid_move = player_input(current_player)
        if not valid_move:
            continue
        
        winner = check_winner ()
        if winner: 
            print(f"{winner} wins!")
            break

        turn += 1

        #switch players
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"

    if turn == 9 and not winner: 
        print("It is a draw")

playing_alternatively()





    # for turn in range(9):
    #     print(f"Turn {turn+1}")
        
    #     if not player_input(current_player):
    #         continue
        # display_board()
        # player_input(current_player)    #this lets current player make a move
       
        # winner = check_winner()
        # if winner == "X":
        #     print("X wins")
        #     break
        # elif winner == "O":
        #     print ("O wins")
        #     break
        # elif turn == 8:
        #     print("It is a draw")

        # if current_player == "X": #here to switch players, if it is one player, change it to the other player
        #     current_player = "O" #after few turns(5 to be exact),if it meets conditon of one win, stop this loop
        # else:
        #     current_player = "X"
# playing_alternatively()

#now I need to add the condition to check if there is a bingo
# need to cut in the middle of the 9 times loop, to give a condition: 

#if 3 in a row, then stop the loop and print("X"/"O" wins!)
#?how do i check? in each input, check if the three are also same.
        #these two codes means conditions like the below:
        # if two_D_list[0][0] == two_D_list[1][0] == two_D_list[2][0] == "X": # if the same column is the same letter is true
        #     print("X wins")
        # elif two_D_list[0][0] == two_D_list[1][0] == two_D_list[2][0] == "O":
        #     print("O wins")
        # elif two_D_list[0][1] == two_D_list[1][1] == two_D_list[2][1] == "X": # if the same column is the same letter is true
        #     print("X wins")
        # elif two_D_list[0][1] == two_D_list[1][1] == two_D_list[2][1] == "O":
        #     print("O wins")
        # elif two_D_list[0][2] == two_D_list[1][2] == two_D_list[2][2] == "X": # if the same column is the same letter is true
        #     print("X wins")
        # elif two_D_list[0][2] == two_D_list[1][2] == two_D_list[2][2] == "O":
        #     print("O wins")
        

# def main():
#     player_input("X")
#     player_input("O")


# list2 = []
# for item in range(2,10):
#     list2.append(item)
# print(list2)

