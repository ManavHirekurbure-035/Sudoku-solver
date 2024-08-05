def fill_element(board):    
    for row in range(9):
        for col in range(9):            
            if board[row][col] == 0:
                pass
            else:
                row_array[row].append(board[row][col])
                column_array[col].append(board[row][col])
                box_array[row//3][col//3].append(board[row][col])
    
def check_row(row,col,board):        
    count = 0
    element = 0
    for i in range(1,10):               
        if i not in row_array[row]:                     
            count += 1
            element = i
    if count == 1:            
        board[row][col] = element
        
    

def check_col(row,col,board):    
    count = 0
    element = 0
    for i in range(1,10):        
        if i not in column_array[col]:            
            count += 1
            element = i
    if count == 1:            
        board[row][col] = element
        

def check_box(row,col,board): 
    r = row//3
    c = col//3   
    count = 0
    element = 0
    for i in range(1,10):        
        if i not in box_array[r][c]:            
            count += 1
            element = i
    if count == 1:            
        board[row][col] = element
        

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
                print("helo")
                                
                
                                
            
    

def solve():
    for row in range(4,5):        
        for col in range(9):
            if board[row][col] == 0:                
                # check_row(row,col,board)
                # check_col(row,col,board)
                # check_box(row,col,board)
                # check_more_row(row,board)
                check_more_col(col,board)
                
                
                
                
                
                

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

board = [
    [0, 6, 9, 7, 5, 0, 8, 0, 2],
    [0, 8, 0, 0, 9, 3, 0, 0, 0],
    [7, 0, 0, 0, 8, 2, 0, 9, 6],
    [0, 0, 0, 5, 0, 0, 0, 0, 0],
    [0, 5, 0, 3, 0, 7, 4, 0, 9],
    [3, 4, 7, 0, 2, 9, 0, 0, 1],
    [8, 7, 2, 0, 4, 5, 0, 1, 3],
    [0, 0, 0, 0, 3, 8, 0, 5, 0],
    [5, 0, 0, 2, 0, 0, 0, 0, 0]
]


fill_element(board)
solve()

for i in board:
    print(i)