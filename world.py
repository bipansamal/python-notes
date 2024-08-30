
# # sum = input("enter your name = ")
# # i = 1
# # while i <= 10:
# #     print("my name is", sum)

# #     i += 1
# # # use of continue in forloop ( yo vanyko ayouta number vanda aru chai chalx)
# # i = 0
# # while i <= 10:
# #     if i == 4:
# #         i += 1
# #         continue
# #     print(i)
# #     i += 1
# # writee from a to z
# # for i in range(ord('a'), ord('z') + 1):
# #     print(chr(i))

# # # writee from a to z
# # for i in range(ord('A'), ord('Z') + 1):
# #     print(chr(i), end=' ')

# # # from 1 to 100
# # for i in range(1, 101):
# #     print(i, end=' ')


# # multipilation table from 1 to 100. 






# # multipilication table

# # num = int(input("enter the number:"))
# # tableNum = int(input("how many table do you want?"))
# # for i in range(1,tableNum+1):
# #     print(num,"*",i,"=",num*i)


# # use of function and also \n
# # def name(s1,s2):
# #     print(s1,s2)

# # s1 = "my name is bipan magar\n"
# # s2 = "i am 20 years old"
# # name(s1,s2)


# # num = int(input("enter your number"))
# # name = int(input("inter number how long you want"))
# # for i in range(1,name+1):
# #     print(num,"*",i, "=" ,num*i)

# # creating a new function.
# # def multi_table(start,end):
# #      return start,end

# # num = int(input("enter your number"))
# # sum = int(input("how many table to you want"))
# # for i in range(1,sum+1):
# #      print(num,"*",i, "=", num*i)
    

# # # making a function .
# # def printname(s1,s2):
# #      return s1+s2
    
# # s1 = 5
# # s2 = 5
# # sum = printname(s1,s2)
# # print("it is:", sum)


# def print_board(board):
#     for row in board:
#         print(" | ".join(row))
#         print("-" * 5)

# def check_winner(board):
#     # Check rows, columns, and diagonals for a win
#     for row in board:
#         if row[0] == row[1] == row[2] and row[0] != " ":
#             return row[0]
    
#     for col in range(3):
#         if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
#             return board[0][col]
    
#     if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
#         return board[0][0]
    
#     if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
#         return board[0][2]

#     return None

# def tic_tac_toe():
#     board = [[" " for _ in range(3)] for _ in range(3)]
#     player = "X"

#     for _ in range(9):
#         print_board(board)
#         row = int(input(f"Player {player}, enter row (0-2): "))
#         col = int(input(f"Player {player}, enter column (0-2): "))
        
#         if board[row][col] == " ":
#             board[row][col] = player
#             winner = check_winner(board)
#             if winner:
#                 print_board(board)
#                 print(f"Player {winner} wins!")
#                 return
#             player = "O" if player == "X" else "X"
#         else:
#             print("Invalid move, try again.")
    
#     print_board(board)
#     print("It's a tie!")

# tic_tac_toe()

i = 1
while i <= 10:
    print(i)
    i += 1