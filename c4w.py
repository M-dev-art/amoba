def checkForWinner(x_list,o_list,coordinates_dict):
    xcoors = list(coordinates_dict.keys())
    ycoors = [i for i in coordinates_dict[xcoors[0]]]
    for i in range(3):
        if ((xcoors[i],ycoors[0]) in x_list) and ((xcoors[i],ycoors[1]) in x_list) and ((xcoors[i],ycoors[2]) in x_list):
            return (True,"x")
    for i in range(3):
        if ((xcoors[i],ycoors[0]) in o_list) and ((xcoors[i],ycoors[1]) in o_list) and ((xcoors[i],ycoors[2]) in o_list):
            return (True,"o")
    for i in range(3):
        if ((xcoors[0],ycoors[i]) in x_list) and ((xcoors[1],ycoors[i]) in x_list) and ((xcoors[2],ycoors[i]) in x_list):
            return (True,"x")
    for i in range(3):
        if ((xcoors[0],ycoors[i]) in o_list) and ((xcoors[1],ycoors[i]) in o_list) and ((xcoors[2],ycoors[i]) in o_list):
            return (True,"o")
    if ((xcoors[0],ycoors[0]) in o_list) and ((xcoors[1],ycoors[1]) in o_list) and ((xcoors[2],ycoors[2]) in o_list):
        return (True,"o")
    if ((xcoors[0],ycoors[2]) in o_list) and ((xcoors[1],ycoors[1]) in o_list) and ((xcoors[2],ycoors[0]) in o_list):
        return (True,"o")
    if ((xcoors[0],ycoors[0]) in x_list) and ((xcoors[1],ycoors[1]) in x_list) and ((xcoors[2],ycoors[2]) in x_list):
        return (True,"x")
    if ((xcoors[0],ycoors[2]) in x_list) and ((xcoors[1],ycoors[1]) in x_list) and ((xcoors[2],ycoors[0]) in x_list):
        return (True,"x")
    if len(x_list) + len(o_list) == 9:
        return (True, 'no one')
    return (False,None)



"""
x_list and o_list : 
        [(),(),()]
    list of tuples

coordinates_dict :
        {
        123: [12, 34, 56]
        234: [1,1,1]
        132: [1,13,3]
        }
    keys are int, elements are lists of int
 """