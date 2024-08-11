def check_full(board):
    counter = 0
    flag = False
    for row in range(9):
        for col in range(9):            
            if board[row][col] == 0:
                flag = True   
                counter += 1
    
    return flag,counter         
    

def append_element(row, col, element):
    row_array[row].append(element)
    column_array[col].append(element)
    box_array[row//3][col//3].append(element)
    

def fill_element(board):    
    for row in range(9):
        for col in range(9):            
            if board[row][col] == 0:
                pass
            else:
                row_array[row].append(board[row][col])
                column_array[col].append(board[row][col])
                box_array[row//3][col//3].append(board[row][col])
    
# def check_row(row,col,board):        
#     count = 0
#     element = 0
#     for i in range(1,10):               
#         if i not in row_array[row]:                     
#             count += 1
#             element = i
#     if count == 1:            
#         board[row][col] = element
#         append_element(row,col,element)
        
        
    

# def check_col(row,col,board):    
#     count = 0
#     element = 0
#     for i in range(1,10):        
#         if i not in column_array[col]:            
#             count += 1
#             element = i
#     if count == 1:            
#         board[row][col] = element
#         append_element(row,col,element)
        

# def check_box(row,col,board): 
#     r = row//3
#     c = col//3   
#     count = 0
#     element = 0
#     for i in range(1,10):        
#         if i not in box_array[r][c]:            
#             count += 1
#             element = i
#     if count == 1:            
#         board[row][col] = element
#         append_element(row,col,element)
        

def check_more_row(row,board): 
    col_val = 0   
    for i in range(1,10):               
        if i not in row_array[row]: 
            count = 0                              
            for k in range(9):                
                if board[row][k] == 0:                                     
                    if (i not in column_array[k]) and (i not in box_array[row//3][k//3]):                                                                   
                        count += 1  
                        col_val = k
            if count == 1:                 
                board[row][col_val] = i
                append_element(row,col_val,i)
                
def check_more_box(row,col,board):    
    r=(row//3)*3  
    c=(col//3)*3  
    for i in range(1,10):
        if i not in box_array[row//3][col//3]:  
            counter = 0            
            for m in range(r,r+3):
                for n in range(c,c+3):   
                    if board[m][n] == 0:                               
                        if (i not in row_array[m]) and (i not in column_array[n]):                                                      
                            counter += 1  
                            row_val = m
                            col_val = n                          
            if counter == 1: 
                board[row_val][col_val] = i                  
                append_element(row_val,col_val,i)                         
                        
                
def check_more_col(col,board):    
    row_val = 0   
    for i in range(1,10):               
        if i not in column_array[col]: 
            count = 0                              
            for k in range(9):                
                if board[k][col] == 0:                                     
                    if (i not in row_array[k]) and (i not in box_array[k//3][col//3]):                                                                   
                        count += 1  
                        row_val = k
            if count == 1:                 
                board[row_val][col] = i
                append_element(row_val,col,i)
                
                                
                


            
    

def solve():
    for row in range(9):        
        for col in range(9):
            if board[row][col] == 0:                
                # check_row(row,col,board)
                # check_col(row,col,board)
                # check_box(row,col,board)
                check_more_row(row,board)
                check_more_col(col,board)
                check_more_box(row,col,board)
            

                             
                
                
                
                
                

# Will contain the numbers present in each box
box_array = [
    [[],[],[]],
    [[],[],[]],
    [[],[],[]],
]

# Will contain the numbers present in each rpw
row_array = [
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    []
]

# Will contain the numbers present in each column
column_array = [
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    []
]

# board = [
#     [4, 0, 3, 0, 2, 0, 0, 7, 1],
#     [2, 6, 0, 0, 5, 0, 0, 4, 9],
#     [9, 0, 8, 4, 0, 0, 0, 5, 6],
#     [0, 4, 2, 0, 0, 7, 0, 0, 0],
#     [0, 0, 0, 0, 4, 0, 9, 1, 5],
#     [1, 0, 9, 5, 0, 0, 0, 0, 7],
#     [3, 8, 0, 2, 0, 9, 7, 0, 0],
#     [0, 2, 1, 0, 3, 0, 5, 0, 8],
#     [7, 9, 0, 0, 0, 0, 0, 0, 0]
# ]
board = [
    [0, 0, 0, 4, 6, 5, 1, 9, 3],
    [0, 3, 1, 0, 0, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 3, 0, 0, 0],
    [1, 0, 0, 5, 0, 8, 3, 2, 0],
    [3, 0, 0, 0, 0, 0, 0, 0, 7],
    [0, 9, 0, 0, 3, 0, 6, 0, 5],
    [8, 6, 0, 0, 0, 0, 0, 5, 4],
    [5, 0, 0, 8, 9, 0, 0, 0, 0],
    [0, 0, 0, 0, 5, 4, 7, 0, 8]
]

fill_element(board)
countEmpty = 0
flag = True
while(flag):
    solve()    
    flag,count = check_full(board)
    if count == countEmpty : 
        # flag = False              
        break 
    countEmpty = count 

if flag:
    print("Sudoku could not be solved")    
else:
    print("\n*************************************")
    print("Sudoku solved")
    for i in board:
        print(i)
    print("\n*************************************")