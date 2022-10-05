def checkForWinner(x_list,o_list,coordinates_dict,size_of_table,amount_for_win,xo_current,coor_current):
    
    for i in range(len(x_list)):
        x_list[i] = x_list[i].copy()
    for i in range(len(o_list)):
        o_list[i] = o_list[i].copy()
    x_coors = list(coordinates_dict.keys())
    y_coors = [i for i in coordinates_dict[x_coors[0]]]

    board = getBoard(x_coors,y_coors,x_list,o_list,size_of_table)
    for j in range(len(x_coors)):
        if coor_current[0] == x_coors[j]:
            coor_current[0] = j
    for j in range(len(y_coors)):
        if coor_current[1] == y_coors[j]:
            coor_current[1] = j

    row_to_check = board[coor_current[1]]

    column_to_check = []
    for i in range(len(board)):
        column_to_check.append(board[i][coor_current[0]])

    
    diagonal_to_check = []
    diagonal_x = coor_current[0]
    diagonal_y = coor_current[1]
    for i in range(len(board)):
        if diagonal_x-1 >= 0 and diagonal_y-1 >= 0:
            diagonal_y -= 1
            diagonal_x -= 1
    for i in range(len(board)):
        if diagonal_x+1 <= size_of_table-1 and diagonal_y+1 <= size_of_table-1:
            diagonal_to_check.append(board[diagonal_y][diagonal_x])
            diagonal_y += 1
            diagonal_x += 1

    diagonal2_to_check = []
    diagonal2_x = coor_current[0]
    diagonal2_y = coor_current[1]
    for i in range(len(board)):
        if diagonal2_x+1 <= size_of_table-1 and diagonal2_y-1 >= 0:
            diagonal2_y -= 1
            diagonal2_x += 1
    for i in range(len(board)):
        if diagonal2_x-1 >= 0 and diagonal2_y+1 <= size_of_table-1:
            diagonal2_to_check.append(board[diagonal2_y][diagonal2_x])
            diagonal2_y += 1
            diagonal2_x -= 1



    if checkLine([diagonal2_to_check,diagonal_to_check,row_to_check,column_to_check],amount_for_win,xo_current):
        return True

def checkLine(lists_to_check,amount_for_win,xo_current):
    for list in lists_to_check:
        longest_same_in_line = 0
        same_in_line = 0
        last_one_was_same = False
        for i in list:
            if i == xo_current:
                same_in_line += 1
                last_one_was_same = True
                if same_in_line > longest_same_in_line:
                    longest_same_in_line = same_in_line
            elif last_one_was_same:
                last_one_was_same = False
                same_in_line = 0
        if longest_same_in_line >= amount_for_win:
            return True

def getBoard(x_coors,y_coors,x_list,o_list,size_of_table):
    x_list = x_list.copy()
    o_list = o_list.copy()
    for i in range(len(x_list)):
        x_list[i] = x_list[i].copy()
    for i in range(len(o_list)):
        o_list[i] = o_list[i].copy()
    board_in_getBoard = []
    for i in range(size_of_table):
        board_in_getBoard.append([0 for j in range(size_of_table)])
    for i in range(len(x_list)):
        for j in range(len(x_coors)):
            if x_list[i][0] == x_coors[j]:
                x_list[i][0] = j
    for i in range(len(x_list)):
        for j in range(len(y_coors)):
            if x_list[i][1] == y_coors[j]:
                x_list[i][1] = j
    for i in range(len(o_list)):
        for j in range(len(x_coors)):
            if o_list[i][0] == x_coors[j]:
                o_list[i][0] = j
    for i in range(len(o_list)):
        for j in range(len(y_coors)):
            if o_list[i][1] == y_coors[j]:
                o_list[i][1] = j
    for i in x_list:
        board_in_getBoard[i[1]][i[0]] = "x"
    for i in o_list:
        board_in_getBoard[i[1]][i[0]] = "o"
    return board_in_getBoard



"""
board = [
    [0, 0, 0, x]
    [0, 0 ,0, 0]
    [0, o, 0, 0]
    [o, 0, x, 0]
]


return either:
    (True,"o")
    (True, "x")
    (False, None)


x_list and o_list : 
        [(;),(;),(;)]
    list of tuples


coordinates_dict :
        {
        123: [12, 34, 56]
        234: [12, 34, 56]
        345: [12, 34, 56]
        }
    keys are int, elements are lists of int

"""